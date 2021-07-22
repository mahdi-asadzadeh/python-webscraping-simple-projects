import requests


url = 'http://www.webscrapingfordatascience.com/usercheck/'

my_headers = {
    'User-Agent': 'Linux/20.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36' + \
    '(KHTML, like Gecko) Chrome/61.0.3163.100'
}
r = requests.get(url, headers=my_headers)
print(r.text)
print(r.request.headers)
