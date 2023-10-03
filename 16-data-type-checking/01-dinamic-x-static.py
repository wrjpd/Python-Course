"""

# Tipagem Dinâmica
-> A checagem de dados é feito somente na execução

# Tipagem Estática
-> A checagem é feita na compilação e informa se estiver algo errado antes da execução;
-> Não é permitido que a variável mude de tipo

"""

###### Problema na tipagem dinâmica ######

# O problema só aparece durante a execucao
resultado = None
if True:
    # resultado = 1+"Geek"
    pass
print(resultado)
