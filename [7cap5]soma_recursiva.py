def soma_recursiva(lista):
    if len(lista) == 0:
        return 0
    else:
        item =lista.pop(0)
        return item + soma_recursiva(lista)
    
lista = [1, 2, 3, 4, 5]
resultado = soma_recursiva(lista.copy())
print(f"A soma dos elementos da lista é: {resultado}")

    