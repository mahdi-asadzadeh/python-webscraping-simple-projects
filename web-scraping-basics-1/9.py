import re
import requests
from bs4 import BeautifulSoup


url = 'http://www.webscrapingfordatascience.com/paramhttp/?query=test'
r = requests.get(url)
html_context = r.text
html_soup = BeautifulSoup(html_context, 'html.parser')


r = html_soup.find(re.compile('^h'))
print(r)
