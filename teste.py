
import json

def ler_json(): #Função de leitura de dados json
    with open('dados.json', 'r', encoding = 'utf8') as f:
        return json.load(f)

data = ler_json()
usuarios = data['usuarios']

for i in usuarios:
    if
