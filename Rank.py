import json

def ler_json(): #Função de leitura de dados de rank json
    with open('rankdata.json', 'r', encoding = 'utf8') as f:
        return json.load(f)

ranqueamento = rankdata['ranqueamento']ler_json() #json bruto

ranqueamento = {'apelido': None, 'pontos': None, 'percentual': None}

#salvando pontos:
ranqueamento.insert(range(ranqueamento), {
    'apelido':apelido, 'pontos':pontos, 'percentual':percentual
})


if resposta == '4':
    #printar o rank
