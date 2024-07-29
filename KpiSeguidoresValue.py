import requests
import pandas as pd
import matplotlib.pyplot as plt

print('Github Users')

username = input('Qual é o nome do usuário? ')

url = f'https://api.github.com/users/{username}'

response = requests.get(url)

def process_api_response(response):
    if response.status_code != 200:
        print(f'Erro ao acessar a API: {response.status_code}')
        return None
    return response.json()

data = process_api_response(response)

if data:
    # Imprime o json completo
    print(data)

    # KPIs do usuário
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

    # Imprime os KPIs
    print('\nKPIs do Usuário:')
    for key, value in kpis.items():
        print(f'{key}: {value}')

    # Acessa o URL de quem o usuário está seguindo
    following_url = f'https://api.github.com/users/{username}/following'
    following_response = requests.get(following_url)
    following_data = process_api_response(following_response)

    if following_data:
        # Coletar o número de repositórios públicos de cada conta seguida
        following_repos = []
        for following in following_data:
            following_username = following['login']
            following_url = f'https://api.github.com/users/{following_username}'
            following_response = requests.get(following_url)
            following_info = process_api_response(following_response)
            if following_info:
                following_repos.append({
                    'Username': following_username,
                    'Public Repos': following_info['public_repos']
                })

        # Criar um DataFrame com os dados
        df = pd.DataFrame(following_repos)

        # Identificar o usuário com mais repositórios públicos
        max_repos_user = df.loc[df['Public Repos'].idxmax()]

        # Comparar com o número de repositórios públicos do usuário atual
        user_repos = data['public_repos']
        print(f"\nUsuário com mais repositórios públicos:")
        print(f"Username: {max_repos_user['Username']}")
        print(f"Repositórios Públicos: {max_repos_user['Public Repos']}")

        print(f"\nSeu número de repositórios públicos: {user_repos}")

        # Plotar os dados
        plt.figure(figsize=(10, 5))
        plt.bar(df['Username'], df['Public Repos'], color='skyblue', label='Seguindo')
        plt.bar(username, user_repos, color='orange', label='Você')
        plt.xlabel('Usuários Seguidos')
        plt.ylabel('Número de Repositórios Públicos')
        plt.title('Comparação de Repositórios Públicos')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()
    else:
        print(f'{username} não está seguindo ninguém.')
else:
    print('Erro ao processar os dados do usuário.')
