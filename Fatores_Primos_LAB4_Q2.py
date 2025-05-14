# Lê um número inteiro do usuário
n = int(input("Digite um número inteiro maior que 1: "))

# Começa testando o menor divisor primo, que é 2
divisor = 2

# Enquanto n for maior que 1, ainda há fatores primos para encontrar
while n > 1:
    # Se o divisor atual divide n, então é um fator primo
    if n % divisor == 0:
        print(divisor)         # Imprime o fator primo encontrado
        n = n // divisor       # Atualiza n dividindo pelo fator encontrado
    else:
        divisor += 1  
        # Se não divide, testa o próximo número como divisor
