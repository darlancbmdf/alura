from acesso_cep import BuscaEndereco
import requests

cep = 71100120

objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro)
print(cidade)
print(uf)
