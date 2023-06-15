"""
Classe para controle de contas
"""
class Conta:
    """ Class Conta """

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print(f'Construindo objeto ... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        """ metodo extrato """
        print(f'Conta nº{self.__numero} Titular {self.__titular}\n')
        print(f'Saldo R${self.__saldo} limite R${self.__limite}')

    def get_saldo(self):
        """ metodo tet_saldo"""
        return self.__saldo

    def get_titular(self):
        """ metodo get_titular"""
        return self.__titular

    @property
    def limite(self):
        """ metodo get_limite"""
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        print('Limite alterado!')

    def depositar(self, valor):
        """ metodo depositar """
        self.__saldo += valor

    def sacar(self, valor):
        """ metodo sacar """
        self.__saldo -= valor

    def transferencia(self, valor, destino):
        """ metodo transferência """
        self.sacar(valor)
        destino.depositar(valor)

    def set_limite(self, novo_limite):
        """ metodo set_limite """
        self.__limite = novo_limite
