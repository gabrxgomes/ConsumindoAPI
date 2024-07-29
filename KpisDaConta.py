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

#🩸 Imprime o json completo
print(data)

# KPIs do usuário
"""
    🩸Todos esses dados estão presentes como parâmetros 
    🩸no link "https://api.github.com/users/gabrxgomes"

"""
kpis = {
    'Nome Completo': data.get('name'),
    'Localização': data.get('location'),
    'Foto': data.get('avatar_url'),
    'Total de Repositórios Públicos': data.get('public_repos'),
    'Total de Seguidores': data.get('followers'),
    'Total de Seguindo': data.get('following'),
    'Número de Gists Públicos': data.get('public_gists'),
    'Data de Criação da Conta': data.get('created_at'),
    'Data da Última Atualização': data.get('updated_at')
}

#🩸 Imprime os KPIs
print('\nKPIs do Usuário:')
for key, value in kpis.items():
    print(f'{key}: {value}')
