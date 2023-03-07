def funcao1():
    return 'Geek University'

if __name__ == '__main__':
    funcao1()
    print('dunder.py está sendo executado diretamente')
else:
    print(f'dunder.py está sendo importado {__name__}')