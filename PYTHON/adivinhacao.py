import random

def jogar():
    print("*********************************************")
    print("***** Bem vindo ao jogo de adivinhação! *****")
    print("*********************************************")

    numero_secreto = round(random.randrange(1, 11))
    total_de_tentativas = 0
    nivel = 4
    pontos = 10
    # rodada = 1 #código do while

    print('qual nível de dificuldade?')
    print('(1) Fácil, (2) Médio ou (3) Difícil')
    nivel = int(input('Defina o nível: '))

    if (nivel == 1):
        total_de_tentativas = 5
    elif (nivel == 2):
        total_de_tentativas = 3
    elif (nivel == 3):
        total_de_tentativas = 1
    else:
        while nivel > 3:
            print('Você deve digitar um número entre 1 a 3 para escolher o nível.')
            nivel = int(input('Defina o nível: '))
            if (nivel == 1):
                total_de_tentativas = 5
            elif (nivel == 2):
                total_de_tentativas = 3
            elif (nivel == 3):
                total_de_tentativas = 1

    # while rodada <= total_de_tentativas:
    for rodada in range(1,  total_de_tentativas + 1):

        print("tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 10: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 10:
            print("Você deve digitar um número entre 1 e 10")
            continue

        acertou = (chute == numero_secreto)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou, seu chute foi maior que o número secreto")
            elif (menor):
                print("Você errou, seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            print(pontos_perdidos)
            pontos = pontos - pontos_perdidos
        # rodada += 1 #código do while

    print("Fim do jogo.")

if(__name__ == '__main__'):
    jogar()
