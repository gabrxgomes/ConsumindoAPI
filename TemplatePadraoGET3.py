import requests


#url = 'xhttps://api.nasa.gov/planetary/apod?api_key=J3QlMqNxK84jeDNWX0UJJhEjJJCBJlU5bSobtp5n'


def fetch_data_from_api(url):
    #Validando a URL

    if not url.startswith('http'):
        print('Invalid URL.')
        return f'A sua URL é inválida, por favor revise a mesma e tente novamente.'

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f'Erro da requisição: {response.status_code}')
            return None

        #Validando seu meu código é um JSON
        if 'application/json' not in response.headers.get('Content-Type', ''):
            print(f'O Conteúdo não é um JSON')
            return None

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição: {e}')
        return None


# Finalmente passando a URL diferente dos outros meios de requesição

# URL CORRETA ABAIXO
url = 'https://api.nasa.gov/planetary/apod?api_key=J3QlMqNxK84jeDNWX0UJJhEjJJCBJlU5bSobtp5n'

# URL ERRADA PARA TESTAR EXCESSÃO
#url = 'xhttps://api.nasa.gov/planetary/apod?api_key=J3QlMqNxK84jeDNWX0UJJhEjJJCBJlU5bSobtp5n'

# iNCREMENTANDO NA VARIAVEL DATA O VALOR DO RESPONSE QUE USAMOS COM O METODO GET NA FUNÇÃO "fetch_data_from_api"
data = fetch_data_from_api(url)

dataValue = data.get('date')

copyrightValue = data.get('copyright')

explanationValue = data.get('explanation')

print(dataValue, copyrightValue, explanationValue)
