def calcular_fatoriais(m):
    fatorial=1
    for i in range(1, m+1):
        fatorial *= i
        print(f"{i}! = {fatorial}")
m = int(input("Digite um número inteiro positivo:"))
calcular_fatoriais(m)

