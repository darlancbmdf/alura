"""
classe para controle de data
"""
class Data:
    """ classe data """
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        """ método formatada """
        print(f'{self.dia}/{self.mes}/{self.ano}')
