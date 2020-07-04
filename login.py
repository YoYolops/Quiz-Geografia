import json

def ler_json(): #Função de leitura de dados json
    with open('dados.json', 'r', encoding = 'utf8') as f:
        return json.load(f)

data = ler_json() #json bruto

usuarios = data['usuarios'] #uma lista com os dicionarios dos dados dos usuários
comp = len(usuarios)

binario = 0
c = 0 #Contador de loop de verificação de apelido em cadastro
resposta = 0 #resposta do menu do usuário
while resposta != '3':
    print('''    [ 1 ] Cadastrar-se
    [ 2 ] Entrar
    [ 3 ] Sair''')

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
        for i in usuarios:
            if apelido in i.values() and senha in i.values():
                print('Bem Vindo(a)')
                binario = 1
        if binario != 1:
            print('Apelido ou senha incorretos.')

        elif binario == 1:
            


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

    #Usar loops para verificar a existencia de dados
