class Loteria:

    def __init__(self, concurso, dezenas = []):
        self.concurso = concurso
        self.dezenas = dezenas

    def mostra_concurso(self):
        print(f'concurso:{self.concurso} dezenas{self.dezenas}')

    def verifica_concurso(self, dezenas_jogadas):
        dezenas_apuradas = self.dezenas
        acertos = 0
        for dezena_apurada in dezenas_apuradas:
            for dezena_jogada in dezenas_jogadas:
                if dezena_jogada == dezena_apurada:
                    acertos +=1
        print(f'O número de acertos no concurso:{self.concurso} foi de {acertos}')


conc2830 = Loteria(2830, [2,3,4,8,9,10,11,12,13,17,18,20,21,22,25])
conc2831 = Loteria(2831, [2,3,5,7,10,11,13,14,15,16,17,19,20,22,25])
conc2832 = Loteria(2832, [1,2,3,5,6,11,14,15,16,19,20,21,22,23,24])
conc2833 = Loteria(2833, [2,3,4,5,6,11,13,14,16,18,19,22,23,24,25])
conc2834 = Loteria(2834, [1,6,8,10,11,12,13,14,17,19,20,21,22,23,25])
conc2835 = Loteria(2835, [2,4,6,7,8,9,10,12,13,14,15,16,21,22,25])
conc2836 = Loteria(2836, [1,2,3,4,7,9,12,14,15,17,18,20,21,22,23])
conc2837 = Loteria(2837, [1,2,5,6,8,10,12,17,18,19,20,21,22,24,25])

dezenas_jogadas = [1,3,5,7,8,9,10,11,13,14,18,20,21,22,24,25]

conc2830.verifica_concurso(dezenas_jogadas)
conc2831.verifica_concurso(dezenas_jogadas)
conc2832.verifica_concurso(dezenas_jogadas)
conc2833.verifica_concurso(dezenas_jogadas)
conc2834.verifica_concurso(dezenas_jogadas)
conc2835.verifica_concurso(dezenas_jogadas)
conc2836.verifica_concurso(dezenas_jogadas)
conc2837.verifica_concurso(dezenas_jogadas)
