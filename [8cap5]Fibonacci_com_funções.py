def fibonacci(entrada):
    if entrada == 0:
        return 0
    elif entrada == 1:
        return 1
    else:
        return fibonacci(entrada-1) + fibonacci(entrada-2)

def soma_recursiva(lista):
    if len(lista) == 0:
        return 0
    else:
        item =lista.pop(0)
        return item + soma_recursiva(lista)
    
lista = []
lista =list(map(int,input().split(",")))

for i in (range(len(lista))):
    lista[i] = fibonacci(lista[i])

soma = soma_recursiva(lista)
print(soma)