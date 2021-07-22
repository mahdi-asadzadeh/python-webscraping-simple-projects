import requests


url = 'http://www.webscrapingfordatascience.com/jsonajax/results.php'
r = requests.post(url, data={'api_code': 'C123456'})

print(r.json())
print(r.json().get('results'))
