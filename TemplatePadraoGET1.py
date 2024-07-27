import requests

url = 'https://api.nasa.gov/planetary/apod?api_key=J3QlMqNxK84jeDNWX0UJJhEjJJCBJlU5bSobtp5n'

response = requests.get(url)
def process_api_response(response): # Usando o early return
    if response.status_code != 200: # Usando o early return

        return f'Erro ao acessar a API: {response.status_code}' # Usando o early return

data = response.json()

print(data)

