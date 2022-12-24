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

* **get_page_content(url : str ,endpoint : str or None=None ,session : any or None=None ,error : bool=False ,warns : bool=True)**  -> tuple[str, int] ¦ Get the content of a page as text.
* **get_first_wiki_paragraph(url : str ,endpoint : str,session : any or None=None,error : bool=False,warns : bool=True)**  -> tuple[str, int] ¦ Get the first paragraph of a wikipedia page as text.
* **get_multiple_page_content(urls : list[str] ,endpoints : list[str] or None=None ,session : any or None=None ,error : bool=False ,warns : bool=True)**  -> tuple[dict[str : str] , dict[str : int]] ¦ Get the content of multiple pages as a dictionary url - text.
* **get_multiple_endpoint_content(url : str ,endpoints : list[str] or None=None ,session : any or None=None ,error : bool=False ,warns : bool=True)**  -> tuple[dict[str : str] or str, dict[str : int] or int] ¦ Get the content of multiple pages by endpoint as a dictionary url - text or as a text if no endpoint was given.

### [Text_cleaner.py](https://github.com/Flotchet/Wikipedia_Scraper/blob/master/Standardized_for_other_projetcs/Text_cleaner.py "Text_cleaner.py")

#### Prerequises

Python 3.10

* re
* pandas
* matplotlib
* lorem_text
* nltk

#### List of functions


* **clean_text_by_regex(text : str , regex_list : str or list[str])** -> str ¦ Clean a text by a list of regex.
* **ctbr(text : str , regex_list : str or list[str])** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_html_tags_from_text(text : str)** -> str ¦ Remove all the html tags from a text.
* **rtft(text : str)** -> str  ¦
  Its the same function as before but with a shorter name.
* **remove_parenthesis_from_text(text : str)** -> str ¦ Remove all the parenthesis from a text.
* **rpft(text : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_braces_from_text(text : str)** -> str ¦ Remove all the braces from a text.
* **rbft(text : str)** -> str ¦
  Its the same function as before but with a shorter name.
* **remove_brackets_from_text(text : str)** -> str ¦ Remove all the brackets from a text.
* **rbktft(text : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_all_types_of_brackets_fror_text(text : str)** -> str ¦ Remove all the brackets from a text.
* **rabft(text : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_new_line_from_text(text : str)** -> str ¦ Remove all the new line from a text.
* **rnlft(text : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_carriage_return_from_text(text : str)** -> str ¦ Remove all the carriage return from a text.
* **rcrft(text : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_carriage_return_line_feed_from_text(text : str)** -> str ¦ Remove all the carriage return line feed from a text.
* **rcrnlft(text : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_tab_from_text(text : str)** -> str ¦ Remove all the tab from a text.
* **rtabft(text : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_non_breaking_space_from_text(text : str)** -> str ¦ Remove all the non breaking space from a text.
* **rnbsft(text : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_non_breaking_hyphen_from_text(text : str)** -> str ¦ Remove all the non breaking hyphen from a text.
* **rnbfhft(text : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_punctuation_characters_from_text(text : str)** -> str ¦ Remove all the punctuation characters from a text.
* **rpcft(text : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_numbers_from_text(text : str)** -> str ¦ Remove all the numbers from a text.
* **rnumft(text : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_multiple_spaces_from_text(text : str)** -> str ¦ Remove all the multiple spaces from a text.
* **rmspft(text : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_special_character_from_text(text : str)** -> str ¦ Remove all the special character from a text.
* **rscft(text : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_control_character_from_text(text : str)** -> str ¦ Remove all the control character from a text.
* **rccft(text : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_all_non_alphanumeric_characters_from_text(text : str)** -> str ¦ Remove all the non alphanumeric characters from a text.
* **rnaacft(text : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **remove_stop_words_from_text(text : str, stop_words : list[str])** -> str ¦ Remove all the stop words from a text.
* **rswft(text : str, stop_words : list[str])** -> str **¦**
  Its the same function as before but with a shorter name.
* **get_stop_words(language : str)** -> list[str] ¦ Get the stop words of a language and return them as a list.
* **remove_stop_words_from_text_by_language(text : str, language : str)** -> str ¦ Remove all the stop words from a text by language.
* **rswftbl(text : str, language : str)** -> str **¦**
  Its the same function as before but with a shorter name.
* **dictionary_of_frequency_of_words(text : str)** -> dict[str : int] ¦ Return a dictionary of the frequency of words in a cleaned text.
* **dict_of_w_f(text : str)** -> dict[str : int] **¦**
  Its the same function as before but with a shorter name.
* **dictionary_of_frequency_of_words_in_a_list_of_text(list_of_text : list[str])** -> dict[str : int] ¦ Return a dictionary of the frequency of words in a list of cleaned text.
* **dict_of_w_f_in_a_lot(text : list[str])** -> dict[str : int] **¦**
  Its the same function as before but with a shorter name.
* **bar_plot_of_words_frequencies(words : dict[str : int]or list[list[str], list[int]])** -> None ¦ Plot a bar plot of the frequency of words.
