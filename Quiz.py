import json

def ler_json(): #Função de leitura de dados json
    with open('dados.json', 'r', encoding = 'utf8') as f:
        return json.load(f)
def ler_jsonrank(): #Função de leitura de dados de rank json
    with open('rankdata.json', 'r', encoding = 'utf8') as f:
        return json.load(f)

rankdata = ler_jsonrank() #json bruto rank
data = ler_json() #json bruto usuarios

ranqueamento = rankdata['ranqueamento']
usuarios = data['usuarios'] #uma lista com os dicionarios dos dados dos usuários
comp = len(usuarios)

quantperg = 0 #contador de quantidade de perguntas (Usado para calcular percentual de acerto)
pontos = 0 # Variável de armazenamento de pontuação individual
c = 0 #Contador de loop de verificação de apelido em cadastro
resposta = 0 #resposta do menu do usuário

print()
print('###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~## ')
print('#####~~~~~~~~~~~~~~~~~~~~~~~~~~~~#####')
print('#######~~~~~~~~~~~~~~~~~~~~~~~~#######')
print('##########~~~~~~~~~~~~~~~~~~##########')
print('###########~~~~~~~~~~~~~~~~~##########')
print('######################################')
print('######################################')
print('######################################')
print('########~~##################~~########')
print('########~~~~~#############~~~~########')
print('########~~~~~~~########~~~~~~~########')
print('########~~~~~~~########~~~~~~~########')
print('######################################')
print('######################################')
print('######################################')
print('###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##')
print('~~~##~~~~~~~~#############~~~~~~~###~~')
print('~~~##~~~~~~~~~~~~~~~~~~~~~~~~~~~~###~~')
print('~~~~~###~~~~~~~~~~~~~~~~~~~~~~###~~~~~')
print('~~~~~~~~#####~~~~~~~~~~~~#####~~~~~~~~')
print('~~~~~~~~~~~~~#############~~~~~~~~~~~~')
print('Desenvolvido por YoYo Produções \n Quizyo   v0.3 ALPHA')
print()

