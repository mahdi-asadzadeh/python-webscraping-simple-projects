import requests


url = 'http://www.webscrapingfordatascience.com/trickylogin/'
my_session = requests.Session()
r = my_session.post(url)
r = my_session.post(url, params={'p': 'login'},
    data={'username': 'dummy', 'password': '1234'})
r = my_session.get(url, params={'p': 'protected'})
print(r.text)