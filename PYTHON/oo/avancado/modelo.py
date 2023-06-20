class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} likes'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

    def __add__(self, novo):
        if isinstance(novo, Playlist):
            nova_lista = self._programas + novo._programas
            return nova_lista
        else:
            raise TypeError("Operação de adição não suportada.")


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2006, 2)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

jhon_wick = Filme('jhon wick', 2018, 180)
jhon_wick.dar_likes()
jhon_wick.dar_likes()
jhon_wick.dar_likes()

#adição de item a playlist já criada 
filme_add = [jhon_wick]
filme_add_playlist = Playlist('jhon wick', filme_add)
playlist_fim_de_semana = playlist_fim_de_semana + filme_add_playlist

print(len(playlist_fim_de_semana))

for programa in playlist_fim_de_semana:
    print(programa)