while resposta != '3':
    print('''    [ 1 ] Cadastrar-se
    [ 2 ] Entrar
    [ 3 ] Sair
    [ 4 ] Rank''')
    print()

    resposta = str(input("O que deseja fazer? "))
    if resposta == "1":
        print("Qual Seu Nome?")
        nome = input("")

        print("Escolha Um Apelido")
        temp = input("")
        while c < comp:
            for i in range(comp):
                if usuarios[i]['apelido'] == temp:
                    c = -1
                    print("Esse Apelido já Foi Escolhido. Insira outro")
                    temp = input("")
            c +=1
        apelido = temp

        print("Escolha Uma Senha")
        senha = input("")

        usuarios.insert(comp, {'nome':nome,'apelido':apelido,'senha':senha})
    elif resposta == "2":
        print("Insira Seu Apelido:")
        apelido = input("")
        print("Insira Sua Senha:")
        senha = input("")
        #Verificar se o apelido existe:
        binario = 0 # Fator de decisão de execuções de algumas linhas, 1: positivo/ 0: negativo
        for i in usuarios:
            if apelido in i.values() and senha in i.values():
                print('Bem Vindo(a)')
                binario = 1
        if binario != 1:
            print('Apelido ou senha incorretos.')

        elif binario == 1:
            print("Teste Seus Conhecimentos de América do Sul!!!")
            print("#########################################################################")


            print("1 - Quantos países soberanos existem na América do Sul? ")
            resp1 = input()
            quantperg += 1
            if resp1 == '12' or resp1 == "doze" or resp1 == 'Doze':
                pontos += 1
                print("Certo! Sua pontuação é: %d"%pontos)
            else: print("Errado, sua pontuação é: %d"%pontos)

            print("#########################################################################")
            print('2 - Qual o Maior País da América do Sul? ')
            resp2 = input("")
            resp2 = resp2.lower()
            quantperg += 1
            if resp2 == "brasil":
                pontos += 1
                print("Parabéns, sua pontuação é: %d"%pontos)
            else: print("Errado! sua pontuação é: %d"%pontos)

            print("#########################################################################")
            print("3 - Qual o Primeiro País da América do Sul a Legalizar a Maconha?")
            resp3 = input("")
            resp3 = resp3.lower()
            quantperg += 1
            if resp3 == "uruguai":
                pontos += 1
                print("Certíssimo! Sua Pontuação é %d"%pontos)
            else: print("Você errou, sua pontuação atual é: %d"%pontos)

            print("#########################################################################")
            print("4 - Qual o País Europeu que Possui Território no Continente Sulamericano?")
            resp4 = input("")
            resp4 = resp4.lower()
            quantperg += 1
            if resp4 == "frança":
                pontos += 1
                print("Muito bem! Sua pontuação é: %d"%pontos)
            else: print("É uma pena, mas você errou, sua pontuação é: %d"%pontos)

            print("#########################################################################")
            print("5 - Diga o Nome do Único País da América do Sul que Começa com S")
            resp5 = input("")
            resp5 = resp5.lower()
            quantperg += 1
            if resp5 == "suriname":
                pontos += 1
                print("Correto!")
            else: print("Infelizmente, você errou.")

            print("#########################################################################")
            print("6 - Qual o primeiro país da América do Sul a eleger uma pesidente mulher?")
            resp6 = input("")
            resp6 = resp6.lower()
            quantperg += 1
            if resp6 == "argentina":
                pontos += 1
                print("Correto!")
            else: print("Você errou.")

            print("#########################################################################")
            print("7 - Qual foi o primeiro presidente do Brasil?")
            resp7 = input("")
            resp7 = resp7.lower()
            quantperg += 1
            if resp7 == "marechal deodoro da fonseca" or resp7 == "deodoro da fonseca":
                pontos += 1
                print("Certo")
            else: print("Errado.")

            print("#########################################################################")
            print("8 - Quem foi o primeiro(a) programador(a) da história?")
            resp8 = input("")
            resp8 = resp8.lower()
            quantperg += 1
            if resp8 == "ada lovelace" or resp8 == "ada":
                pontos += 1
                print("Certo")
            else: print("Errado.")

            print("#########################################################################")
            percentual = (100 * pontos)/quantperg
            print('Você acertou %d, tendo %d por cento de acerto'%(pontos, percentual))
            print()

            binario = 0 # Fator de decisão de execuções de algumas linhas, 1: positivo/ 0: negativo
            for i in ranqueamento:
                if i['apelido'] == apelido:
                    i['pontos'] = pontos
                    i['percentual'] = percentual
                    binario = 1
            if binario != 1:
                ranqueamento.insert(len(ranqueamento), { #inserção dos dados de pontuação no rankdata
                    'apelido':apelido, 'pontos':pontos, 'percentual':percentual
                })

    #Para Gravar os dados coletados:
save_usuarios = {'usuarios': usuarios}
save_usuarios = json.dumps(save_usuarios, indent=4, sort_keys=False)
try:
    arquivo_json = open('dados.json', 'w')
    arquivo_json.write(save_usuarios)
    arquivo_json.close()
except Exception as erro:
    print("Ocorreu um erro ao gravar arquivo.")
    print("O erro é: {}".format(erro))


save_ranqueamento = {'ranqueamento': ranqueamento}
save_ranqueamento = json.dumps(save_ranqueamento, indent=4, sort_keys=False)
try:
    arquivo_json = open('rankdata.json', 'w')
    arquivo_json.write(save_ranqueamento)
    arquivo_json.close()
except Exception as erro:
    print("Ocorreu um erro ao gravar arquivo.")
    print("O erro é: {}".format(erro))


    #Usar loops para verificar a existencia de dados
