import requests
from bs4 import BeautifulSoup
import re
import sqlite3
import random

def link_catalog():
    soup = BeautifulSoup(requests.get('https://www.onliner.by/').text, 'lxml')
    return ([a['href'] for a in soup.find_all('a', href=True, class_="project-navigation__link project-navigation__link_primary")])

def name_news():
    soup = BeautifulSoup(requests.get('https://www.onliner.by/').text, 'lxml')
    name_news=list(map(lambda x: x.strip(), [i.text for i in soup.find_all(class_="project-navigation__text")]))[1:]
    return (name_news)

# print(random.choice(link_catalog()))
soup = BeautifulSoup(requests.get(random.choice(link_catalog())).text, 'lxml')
# soup = BeautifulSoup(requests.get('https://catalog.onliner.by/pram').text, 'lxml')
name_product = list(map(lambda x: x.strip(), [i.text for i in soup.find_all(class_='js-schema-results schema-grid__center-column')]))

print(name_product)