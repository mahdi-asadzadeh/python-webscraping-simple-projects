import requests


url = 'http://www.webscrapingfordatascience.com/paramhttp/?query=test'
r = requests.get(url)
print(r.text)
print(r.status_code)
print(r.reason)
print(r.headers)
print(r.url)