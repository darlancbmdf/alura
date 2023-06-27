from cpf_cnpj import Documento

exemplo_cnpj = '08977914000119'
exemplo_cpf = '83234853134'

documento = Documento.cria_documento(exemplo_cpf)
print(documento)
