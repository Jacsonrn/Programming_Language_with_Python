def primos():
    contador = 0
    entrada = int(input("Digite um número inteiro positivo: "))
    original = entrada  # salva para exibir depois

    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        while entrada % p == 0:
            contador += 1
            entrada //= p  # divisão inteira para manter 'entrada' como int

    return original, contador

entrada, contador = primos()
print(f"{entrada} tem {contador} fatores primos")
