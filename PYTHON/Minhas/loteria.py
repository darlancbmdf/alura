class Loteria:

    def __init__(self, nome, concurso, dezenas):
        self.concurso = concurso
        self.dezenas = dezenas
        self.nome = nome

    def mostra_concurso(self):
        print(f'concurso:{self.concurso} dezenas:{self.dezenas}')

    def verifica_acertos(self, dezenas_jogadas):
        dezenas_apuradas = self.dezenas
        acertos = 0
        for dezena_apurada in dezenas_apuradas:
            for dezena_jogada in dezenas_jogadas:
                if dezena_jogada == dezena_apurada:
                    acertos +=1
        return acertos     

    def verifica_lotofacil(self, dezenas):
        acertos = self.verifica_acertos(dezenas)
        if self.nome == 'lotofacil':
            if acertos >= 11:
                
                print(f'\nPREMIADO! ({self.concurso}) {acertos} acertos :D\n')
            else:
                print(f'NÃO PREMIADO! ({self.concurso}) {acertos} acertos :(')

conc2830 = Loteria('lotofacil', 2830, [2,3,4,8,9,10,11,12,13,17,18,20,21,22,25])
conc2831 = Loteria('lotofacil', 2831, [2,3,5,7,10,11,13,14,15,16,17,19,20,22,25])
conc2832 = Loteria('lotofacil', 2832, [1,2,3,5,6,11,14,15,16,19,20,21,22,23,24])
conc2833 = Loteria('lotofacil', 2833, [2,3,4,5,6,11,13,14,16,18,19,22,23,24,25])
conc2834 = Loteria('lotofacil', 2834, [1,6,8,10,11,12,13,14,17,19,20,21,22,23,25])
conc2835 = Loteria('lotofacil', 2835, [2,4,6,7,8,9,10,12,13,14,15,16,21,22,25])
conc2836 = Loteria('lotofacil', 2836, [1,2,3,4,7,9,12,14,15,17,18,20,21,22,23])
conc2837 = Loteria('lotofacil', 2837, [1,2,5,6,8,10,12,17,18,19,20,21,22,24,25])

dezenas_jogadas = [1,3,5,7,8,9,10,11,13,14,18,20,21,22,24,25]

conc2830.mostra_concurso()

conc2830.verifica_lotofacil(dezenas_jogadas)
conc2831.verifica_lotofacil(dezenas_jogadas)
conc2832.verifica_lotofacil(dezenas_jogadas)
conc2833.verifica_lotofacil(dezenas_jogadas)
conc2834.verifica_lotofacil(dezenas_jogadas)
conc2835.verifica_lotofacil(dezenas_jogadas)
conc2836.verifica_lotofacil(dezenas_jogadas)
conc2837.verifica_lotofacil(dezenas_jogadas)
