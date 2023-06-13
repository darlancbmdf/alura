def jogar():
    print("************************************")
    print("***** Bem vindo ao jogo Forca! *****")
    print("************************************")

    palavra_secreta = 'bombeiros'

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):

        chute = input('Qual letra?')
        chute = chute.strip() # a função .strip() retira os espaços no início e no final

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print('Encontrei a letra {} na posicao {}'.format(letra, index))
            index += 1

        print('jogando...')

    print("Fim do jogo.")


if (__name__ == '__main__'):
    jogar()
