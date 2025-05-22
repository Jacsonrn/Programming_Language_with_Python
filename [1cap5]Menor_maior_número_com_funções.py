def ler_numeros():
    """Esse função recebe três números inteiros  e retorna esses valores 
    """
    a = int(input("Digite o primeiro númeor"))
    b = int(input("Digite o segundo número"))
    c = int(input("Digite o terce"))
    return a, b, c

def encontra_menor_maior(a, b, c):
    """Essa função encontra o maior e menor valor entre três númuros inteiros"""
    menor = min(a, b, c)
    maior = max(a, b, c)
    return menor, maior

num1, num2, num3 = ler_numeros()
menor, maior = encontra_menor_maior(num1, num2, num3)
print(f"O menor número é {menor}")
print(f"O maior número é {maior}")
