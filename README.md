# ConsumindoAPI
🗝️Passo a passo de como consumir api e dados de um JSON de diversas formas.


🩸![image](https://github.com/user-attachments/assets/e502b7de-eebd-41f2-91a6-bb95c089d3bb)

🩸![image](https://github.com/user-attachments/assets/3a4f8089-b1b8-4943-bb7e-9da8eeadef39)

🩸![image](https://github.com/user-attachments/assets/3af8ca90-1da3-450b-86f1-a9cd211b4b35)

🩸Arquivo (TemplatePadraoGET0): Template padrão de consumo de api método GET sem passar parâmetro e sem usar early return.

🩸Arquivo (TemplatePadraoGET1): Template padrão de consumo de api método GET sem passar parâmetro e com early return.

🩸Arquivo (TemplatePadraoGET2): Template padrão de consumo de api método GET sem passar parâmetro e com early return e tratamento de excessões para
    o consumo de api (url e formato JSON).

🩸Arquivo (TemplatePadraoGET3): Template padrão de consumo de api método GET com parâmetro passado e com early return e trabamento de excessões para
    o comsumo de api(url e formato JSON), a minha variavel "data" recebe o valor do GET pois o meu "response = requests.get(url)" está dentro da minha função
    "fetch_data_from_api".

🩸Arquivo (TemplatePadraoGET3.1_revisado):Template padrão de consumo de api método GET com parÂmetro passado e com early return nas duas funções usadas                     "fetch_data_from_api" e "process_api_data" otimizando ainda mais e deixando mais legivel que o arquivo anterior, padronizando comentarios e retirando                 comentários redundantes.

🩸Arquivo (ConsumindoAPIGithub): Template padrão de consumo de api método GET com parâmetro passado e com early return apenas com tratamento do 200.

# Referências Bibliográficas

🗺 https://medium.com/@danilossdev/melhore-a-legibilidade-e-a-manutenibilidade-do-seu-c%C3%B3digo-com-a-pr%C3%A1tica-do-early-return-ead87e298d17#:~:text=A%20ideia%20do%20%E2%80%9Cearly%20return,antecipadamente%20a%20execu%C3%A7%C3%A3o%20do%20programa.&text=Se%20pensarmos%20no%20caminho%20feliz,mas%20avaliando%20os%20caminhos%20alternativos.
🗺️https://pauloreal.medium.com/saiba-o-porque-voce-deveria-evitar-o-else-no-seu-codigo-792c8abc5683
🗺️https://osantana.me/dicas-para-um-bom-programa-em-python/
