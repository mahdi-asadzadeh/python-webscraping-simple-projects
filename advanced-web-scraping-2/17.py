import requests


url = 'http://www.webscrapingfordatascience.com/cookielogin/'
r = requests.post(url, data={'username': 'dummy', 'password': '1234'})
my_cookies = r.cookies
r = requests.get(url + 'secret.php', cookies=my_cookies)

print(r.text)