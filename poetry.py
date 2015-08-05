#!/usr/bin/env python

# Python Dojo Edinburgh 04/Aug/15

# write a Poetry Generator...

import requests
import re
from bs4 import BeautifulSoup



POEM_URL = "http://www.poemhunter.com"

userinput = raw_input('Poems about what? ')

poetrysearchqueryurl = "http://www.poemhunter.com/search/?q=" + userinput.replace(' ', '+')



searchresultsresponseobject = requests.get(poetrysearchqueryurl)
soup = BeautifulSoup(searchresultsresponseobject.text)

lists = soup.findAll('a', href=re.compile(r'/poem/'))



gets = [POEM_URL + i['href'] for i in lists]



for url in gets:
	
	poemresponseobject = requests.get(url)
	soup = BeautifulSoup(poemresponseobject.text,)
	poetry = soup.find('p', attrs={"class":None})

	#print str(poetry.text).split(' ')
	print poetry.text












