endereco = 'Rua Padre Aurélio, Casa 744, bairro centro, santana, BA, 47700000'

import re # Regular Expression -- RegEx


# padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}") # usando multiplicadores {5} e {3}
# padrao = re.compile("[0-9]{5}[-]?[0-9]{3}") # usando o '?'
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") # usando intervalos 0-9 e no caso do [-]{0,1} informando que pode ocorrer de 0 a 1 vez

busca = padrao.search(endereco) # Match
if busca:
    cep = busca.group()
    print(cep)
