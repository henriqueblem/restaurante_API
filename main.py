from fastapi import FastAPI, Query
import requests

'''Para rodar o arquivo no terminal execute o seguinte comando: uvicorn main:app --reload'''

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    É importante seguir as tradições e boas práticas.
    '''
    return {'Hello':'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):

    '''
    Endpoint para visualização dos cardapios dos restaurantes
    
    '''

    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()

        if restaurante is None:
            return {'Dados:':dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                '''...Método que adiciona os ítens ao dicionário de seu respectivo restaurante'''
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante:':restaurante, 'Cardapio':dados_restaurante}

    else:
        return {'Erro:': f'{response.status_code} - {response.text}'}