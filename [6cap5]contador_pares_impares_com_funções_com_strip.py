def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

def contar_positivos_negativos(lista):
    positivos = 0
    negativos = 0
    for n in lista:
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1
    return positivos, negativos

# Programa principal
entrada = input("Digite os números separados por vírgula: ")
lista = [int(x.strip()) for x in entrada.split(",")]

pares, impares = contar_pares_impares(lista)
positivos, negativos = contar_positivos_negativos(lista)

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
