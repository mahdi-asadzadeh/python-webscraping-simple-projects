import requests


url = 'http://www.webscrapingfordatascience.com/authentication/'
r = requests.get(url, auth=('fddd', 'ddddd'))
print(r.text)
print(r.request.headers)