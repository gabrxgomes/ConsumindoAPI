import requests

url = 'https://api.nasa.gov/planetary/apod?api_key=J3QlMqNxK84jeDNWX0UJJhEjJJCBJlU5bSobtp5n'
#O padrão tem que ser igual ao mostrado a cima.


#VAMOS SEMPRE LEMBRAR QUE PRECISAMOS DE UMA API_KEY PARA ACESSAR QUALQUER TIPO DE ENDPOINT
#ISSO É FUNDAMENTAL E INDISPENSAVEL!
response = requests.get(url)


if response.status_code == 200:
    data = response.json()

    print(data)

else:
    print(f'Erro ao acessar a API: {response.status_code}')