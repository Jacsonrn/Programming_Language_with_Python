def ler_dados():
    """Lê os coeficientes A, B e C do usuário e retorna como float."""
    A = float(input("Digite o valor de A: "))
    B = float(input("Digite o valor de B: "))
    C = float(input("Digite o valor de C: "))
    return A, B, C

def pode_calcular_raizes(A, B, C):
    """Verifica se é possível calcular as raízes (A ≠ 0 e delta ≥ 0)."""
    delta = B**2 - 4*A*C
    return A != 0 and delta >= 0

def calcular_raizes(A, B, C):
    """Calcula e retorna as raízes da equação de segundo grau."""
    delta = B**2 - 4*A*C
    x1 = (-B + delta**0.5) / (2*A)
    x2 = (-B - delta**0.5) / (2*A)
    return x1, x2

# Programa principal
A, B, C = ler_dados()
if pode_calcular_raizes(A, B, C):
    x1, x2 = calcular_raizes(A, B, C)
    print(f"R1 = {x1:.2f}")
    print(f"R2 = {x2:.2f}")
else:
    print("Impossível calcular")