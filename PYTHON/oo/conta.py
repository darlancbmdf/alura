class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print(f'Construindo objeto ... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Conta nº{self.__numero} Titular {self.__titular}\n')
        print(f'Saldo R${self.__saldo} limite R${self.__limite}')

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        print('Limite alterado!')

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print(f'Saque de {valor}, concluído com sucesso!')
        else:
            print(f'O valor {valor} passou o limite.')

    def transferencia(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def set_limite(self, novo_limite):
        self.__limite = novo_limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
