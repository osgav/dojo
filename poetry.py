#!/usr/bin/env python

# Python Dojo Edinburgh 04/Aug/15

# write a Poetry Generator...

import requests
import re
from bs4 import BeautifulSoup



POEMHUNTER_URL = "http://www.poemhunter.com"
POEMHUNTER_SEARCH = "http://www.poemhunter.com/search/?q="


def page_source(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	return soup


def main():
	
	user_input = raw_input('Poems about what? ')

	poem_search_url = POEMHUNTER_SEARCH + user_input.replace(' ', '+')
	search_results_soup = page_source(poem_search_url)
    
	poem_rel_urls = search_results_soup.findAll('a', href=re.compile(r'/poem/'))
	poem_abs_urls = [POEMHUNTER_URL + i['href'] for i in poem_rel_urls]

	for url in poem_abs_urls:
		poem_soup = page_source(url)
		poetry = poem_soup.find('p', attrs={"class":None})
		print poetry.text

if __name__ == "__main__":
	main()







