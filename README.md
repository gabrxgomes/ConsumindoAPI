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
