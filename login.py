import json

def ler_json():
    with open('dados.json', 'r', encoding = 'utf8') as f:
        return json.load(f)

data = ler_json()

usuarios = data['usuarios']
comp = len(usuarios)

resposta = 0
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
        for i in range(comp):
            if usuarios[i]['apelido'] == temp:
                temp = None
                print("Esse Apelido já Foi Escolhido")
        apelido = temp

        print("Escolha Uma Senha")
        senha = input("")

        usuarios.insert(comp, {'nome':nome,'apelido':apelido,'senha':senha})
    elif resposta == "2":
        print("Insira Seu Apelido:")
        apelido = input("")
        print("Insira Sua Senha:")
        senha = input("")

    #Para Gravar:
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
