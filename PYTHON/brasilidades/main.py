from cpf_cnpj import Documento

exemplo_cnpj = '08977914000119'
exemplo_cpf = '832348531345'

documento = Documento.cria_documento(exemplo_cpf)
print(documento)
