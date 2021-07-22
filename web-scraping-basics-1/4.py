import requests
from urllib.parse import unquote


class NonEncodedSession(requests.Session):
    def send(self, *args, **kwargs):
        args[0].url = unquote(args[0].url)
        return requests.Session.send(self, *args, **kwargs)


my_requests = NonEncodedSession()
url = 'http://www.example.com/?spaces |pipe'
r = my_requests.get(url)
print(r.url)
print(r.status_code)
