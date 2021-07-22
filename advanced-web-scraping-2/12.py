import requests


url = 'http://www.webscrapingfordatascience.com/postform2/'
formdata = {'name': 'Seppe'}
filedata = {'profile_picture': open('1.jpg', 'rb')}
r = requests.post(url, data=formdata, files=filedata)
print(r.text)

