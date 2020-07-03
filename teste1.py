resposta = 0
usuarios = []

comp = len(usuarios)


while resposta != 1:
    resposta = str(input('parar 1: '))
    print("Qual Seu Nome?")
    nome = input("")

    print("Escolha Um Apelido")
    temp = input("")
    apelido = temp

    print("Escolha Uma Senha")
    senha = input("")

    usuarios.insert(comp, {'nome':nome,'apelido':apelido,'senha':senha})

    print(usuarios)
