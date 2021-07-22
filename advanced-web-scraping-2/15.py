import requests


url = 'http://www.webscrapingfordatascience.com/redirect/'
r = requests.get(url, allow_redirects=False)
print(r.text)
print(r.headers)

