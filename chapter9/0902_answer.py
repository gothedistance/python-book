import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.urlopen('http://quality-start.in/company/')

soup = BeautifulSoup(req,"html.parser")

side_menu = soup.find('div',class_='list-group')
for a_tags in side_menu.find_all('a'):
    print(a_tags.string)
