import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.urlopen('http://quality-start.in/company/')

soup = BeautifulSoup(req,"html.parser")

print(soup.find('h1').text)
