import warnings
import functools
import re
import time
import json
from requests import Session
import bs4
from urllib3.exceptions import NewConnectionError

cache = {}
def hashable_cache(f):
    def inner(url, session):
        if url not in cache:
            cache[url] = f(url, session)
        return cache[url]
    return inner


@functools.lru_cache(maxsize=None)
def status_to_text(status_code: int) -> str:

    """
    Convert a status code to a text message.
    take int as an entry
    return str as an output
    """
    # Convert a status code to a text message.

    status_dict = {
        # infos response
        100: "Continue",
        101: "Switching Protocols",
        102: "Processing",
        103: "Early Hints",
        # success response
        200: "OK",
        201: "Created",
        202: "Accepted",
        203: "Non-Authoritative Information",
        204: "No Content",
        205: "Reset Content",
        206: "Partial Content",
        207: "Multi-Status",
        208: "Already Reported",
        226: "IM Used",
        # redirection response
        300: "Multiple Choices",
        301: "Moved Permanently",
        302: "Found",
        303: "See Other",
        304: "Not Modified",
        305: "Use Proxy",
        306: "Switch Proxy",
        307: "Temporary Redirect",
        308: "Permanent Redirect",
        # client error response
        400: "Bad Request",
        401: "Unauthorized",
        402: "Payment Required",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        406: "Not Acceptable",
        407: "Proxy Authentication Required",
        408: "Request Timeout",
        409: "Conflict",
        410: "Gone",
        411: "Length Required",
        412: "Precondition Failed",
        413: "Payload Too Large",
        414: "URI Too Long",
        415: "Unsupported Media Type",
        416: "Range Not Satisfiable",
        417: "Expectation Failed",
        418: "I'm a teapot",
        421: "Misdirected Request",
        422: "Unprocessable Entity",
        423: "Locked",
        424: "Failed Dependency",
        425: "Too Early",
        426: "Upgrade Required",
        428: "Precondition Required",
        429: "Too Many Requests",
        431: "Request Header Fields Too Large",
        451: "Unavailable For Legal Reasons",
        # server error response
        500: "Internal Server Error",
        501: "Not Implemented",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Timeout",
        505: "HTTP Version Not Supported",
        506: "Variant Also Negotiates",
        507: "Insufficient Storage",
        508: "Loop Detected",
        510: "Not Extended",
        511: "Network Authentication Required"
    }
    # find if the status code is in the keys
    if status_code in status_dict.keys():
        return str(status_code) + ": " + status_dict[status_code]
    else:
        return str(status_code) + ": Unknown or unofficial status code"


@functools.lru_cache(maxsize=None)
def get_lead(sess : any) -> dict[str : list[dict]]:

    """ 
    get all the leaders in their respective countries with some infos.
    take a session as an entry
    return a dict with the country as key and a list of dict as value
    """
    # get all the leaders in their respective countries with some infos.

    root_url = "https://country-leaders.onrender.com"
    cookie_url = "/cookie"
    country_url = "/countries"
    leaders_url = "/leaders"

    requ = sess.get(root_url + cookie_url)
    cookies = requ.cookies

    requ1 = sess.get(root_url + country_url, cookies=cookies)
    countries = requ1.json()

    lead = [sess.get(root_url + leaders_url,
                     cookies=cookies,
                     params={"country": country}).json() for country in countries]

    leaders_dict = dict(map(lambda i, j: (i, j), countries, lead))

    return leaders_dict


@hashable_cache
def get_first_paragraph(url : str, sess : any) -> str:

    """
    get the first paragraph of the content of a wikipedia page.
    take a url and a session as an entry
    return a str with the first paragraph of the wikipedia page
    """
    # get the first paragraph of the content of a wikipedia page.

    root_url = "https://country-leaders.onrender.com"
    status_url = "/status"

    regex_list = [r"\ *\(/.+/\[e\].*\)",
                  r"\ *\(/.+/.*\)",
                  r"\[[0-9]+\]",
                  r"[\n]",
                  r"[\t]",
                  r"[\xa0]"]

    req = sess.get(url=url)

    # print the content of the webpage if stautus is 200
    if req.status_code != 200:
        message = root_url + status_url + " " + status_to_text(req.status_code)
        warnings.warn(message)
        return message

    soup = bs4.BeautifulSoup(req.text, "html.parser")

    for paragraph in soup.find_all('p'):

        for _ in paragraph.find_all('b'):

            text = paragraph.text

            for regex in regex_list:

                pattern = re.compile(regex)
                text = re.sub(pattern, "", text)

            return text


def get_leaders() -> tuple[dict[str : list[dict]], str]:
    with Session() as session:

        """
        get all the leaders in their respective countries with some infos
        + the first wikipedia paragraph for each leader.
        takes no entry
        return a dict with the country as key and a list of dict as value
        and a str with the code of the error
        """
        # get all the leaders in their respective countries with some infos
        # + the first wikipedia paragraph for each leader.

        leaders_per_country = get_lead(session)
        code = 0

        for country, leaders in leaders_per_country.items():

            for leader in leaders:

                try:
                    leaders_per_country[country][leaders.index(
                        leader)]["first_paragraph"] = get_first_paragraph(
                            leader["wikipedia_url"], session)

                    if code == 0:
                        code = "scr-0"

                except NewConnectionError as nce:
                    leaders_per_country[country][leaders.index(
                        leader)]["first_paragraph"] = "NewConnectionError" + str(nce)
                    print(str(nce))
                    code = "scr-1"
                    continue

                except Exception as E:
                    leaders_per_country[country][leaders.index(
                        leader)]["first_paragraph"] = "Error" + str(nce)
                    print(str(E))
                    code = "scr-2"
                    continue

    return leaders_per_country, code;


def save_leaders_to_json(filename, leaders_per_country):

    """
    save the leaders_per_country dict to a json file
    take a filename and a dict as an entry
    return a str with a code of the result to check if
    the saving was done correctly
    """
    # save the leaders_per_country dict to a json file

    test = leaders_per_country[list(leaders_per_country.keys())[0]][0]["first_paragraph"]
    with open(filename, "w") as the_file:
        print("saving...")
        json.dump(leaders_per_country, the_file)

    with open(filename, "r") as the_file:
        leaders_per_country = json.load(the_file)
        if test == leaders_per_country[list(leaders_per_country.keys())[0]][0]["first_paragraph"]:
            print("Success! Scraping done!")
            return "sjs-0"
        else:
            print("Error during saving! Try again...")
            return "sjs-1"

    return "sjs-2"


def main():

    """
    main function
    takes no entry
    return 0 if termineted correctly
    """
    # main function


    print("starting")

    code = "main-0"
    start = time.time()
    leaders_per_country,code = get_leaders()

    if code == "scr-0":
        print("scraping went smoothly")
    if code == "scr-1":
        print("scraping failed at some point due to a NewConnectionError")
    if code == "scr-2":
        print("scraping failed at some point due to an error")

    end = time.time()

    print("Elapsed time: " + str(end - start))
    code = save_leaders_to_json("leaders.json", leaders_per_country)

    return code


if __name__ == "__main__":
    main()
