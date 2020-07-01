print("Você Já Possui Cadastro? (S/N)")
resposta = input("")

resposta = resposta.lower()
if resposta == "nao" or resposta == "n" or resposta == "não":
    print("Qual Seu Nome?")
    nome = input("")

    print("Escolha Um Apelido")
    apelido = input("")

    print("Escolha Uma Senha")
    senha = input("")
else:
    print("Insira Seu Nome ou Apelido:")
    nome = input("")
    print("Insira Sua Senha:")
    senha = input("")
