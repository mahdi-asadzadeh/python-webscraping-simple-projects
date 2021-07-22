import requests


url = 'http://www.webscrapingfordatascience.com/postform2/'


formdata = {
    'name': 'Seppe',
    'gender': 'M',
    'pizza': 'like',
    'haircolor': 'brown',
    'comments': '',
    'protection': '2c17abf5d5b4e326bea802600ff88405'
}

r = requests.post(url, formdata)
print(r.text)
