import requests
from bs4 import BeautifulSoup


url = 'http://www.webscrapingfordatascience.com/postform3/'
r = requests.get(url)
html_soup = BeautifulSoup(r.text, 'html.parser')
p_val = html_soup.find('input', attrs={'name': 'protection'}).get('value')


formdata = {
    'name': 'Seppe',
    'gender': 'M',
    'pizza': 'like',
    'haircolor': 'brown',
    'comments': '',
    'protection': p_val,
}

r = requests.post(url, data=formdata)
print(r.text)
