print("Teste Seus Conhecimentos de América do Sul!!!")
print("Desenvolvido por YoYo Produções \n Versão 0.1 ALPHA")
print("#########################################################################")


pontos = 0


print("1 - Quantos países soberanos existem na América do Sul? ")
resp1 = int(input())
if resp1 == 12 or resp1 == "doze" or resp1 == Doze:
    pontos += 1
    print("Certo! Sua pontuação é: %d"%pontos)
else: print("Errado, sua pontuação é: %d"%pontos)

print("2 - Qual o Maior País da América do Sul? ")
resp2 = input("")
resp2 = resp2.lower()
if resp2 == "brasil":
    pontos += 1
    print("Parabéns, sua pontuação é: %d"%pontos)
else: print("Errado! sua pontuação é: %d"%pontos)

print("3 - Qual o Primeiro País da América do Sul a Legalizar a Maconha?")
resp3 = input("")
resp3 = resp3.lower()
if resp3 == "uruguai":
    pontos += 1
    print("Certíssimo! Sua Pontuação é %d"%pontos)
else: print("Você errou, sua pontuação atual é: %d"%pontos)

print("4 - Qual o País Europeu que Possui Território no Continente Sulamericano?")
resp4 = input("")
resp4 = resp4.lower()
if resp4 == "frança":
    pontos += 1
    print("Muito bem! Sua pontuação é: %d"%pontos)
else: print("É uma pena, mas você errou, sua pontuação é: %d"%pontos)

print("5 - Diga o Nome do Único País da América do Sul que Começa com S")
resp5 = input("")
resp5 = resp5.lower()
if resp5 == "suriname":
    pontos += 1
    print("Correto!")
else: print("Infelizmente, você errou.")

percentual = pontos * 20
print("Você fez %d pontos de 5, tendo %d por cento de acerto"%(pontos, percentual))
