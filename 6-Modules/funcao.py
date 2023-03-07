def soma_impares(numeros):
    total= 0
    for num in numeros:
        if num % 2!=0:
            total=total+num
    return total

lista=[1,2,3]