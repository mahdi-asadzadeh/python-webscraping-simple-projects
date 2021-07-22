import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/w/index.php' + \
      '?title=List_of_Game_of_Thrones_episodes&oldid=802553687'
r = requests.get(url)
html_context = r.text 
html_soup = BeautifulSoup(html_context, 'html.parser')

"""
      find(name, attrs, recursive, string, **keywords)
      find_all(name, attrs, recursive, string, limit, **keywords)
"""

print(html_soup.find('h1'))
print(html_soup.find('', {'id': 'p-logo'}))
for found in html_soup.find_all(['h1', 'h2']):
      print(found)
      