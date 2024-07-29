import requests

print('Github Users')

username = input('Qual é o nome do usuário ?')

url = f'https://api.github.com/users/{username}'

response = requests.get(url)


def process_api_response(response):
    if response.status_code != 200:
        return f'Erro ao acessar a API: {response.status_code}'

data = response.json()

#Imprime o json completo
#print(data)

#me dá o retorno em parametros
print(f'Nome Completo: {data["name"]}')
print(f'Localização: {data["location"]}')
print(f'Foto: {data["avatar_url"]}')
