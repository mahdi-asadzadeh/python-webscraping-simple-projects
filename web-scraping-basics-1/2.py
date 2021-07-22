import requests
from urllib.parse import quote, quote_plus


raw_string = 'a query with /, spaces and?&'
print(quote(raw_string))
print(quote_plus(raw_string))
