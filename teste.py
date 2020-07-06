import json

def ler_jsonrank(): #Função de leitura de dados de rank json
    with open('rankdata.json', 'r', encoding = 'utf8') as f:
        return json.load(f)

rankdata = ler_jsonrank() #json bruto
ranqueamento = rankdata['ranqueamento']

print(rankdata)
print(ranqueamento)
