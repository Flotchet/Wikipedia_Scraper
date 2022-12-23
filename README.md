# Wikipedia scraping project

## Current state

Currently in the To go further part and making the code reusable in other projects

## prerequises

Python 3.10

* warnings
* functools
* re
* time
* json
* requests
* bs4
* urllib3.exceptions

## What it does

Get all the leaders from a series of countries from https://country-leaders.onrender.com and get a set of informations about each of them, scrape some data from wikipedia and store them in a json file with this structure:

Country : list of leaders ->

* "id" : str "Q"+"int"
* "first_name" : str
* "last_name" : str
* "birth_date" : str "yyyy-mm-dd"
* "death_date" : str "yyyy-mm-dd"
* "place_of_birth" : str
* "wikipedia_url" : str URL -> "https://"   + "country-prefix" + ".wikipedia.org/wiki/" + "endpoint"
* "start_mandate" : str "yyyy-mm-dd"
* "end_mandate" : str "yyyy-mm-dd"
* "first_paragraph" : str

## How to use it

just run the leaders_scraper.py and it should do the trick!

## Informations about the standardized files

### [HTTP_code_analyzer.py](https://github.com/Flotchet/Wikipedia_Scraper/blob/master/Standardized_for_other_projetcs/HTTP_code_analyzer.py "HTTP_code_analyzer.py")

#### Prerequisess

Python 3.10

* functools

#### List of functions

* **status_to_text_summarized**(**status_code**: **int**)  -> str **¦**
  Convert an int into the corresponding status code message.
* **stts**(**status_code**: **int**)  -> str **¦**
  Its the same function as before but with a shorter name.
* **status_to_text_complete**(**status_code**: **int**)  *->* dict[**str**:**str**] **¦**
  Convert an int into the corresponding status code message and
  a bit of information concerning the status_code in the form of a
  dictionary with the keys "Response" and "Explaination".
* **sttc**(**status_code**: **int**)  -> dict[**str**:**str**] **¦**
  Its the same function as before but with a shorter name.
* **sttc_as_text**(**status_code**: **int**) -> str **¦**
  Convert an int into the corresponding status code message and
  a bit of information concerning the status_code as a multiline text.
* **stt**(**status_code**: **int**)  -> str **¦**
  Its the same function as before but with a shorter name.

### [Get_DATA.py](https://github.com/Flotchet/Wikipedia_Scraper/blob/master/Standardized_for_other_projetcs/Get_DATA.py "Get_DATA.py")

#### Prerequisess

Python  3.10

* json
* pandas
* numpy
* pickle
* os

#### List of functions

* **save_data(data : any, path : str, name : str, format : str, error : bool = False, warns : bool = True)** -> int  ¦
  Save a data object (dict, list, np.ndarray, pd.DataFrame) into a file format(csv,txt,json,pickle).
* **save_data_to_json(data : dict[any:any], path : str, name : str, error : bool = False, warns : bool = True)** -> int **¦**
  Save a dictionary in the form of a json file.
* **save_data_to_csv(data : any , path : str, name : str, error : bool = False,warns : bool = True)** -> int **¦**
  Save a data object (dict, list, np.ndarray, pd.DataFrame) into a csv file.
* **save_data_to_txt(data : any , path : str, name : str, error : bool = False,warns : bool = True)** -> int **¦**
  Save a data object (str, int, float, dict, list, np.ndarray, pd.DataFrame) into a txt file.
* **save_data_to_pickle(data : any , path : str, name : str, error : bool = False,warns : bool = True)** -> int **¦**
  Save any serealizable object into a pickle file.
* **load_json(path : str, name : str, error : bool = False,warns : bool = True) ->** tuple[dict:int] **¦**
  Load a json file as a dictionary.
* **load_csv(path : str, name : str, error : bool = False,warns : bool = True)** -> tuple[any:int] **¦**
  Load a csv file as a pandas dataframe.
* **load_txt(path : str, name : str, error : bool = False,warns : bool = True)** -> tuple[str, int] **¦**
  Load a txt file as a string.
* **load_pickle(path : str, name : str, error : bool = False,warns : bool = True)** -> tuple[any, int] **¦**
  Load a pickle file into an object.

### [Get_page_content.py](https://github.com/Flotchet/Wikipedia_Scraper/blob/master/Standardized_for_other_projetcs/Get_page_content.py "Get_page_content.py")

#### Prerequisess

Python 3.10

* requests
* bs4
* warnings

#### List of functions

* **get_page_content(url : str ,endpoint : strorNone=None ,session : anyorNone=None ,error : bool=False ,warns : bool=True)**  -> tuple[str, int] ¦ Get the content of a page as text.
* **get_first_wiki_paragraph(url : str ,endpoint : str,session : anyorNone=None,error : bool=False,warns : bool=True)**  -> tuple[str, int] ¦ Get the first paragraph of a wikipedia page as text.
* **get_multiple_page_content(urls : list[str] ,endpoints : list[str]orNone=None ,session : anyorNone=None ,error : bool=False ,warns : bool=True)**  -> tuple[dict[str : str] , dict[str : int]] ¦ Get the content of multiple pages as a dictionary url - text.
* **get_multiple_endpoint_content(url : str ,endpoints : list[str]orNone=None ,session : anyorNone=None ,error : bool=False ,warns : bool=True)**  -> tuple[dict[str : str]orstr, dict[str : int]orint] ¦ Get the content of multiple pages by endpoint as a dictionary url - text or as a text if no endpoint was given.
