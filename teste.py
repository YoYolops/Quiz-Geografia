a = {'nome':'joao','apelido':'jojo'}
b = {'nome':'marcos','apelido':'marquin'}



#Para Gravar:
usuarios = [
dict(nome = jogador['nome'], apelido = jogador['apelido'], senha = jogador['senha'])
 for obj in usuarios
]

save_usuarios = {'usuarios': usuarios}
save_usuarios = json.dumps(save_usuarios, indent=4, sort_keys=False)
try:
    arquivo_json = open('dados_usuarios.json', 'w')
    arquivo_json.write(save_usuarios)
    arquivo_json.close()
except Exception as erro:
    print("Ocorreu um erro ao gravar arquivo.")
    print("O erro é: {}".format(erro))

#Usar loops para verificar a existencia de dados
