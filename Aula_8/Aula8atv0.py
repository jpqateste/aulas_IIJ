import requests


def descobrir_bairro(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
  

    data = response.json()
    bairro = data['bairro']

    return bairro

squad ={
    "matheus": "40140620",
    "michelle": "40155250"
}

for nome, cep in squad.items():
   bairro = descobrir_bairro(cep)
   print(f"{nome} mora em {bairro}")

   