def multiplicacao_recursiva(a, b):
    # Se b for 0, retornamos 0 (base da recursão)
    if b == 0:
        return 0
    # Se b for negativo, ajustamos chamando a função com valores positivos
    if b < 0:
        return -multiplicacao_recursiva(a, -b)
    # Caso recursivo: somar 'a' repetidamente
    return a + multiplicacao_recursiva(a, b - 1)

# Entrada do usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Chamada da função e exibição do resultado
resultado = multiplicacao_recursiva(num1, num2)
print(f"O resultado da multiplicação é: {resultado}")
