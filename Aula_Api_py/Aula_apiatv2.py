import requests
import json

r = requests.get('http://apilivro.jogajuntoinstituto.org/books/')
data = r.json()
print(r.status_code)

for l in data:
    if l['description'] =='Squad Fénix':
        print(l)
