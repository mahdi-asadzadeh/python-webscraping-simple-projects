import requests


url = 'http://www.webscrapingfordatascience.com/referercheck/secret.php'
my_headers = {
  'Referer': 'http://www.webscrapingfordatascience.com/referercheck/'
}
r = requests.get(url, headers=my_headers)
print(r.text)
print(r.headers)
print(r.request.headers)