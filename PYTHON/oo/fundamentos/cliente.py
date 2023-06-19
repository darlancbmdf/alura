class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome.title() # title() deixa a primeira letra maiuscula

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
