from random import randrange
import os

os.system('CLS')
tentativas = 1
sala = 1

while tentativas <= 7 and sala <= 7:
    print("Você está na sala: {}\nEscolha seu caminho".format(sala))
    print("[1] - Caminho Vermelho\n[2] - Caminho Preto")

    escolha = int(input())

    if escolha == 1:
        sala += 1
    elif escolha == 2:
        sala += 2
    else:
        ("Não existe esse caminho!")
    os.system('CLS')
    tentativas += 1


if tentativas >= 7:
    print("Você gastou todos seus recursos, não há mais saidas, você e seus companheiros morreram")
elif sala == 9:
    print("Você está na sala: {}\nVocê venceu!!".format(sala))
elif sala == 8:
    sala = input(randrange(1, 5))