import requests
from urllib.parse import quote, quote_plus


url = 'http://www.webscrapingfordatascience.com/paramhttp/?query='

parameters = {
    'query':  'a query with /, spaces and?&'
}

r = requests.get(url , params=parameters)

print(r.text)
print(r.url)
