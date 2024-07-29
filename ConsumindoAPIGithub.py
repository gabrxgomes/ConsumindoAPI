import requests

print('Github Users')

username = input('Qual é o nome do usuário? ')

url = f'https://api.github.com/users/{username}'

response = requests.get(url)

def process_api_response(response):
    if response.status_code != 200:
        return f'Erro ao acessar a API: {response.status_code}'
    return response.json()

data = process_api_response(response)

# Imprime o json completo
print(data)

# Imprime o retorno em parâmetros
print(f'Nome Completo: {data["name"]}')
print(f'Localização: {data["location"]}')
print(f'Foto: {data["avatar_url"]}')

# Acessa o URL de seguidores
followers_url = data["followers_url"]

# Faz uma nova solicitação HTTP para a URL de seguidores
followers_response = requests.get(followers_url)
followers_data = process_api_response(followers_response)

# Verifica se há seguidores
if followers_data:
    print(f'\nSeguidores de {username}:')
    for follower in followers_data:
        print(f'Nome de usuário: {follower["login"]}')
        print(f'Foto: {follower["avatar_url"]}\n')
else:
    print(f'{username} não tem seguidores.')
