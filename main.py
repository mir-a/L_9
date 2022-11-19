import urllib.request
opener = urllib.request.build_opener()
response = opener.open('https://wikipedia.org/')
print(response.read())

import requests
response = requests.qet('https://wikipedia.org/')
print(response.text)
print(f"Datatype - {type(response.text)}")

response = requests.post('https://httpbin.org/post', data='Test', heders = {'h1': 'TITLE'})
print(response.text)
print(f"Datatype - {type(response.text)}")

