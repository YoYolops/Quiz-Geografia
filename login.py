import json
jogador = {"nome":None,
            "apelido":None,
            "senha":None,
            "pontos":None,
            "acerto":None,
}
usuarios = []
comp = len(usuarios)

print("Você Já Possui Cadastro? (S/N)")
resposta = input("")
resposta = resposta.lower()
if resposta == "nao" or resposta == "n" or resposta == "não":
    print("Qual Seu Nome?")
    jogador["nome"] = input("")

    print("Escolha Um Apelido")
    temp = input("")
    for i in range(comp):
        if usuarios[i]['apelido'] == temp:
            print("Esse Apelido já Foi Escolhido")
        else:
            jogador["apelido"] = temp
    print("Escolha Uma Senha")
    jogador["senha"] = input("")

else:
    print("Insira Seu Nome ou Apelido:")
    nome = input("")
    print("Insira Sua Senha:")
    senha = input("")

usuarios.append(jogador)
#Para Gravar:
save_usuarios = {'usuarios': usuarios}
save_usuarios = json.dumps(save_usuarios, indent=4, sort_keys=False)
try:
    arquivo_json = open('dados_usuarios', 'w')
    arquivo_json.write(save_usuarios)
    arquivo_json.close()
except Exception as erro:
    print("Ocorreu um erro ao gravar arquivo.")
    print("O erro é: {}".format(erro))

#Usar loops para verificar a existencia de dados
