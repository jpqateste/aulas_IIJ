import requests
import json

books = [
         {'title': 'Nineteem Eighty-Four', 
           'description': 'Squad Fénix', 
           'author': 1, 
           'gender': 3},
        {'title': 'Anne of the Island', 
           'description': 'Squad Fénix', 
           'author': 19, 
           'gender': 3},
        {'title': 'Anne of Avonlea', 
           'description': 'Squad Fénix', 
           'author': 19, 
           'gender': 3},
        {'title': 'Anne of Green Gables', 
           'description': 'Squad Fénix', 
           'author': 19, 
           'gender': 3}
]

def criarLivros():
    for b in books:

        r = requests.post("http://apilivro.jogajuntoinstituto.org/books/", data=b)
        print(r.status_code)

criarLivros()



