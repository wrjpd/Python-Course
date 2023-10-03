"""
O operador Walrus permite fazer atribuição e retorno de valor em uma mesma expressão.

# Sintaxe

variavel := expressao

"""

print(nome := "teste")


###### Outro exemplo ######

# Python 3.7
# cesta = []
# fruta = input("Informe a fruta: ")
# while fruta != "jaca":
#     cesta.append(fruta)
#     fruta = input("Informe a fruta: ")


# Python 3.8
cesta = []
while (fruta := input("Informe a fruta: ")) != "jaca":
    cesta.append(fruta)
