"""
Assertions (Afirmações/Checagens)

Em Python, utilizamos a palavra reservada "assert" para realizar simples afirmações utilizadas nos testes.

Utilizamos o "assert" em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, o assert retorna None e caso seja falsa levanta um erro do tipo AssertionError.

# Obs: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada.

# Obs: A palavra "assert" pode ser utilizada em qualquer função ou código, não precisa ser exclusivamente nos testes.


ALERTA: Cuidado ao utilizar "assert"
- Se um programa Python for executado com o parâmetro -O, nenhum assertion será validado, ou seja, todas as suas validações ja eram



"""


def soma_numeros_positivos(a, b):
    try:
        assert a > 0 and b > 0, "Ambos números precisam ser positivos"
        return a+b
    except (AssertionError) as error:
        return error


print(soma_numeros_positivos(1, -3))  # AssertionError
