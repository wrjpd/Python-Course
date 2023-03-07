"""
# Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open().

open() -> Na forma mais simples de utilização nós passamos um parâmetro de entrada, o caminho do arquivo. Essa função retorna um __io.TextIOWrapper, e é com ele que trabalhamos.

Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então teremos o erro FileNotFounderror.

read() -> Le o arquivo. Pode ser passado um número como parâmetro que é o limitante de caracteres a serem lidos no arquivo




# seek, readline, readlines, close, closed e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo. Ela recebe um parâmetro que indica onde queremos colocar o cursor.

readline() -> Função que lê o arquivo linha a linha.

readlines() -> retorna uma lista com cada linha sendo um elemento.

close() -> # Quando abrimos o arquivo com a função open(), é criada uma conexão entre o arquivo no disco do computador e o código. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo, devemos fechar essa conexão, para isso utilizamos a função close().

Passos para se trabalhar com um arquivo:
1- Abrir o arquivo;
2- Trabalhar o arquivo;
3- Fechar o arquivo;

closed -> Verifica se o arquivo está aberto ou fechado


# With

Bloco with

Passo para se trabalhar com arquivos
1 - Abrir o arquivo
2 - Manipular o arquivo
3 - Fechar o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with.





# Escrevendo em arquivos

Para escrever precisamos abrir.
Ao abrir um arquivo para leitura, não podemos escrever nele. Da mesma forma, ao abrir um arquivo para a escrita, não podemos ler ele.

Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

write() -> Recebe uma string e escreve no arquivo.




# Modos de Arquivos

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita exclusiva. Da erro se já existir o arquivo.
a -> Abre para escrita, e adiciona ao arquivo original sem sobrescreve-lo. Se o arquivo não existir, ele cria. SEMPRE ADICIONA NO FINAL DO ARQUIVO.
+ -> Abre para o modo de atualização: Leitura e escrita





# StringIO

Para ler ou escrever dados em arquivos do sistema operacional, o software precisa ter permissão:
    - Permissão de leitura
    - Permissão de escrita

StringIO -> Utilizado para ler e criar arquivos em memória.





# Sistema de Arquivos - Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

os -> Operating System




# Sistema de Arquivos - Manipulação

"""

from os import system

# Leitura de Arquivos

arquivo=open("texto.txt")
print(arquivo) #<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
print(type(arquivo))

# Para ler o conteúdo de um arquivo após a sua abertura, devemos utilizar o atributo read()
print(arquivo.read())
print(arquivo.read()) # Nada é retornado. O Python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor funciona como o cursor quando estamos escrevendo.
 
arquivo=open("texto.txt") # Ao lermos o arquivo, ele é fechado e precisamos abrir novamente.
ret=arquivo.read() # Aqui estamos passando o arquivo para a variável ret, e assim podemos chamar quantas vezes quisermos.
print(ret)
print(ret)



system('cls')
# Seek e Cursors

arquivo=open('texto.txt')
print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0) # caractere na posição 0 .Movimenta o cursor para a posição 0 e então podemos reler o arquivo.
print(arquivo.read())


system('cls')
# readline

arquivo=open('texto.txt')
print(arquivo.readline()) # 1° linha
print(arquivo.readline()) # 2° linha
print(arquivo.read()) # Retorna a partir da 3° linha

system('cls')
# readlines()

arquivo=open('texto.txt')
print(arquivo.readlines())

system('cls')
# close()
# 1- Abrir o arquivo
arquivo=open('texto.txt')

# 2- Trabalhar o arquivo;
print(arquivo.read())

# 3- Fechar o arquivo;
arquivo.close()


# closed verifica se o arquivo está aberto ou fechado
print(arquivo.closed)




system("cls")
# With

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

# quando sai do bloco with o arquivo já está fechado
print(arquivo.closed)




system('cls')
# Escrevendo em arquivos

# O conteúdo anterior some.
# Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado. Caso ele ja exista, o anterior será apagado e um novo será criado.
with open("novo.txt",'w',encoding='utf-8') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha.\n')
    arquivo.write('Sem chamar a função novamente.\nSem chamar a função novamente.\nSem chamar a função novamente.')


# Recebendo dados do usuário e escrevendo o arquivo.

with open("frutas.txt","w") as arquivo:
    while True:
        break
        fruta = input("Informe uma fruta ou digite sair: ")
        if fruta != "sair":
            arquivo.write(fruta+'\n')
        else:
            break




system('cls')
# Modos de Arquivos

#x
try:
    with open('university.txt','x') as arquivo:
        arquivo.write("Teste de conteúdo.")
except FileExistsError:
    print('Arquivo já existe')


#a
with open("frutas2.txt","a") as arquivo:
    while True: 
        break       
        fruta = input("Informe umaa fruta ou digite sair: ")
        if fruta != "sair":
            arquivo.write(fruta+'\n')
        else:
            break


# +
with open('outro.txt','r+') as arquivo: # leitura + escrita
    arquivo.write('teste')
    arquivo.seek(0)
    arquivo.write('No topo\n')
    arquivo.write('Nova linha.\n')





system('cls')
# StringIO

from io import StringIO

mensagem = 'Este é apenas uma string normal.'
# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois.
arquivo=StringIO(mensagem)

# Agora tendo o arquivo, podemos utilizar tudo que já sabemos
print(arquivo.read())

# Podemos escrever
arquivo.write('Outro texto')

arquivo.seek(0)
print(arquivo.read())





system('cls')
# Sistema de Arquivos - Navegação

import os

print(os.getcwd()) # Pega o diretório atual (path absoluto)

# Para mudar o diretório, podemos usar chdir()
# os.chdir('..')
print(os.getcwd())

# Podemos checar se u diretório é absoluto ou relativo
print(os.path.isabs("C:\\Users\\T-Gamer")) # Windows
print(os.path.isabs("Users/T-Gamer"))

# Podemos identificar o sistema operacional com o módulo os
print(os.name) # posiz (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional
# print(os.uname()) # Só funciona em Posix 

# Mudar de diretório
print(os.getcwd()) #C:\Users\T-Gamer\Documents\Python\Leitura e Escrita de Arquivos

res=os.path.join(os.getcwd(),'folder_teste') # C:\Users\T-Gamer\Documents\Python\Leitura e Escrita de Arquivos/geek

os.chdir(res)
print(os.getcwd())

# Podemos listar os diretórios
print(os.listdir()) # Retorna uma lista com os arquivos
print(os.listdir("..\\"))

# Listar os diretórios com mais detalhes
print(os.scandir()) # Retorna um iterator
arquivos=list(os.scandir()) 

print(dir(arquivos)) # ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'] 

print('--')
print(os.getcwd())
print(arquivos[0])
print(arquivos[0].inode())
print(arquivos[0].is_dir()) # É um diretório? False
print(arquivos[0].is_file()) # É um arquivo? True
print(arquivos[0].is_symlink()) # É um link simbólico? False
print(arquivos[0].name)
print(arquivos[0].path)
print(arquivos[0].stat()) # Estatísicas sobre o arquivo

# Quando utilizamos a função scandir() nós precisamos fechá-la.

os.scandir().close







# Sistema de Arquivos - Manipulação



