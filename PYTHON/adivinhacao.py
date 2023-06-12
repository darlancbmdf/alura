import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = round(random.randrange(1, 11))
total_de_tentativas = 3
#rodada = 1 #código do while

#while rodada <= total_de_tentativas:
for rodada in range(1,  total_de_tentativas + 1):
    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 10: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 10):
        print("Você deve digitar um número entre 1 e 10")
        continue

    acertou = (chute == numero_secreto)
    maior = (chute > numero_secreto)
    menor = (chute < numero_secreto)

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou, seu chute foi maior que o número secreto")
        elif (menor):
            print("Você errou, seu chute foi menor que o número secreto")
    #rodada += 1 #código do while

print("Fim do jogo.")
