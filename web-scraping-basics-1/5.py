import requests


def calc(a, b, op):
    url = 'http://www.webscrapingfordatascience.com/calchttp/'
    params = {'a': a, 'b': b, 'op': op}
    r = requests.get(url, params=params)
    return r.text


print(calc(4, 6, '*'))
print(calc(4, 6, '/'))
