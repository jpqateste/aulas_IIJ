import requests


response = requests.get('https://viacep.com.br/ws/60335000/json/')
data = response.json()

print(data['localidade'])
