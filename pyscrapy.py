from bs4 import BeautifulSoup

import requests


#tag = raw_input("Enter the tags you want to search in the site:")

url = raw_input("Enter a website to extract the URL's from: ")

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

def links():
	for link in soup.find_all('a'):
	    print(link.get('href'))

def texts():
	print(soup.get_text())

def tags():
	for tag in soup.find_all(True):
		print(tag.name)

ch = input("Enter your choice of function ")

options = {0 : links,
	   1 : texts,
	   2 : tags,
         
}

options[ch]()


