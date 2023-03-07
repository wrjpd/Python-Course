"""
# Try/Except

Utilizamos o bloco try/except para tratar erros que podemo ocorrer no nosso código, previnindo assim que, o programa pare de funcionar e o usuário receba mensagens de erro inesperadas ou o código crashe.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problemas



#Try / Except / Else / Finally

Dica de quando e onde tratar código: Toda entrada deve ser tratada!
"""

# Bloco Try/Except

# Exemplo 1 - Tratando um erro genérico. Tratar erro de forma genérica é inadequado.
# Tente executar a função 'geek()', caso você encontre erro, imprima mensagem de erro.

try:
    geek()
except:
    print('Função não existe')


# Exemplo 2 - Tratando erro de forma específica. Melhor forma

try:
    geek()
except NameError: # Aqui só estamos tratando o tipo de erro "NameError". Se colocar o tipo de erro errado, o except não é executado e o erro aparece.
    print('Você está utilizando uma função inexistente')

# Exemplo 3 - retornando o erro.
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte error: {err}')




# Exemplo 4 - Diferentes tipos de erro:

try:
    len(5)
except NameError as err:
    print(f'Deu NameError:{err}')
except TypeError as err:
    print(f'Deu TypeError:{err}')


# Exemplo 5 - Valor default de erro

try:
    print('Geek'[9])
except NameError as err:
    print(f'Deu NameError:{err}')
except TypeError as err:
    print(f'Deu TypeError:{err}')
except:
    print('Deu um erro diferente')


# Exemplo 6 - Try sem except, ou seja, sem retornar nem printar nada

try:
    geek()
except:
    pass


# Exemplo 7 - Exemplo real

def pega_valor(dicionario,chave):
    print('oi')
    try:
        return dicionario[chave]
    except KeyError:# pega_valor(dic,"game")
        return None
    except TypeError: # peg_valor(7,"nome")
        return None



dic={"nome":"Geek"}
print(pega_valor(7,"nome"))





# Try, Except, Else e Finally


try:
    num=int(input("Informe um número: (try/except)"))    
except ValueError:
    print('Valor incorreto')

# print(f'Você digitou {num}') # Ainda retorna erro, pois a variável "num" não foi atribuida.


# else é executado somente se não ocorrer o erro, ou seja, se não entrar no except.
try:
    num=int(input("Informe um número: (else)"))    
except ValueError:
    print('Valor incorreto')
else:
    print(f"Você digitou {num}")


# finally é executado sempre. Independente se houve erro ou não
try:
    num=int(input("Informe um número: (finally)"))    
except ValueError:
    print('Valor incorreto')
else:
    print(f"Você digitou {num}")
finally:
    print('Executando o finally')

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.
# Exemplo: fechar banco de dados

# Exemplo mais complexo ERRADO

def dividir(a,b):
    return a/b


num1 = int(input("Informe o primeiro número: (Exemplo errado)"))

try:
    num2 = int(input("Informe o segundo número: (Exemplo errado) "))
except ValueError:
    print(" O valor precisa ser numérico")
    

try:
    print(dividir(num1,num2))
except NameError:
    print("Valor incorreto")


# Exemplo complexo - Correto
# O tratamento deve ser feito dentro da função

def dividir(a,b):
    try:
        return int(a)/int(b)
    except ValueError:
        return "Valor incorreto"
    except ZeroDivisionError:
        return "Não é possível realizar uma divisão por zero"

num1=input("Informe o primeiro número: (Exemplo certo)")
num2=input("Informe o segundo número: (Exemplo certo)")

print(dividir(num1,num2))


# Exemplo complexo Semi-genérico

def dividir(a,b):
    try:
        return int(a)/int(b)
    except (ValueError,ZeroDivisionError) as err:
        return f"Ocorreu um problema: {err}"
       

num1=input("Informe o primeiro número: (Exemplo semi-genérico)")
num2=input("Informe o segundo número: (Exemplo semi-genérico)")

print(dividir(num1,num2))
