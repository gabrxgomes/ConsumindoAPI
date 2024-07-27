import requests


def fetch_data_from_api(url):
    """
    Faz uma requisição GET para a URL especificada e retorna os dados em formato JSON.

    Args:
        url (str): A URL da API.

    Returns:
        dict: Os dados retornados pela API em formato JSON.
        str: Mensagem de erro em caso de URL inválida.
        None: Em caso de erro na requisição ou se o conteúdo não for JSON.
    """

    # Validando a URL
    if not url.startswith('http'):
        print('URL inválida.')
        return 'A sua URL é inválida, por favor revise a mesma e tente novamente.'

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f'Erro da requisição: {response.status_code}')
            return None

        # Validando se o conteúdo é JSON
        if 'application/json' not in response.headers.get('Content-Type', ''):
            print('O conteúdo não é um JSON.')
            return None

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição: {e}')
        return None


def process_api_data(url):
    """
    Faz a requisição para a API e processa os dados retornados.

    Args:
        url (str): A URL da API.
    """
    data = fetch_data_from_api(url)

    if data is None:
        print('Erro ao obter dados da API.')
        return

    date = data.get('date')
    copyright_info = data.get('copyright')
    explanation = data.get('explanation')
    hdurl = data.get('hdurl')

    print(date, copyright_info, explanation, hdurl)


# URL correta
url = 'https://api.nasa.gov/planetary/apod?api_key=J3QlMqNxK84jeDNWX0UJJhEjJJCBJlU5bSobtp5n'

# URL errada para testar exceção
# url = 'xhttps://api.nasa.gov/planetary/apod?api_key=J3QlMqNxK84jeDNWX0UJJhEjJJCBJlU5bSobtp5n'

# Chamando a função para processar os dados da API
process_api_data(url)
