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

### List of functions

* **status_to_text_summarized**(**status_code**: **int**)  -> str
  convert an int into the corresponding status code message
* **stts**(**status_code**: **int**)  -> str
  Its the same function as before but with a shorter name
* **status_to_text_complete**(**status_code**: **int**)  *->* dict[**str**:**str**]
  convert an int into the corresponding status code message and
  a bit of information concerning the status_code in the form of a
  dictionary with the keys "Response" and "Explaination".
* **sttc**(**status_code**: **int**)  -> dict[**str**:**str**]
  Its the same function as before but with a shorter name
* **sttc_as_text**(**status_code**: **int**) -> str
  convert an int into the corresponding status code message and
  a bit of information concerning the status_code as a multiline text
* **stt**(**status_code**: **int**)  -> str
  Its the same function as before but with a shorter name
