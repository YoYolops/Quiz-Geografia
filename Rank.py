import json

def ler_jsonrank(): #Função de leitura de dados de rank json
    with open('rankdata.json', 'r', encoding = 'utf8') as f:
        return json.load(f)

rankdata = ler_jsonrank() #json bruto
ranqueamento = rankdata['ranqueamento']


#salvando pontos:

ranqueamento.insert(range(ranqueamento), {
    'apelido':apelido, 'pontos':pontos, 'percentual':percentual
})


save_ranqueamento = {'usuarios': ranqueamento}
save_ranqueamento = json.dumps(save_ranqueamento, indent=4, sort_keys=False)
try:
    arquivo_json = open('rankdata.json', 'w')
    arquivo_json.write(save_ranqueamento)
    arquivo_json.close()
except Exception as erro:
    print("Ocorreu um erro ao gravar arquivo.")
    print("O erro é: {}".format(erro))
