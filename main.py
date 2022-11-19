import urllib.request
opener = urllib.request.build_opener()
response = opener.open('https://wikipedia.org/')
print(response.read())

import requests
response = requests.qet('https://wikipedia.org/')
print(response.content)
print(f"Datatype - {type(response.text)}")
