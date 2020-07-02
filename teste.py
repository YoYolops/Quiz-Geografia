jogador = {"nome":None,
            "apelido":None,
            "senha":None,
            "pontos":None,
            "acerto":None,
}
usuarios = []

print("Você Já Possui Cadastro? (S/N)")
resposta = input("")
resposta = resposta.lower()
if resposta == "nao" or resposta == "n" or resposta == "não":
    print("Qual Seu Nome?")
    jogador["nome"] = input("")

    print("Escolha Um Apelido")
    jogador["apelido"] = input("")

    print("Escolha Uma Senha")
    jogador["senha"] = input("")
    usuarios.append(jogador)
