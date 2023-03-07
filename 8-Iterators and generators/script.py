"""
# Entendendo Iterators e Iteráveis

Iterator    -> Um objeto que pode ser iterado.
            -> Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamado;

Iterable    -> Um objeto que irá retornar um iterator quando a função iter() for chamada.





# Criando sua própria versão de loop






# Geradores

 - Geradores são iterators; o contrário não é verdadeiro, ou seja, nem todo iterator é um generator

 Outras informações:
 - Generators podem ser criados com funções geradoras;
 - Funções geradoras utilizam a palavra reservada yield;
 - Generators podem ser criados com Expressões Geradoras

 # Diferença entre Funções e Generator Functions.


Funções
- Utiliza return
- Retorna uma vez
- Quando executada retorna um valor

Generator Functions
- Utiliza yield
- Pode utilizar yield múltiplas vezes
- Quando executada retorna um generator

 




# Teste de Memória com Geradores






# Teste de Velocidade com Expressões Geradoras







"""

# Entendendo iterators e iteráveis

nome='Geek' # É um iterable mas não é um iterator
numeros=[1,2,3,4,5] # É um iterable mas não é um iterator

# print(next(nome)) # TypeError: 'str' object is not an iterator
# print(next(numeros)) # TypeError: 'str' object is not an iterator

# Transformando iterable em iterator

it1=iter(nome) # <str_iterator object at 0x7efcb0adef70>
it2=iter(numeros)
print(it2) # <list_iterator object at 0x7f52d7b2a490>


# Agora podemos usar o next()

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
# print(next(it1)) # Traceback (most recent call last):
#   File "/home/joao/Documentos/pendrive/Python/Python/Iteradores e Geradores/script.py", line 62, in <module>
#     print(next(it1))
# StopIteration


# Por baixo dos panos, o python pega o iterable 'nome', aplica o iter() e executa o next() até o final
nome='Geek'
for letra in nome:
    print(f'{letra}')





# Criando sua própria versão de loop

def meu_for(iterable):
    it=iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
        
meu_for([1,2,3])







# Escrevendo um Iterador costumizado

class Contador:
    def __init__(self,menor,maior):
        self.menor=menor
        self.maior=maior

com=Contador(1,61)
print(com) # <__main__.Contador object at 0x7fa332c8a490>
print(com.menor)
print(com.maior)


# Podemos tranformar em um iterável?

# it= iter(com) # TypeError: 'Contador' object is not iterable
# print(next(it))

# Para ser iterável, precisamos adicionar um método __iter__ e __next__

class Contador:
    def __init__(self,menor,maior):
        self.menor=menor
        self.maior=maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero=self.menor
            self.menor=self.menor+1
            return numero
        raise StopIteration
    
com = Contador(1,10)
it= iter(com) # TypeError: 'Contador' object is not iterable
print(next(it))

for n in Contador(1,4):
    print(n)









# Geradores

# Exemplo de Generator Function

# Uma Generator Function não é um Generator, ela gera um Generator
def conta_ate(valor_maximo):
    contador=1
    while contador <= valor_maximo:
        yield contador
        contador=contador+1

gen=conta_ate(10)
print(type(gen)) # <class 'generator'>

print(next(gen))
print(next(gen))

for n in gen: # Parte a partir do 3
    print(n)





# Teste de Memória com Geradores

# Utilizando um for pra printar 100.000 números:

# Função utilizando listas : 449Mb
def fib_list(max):
        nums=[]
        a,b=0,1
        while len(nums) < max:
            nums.append(b)
            a,b=b,a+b
        return nums

print(fib_list(5))

# Agora, vamos utiizar o gerador
# Função Geradora : 3Mb
def fib_gen(max):
    a,b,contador=0,1,0
    while contador < max:
        a,b=b,a+b
        yield a
        contador = contador + 1
print(list(fib_gen(5)))





# Teste de Velocidade com Expressões Geradoras

# Ambas geram um ge: Generator Functions e Generator Expression

# Generator Function
def nums(max):
    for num in range(1,max):
        yield num

ge1=nums(100000000)
print(ge1) # <generator object nums at 0x7fe38deb3c10>

# Generator Expression
ge2= (num for num in range(1,10)) # <generator object <genexpr> at 0x7fed71627c10>
print(ge2)



# Realizando o teste de velocidade
import time

# Generator Function
fun_inicio=time.time()
print(sum(ge1))
fun_tempo=time.time()-fun_inicio

# Generator Expression
gen_inicio=time.time()
print(sum(num for num in range(100000000)))
gen_tempo=time.time()-gen_inicio

# List Comprehension
list_inicio=time.time()
print(sum([num for num in range(100000000)]))
list_tempo=time.time()-gen_inicio

print(f'Generator Function levo {fun_tempo}')
print(f'Generator Expression levo {gen_tempo}')
print(f'List Comprehension levo {list_tempo}')




