import requests
import json

'''Acessando e importando os dados da API'''
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    print(response.status_code)
    dados_json = response.json()
    dados_restaurante = {}

    '''Método para percorrer os dados, separando-os por restaurante...'''
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []

        '''...Método que adiciona os ítens ao dicionário de seu respectivo restaurante'''
        dados_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

else:
    print(f'Um erro "{response.status_code}" foi encontrado')

'''Método para criação dos arquivos .json: Pega os ítens filtrados por restaurante, armazena ao cardápio(biblioteca) do restaurante a que pertence.'''
for nome_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)