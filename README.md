# Wikipedia scraping project

## Current state

Currently in the To go further part

## prerequise

* warnings
* functools
* re
* time
* json
* requests
* bs4
* urllib3.exceptions

## What it does

Get all the leaders from a series of countries from https://country-leaders.onrender.com and get a informations about them, scrape some data from wikipedia and store them in a json file with this structure:

Country : list of leaders ->

* "id" : str "Q"+"int"
* "first_name" : str
* "last_name" : str
* "birth_date" : str "yyyy-mm-dd"
* "death_date" : str "yyyy-mm-dd"
* "place_of_birth" : str
* "wikipedia_url" : str URL -> "https://"   + "contry" + ".wikipedia.org/wiki/" + "endpoint"
* "start_mandate" : str "yyyy-mm-dd"
* "end_mandate" : str "yyyy-mm-dd"
* "first_paragraph" : str

## How to use it

just run the leaders_scraper.py and it should do the trick!
