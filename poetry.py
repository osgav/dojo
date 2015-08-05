#!/usr/bin/env python

# Python Dojo Edinburgh 04/Aug/15

# write a Poetry Generator...

import random
import requests
import re
from bs4 import BeautifulSoup


POEMHUNTER_URL = "http://www.poemhunter.com"
POEMHUNTER_SEARCH = "http://www.poemhunter.com/search/?q="
# Thank you for the poems


def page_source(url):
	# make a HTTP GET request to the URL passed
	# in and return a BeautifulSoup object
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	return soup


def main():
	# what shall we be searching for then?
	user_input = raw_input('\nWhat would you like to hear a poem about?  ')

	# build URL to pass to page_source function
	# and retrieve source HTML for parsing
	poem_search_url = POEMHUNTER_SEARCH + user_input.replace(' ', '+')
	search_results_soup = page_source(poem_search_url)
    
    # find specific 'poem' URLs from search results
    # source and construct absolute URLs from relative paths
	poem_rel_urls = search_results_soup.findAll('a', href=re.compile(r'/poem/'))
	poem_abs_urls = [POEMHUNTER_URL + i['href'] for i in poem_rel_urls]

	# empty list to build the poem
	poem_lines = []

	# loading words
	loading = ["hmmm...", "thinking...", user_input + "..."]

	print "\n"

	# for each of the poem webpage URLs
	# print a random loading word, grab the page
	# source HTML and extract the first <p> with
	# no class attribute
	# split the contents of the <p> tag by line 
	# breaks (<br/>) and add the second line to
	# poem_lines list
	for url in poem_abs_urls:
		print loading[random.randint(0,2)]
		poem_soup = page_source(url)
		poetry = poem_soup.find('p', attrs={"class":None})
		poem_lines.append(str(poetry).split('<br/>')[1])

	print "\n Have you heard this one before?\n"

	# write poetry
	for line in poem_lines:
		print line.strip()

	print "\n"


if __name__ == "__main__":
	main()







