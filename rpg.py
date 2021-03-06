from random import randrange
import os

os.system('CLS')
tentativas = 0
sala = 1
vidas = 8
CAMINHO_VERMELHO = 1
CAMINHO_PRETO = 2

def narrador(sala):       
    print("Você tem {} vidas restantes".format(vidas))
    print("Você está na sala: {}\nEscolha seu caminho".format(sala)) 
    print("[1] - Caminho Vermelho\n[2] - Caminho Preto")

def mensagemDerrota():
    print("Você gastou todos seus recursos, não há mais saidas, você e seus companheiros morreram")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def mensagemVitoria():
    print("Você está na sala: {}\nVocê venceu!!".format(sala))
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

while (tentativas <= 7 and sala != 9):
    tentativas += 1
    vidas -=1
    narrador(sala)

    escolha = int(input())

    if ((escolha == CAMINHO_VERMELHO and sala != 6) or (escolha == CAMINHO_PRETO and sala != 8)):
        sala += escolha
        os.system('CLS')
    elif sala == 8:
        sala = randrange(1, 6)
        os.system('CLS')
    else:
        print("\nNão existe esse caminho!\n\n")

if tentativas > 7:
    mensagemDerrota()
else:
    mensagemVitoria()
