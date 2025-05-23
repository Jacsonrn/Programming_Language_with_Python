import math

print("Digite 1 para: Calcular a área de um triângulo (base e altura)")
print("Digite 2 para: Calcular a área de um círculo")
print("Digite 3 para: Calcular a área de um retângulo")
print("Digite 4 para: Sair do programa")
a = int(input())

def area_triangulo():
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    dtriangulo = (base * altura) / 2
    return dtriangulo

def area_circulo():
    raio = float(input("Digite o raio do círculo: "))
    dcirculo = math.pi * (raio ** 2)
    return dcirculo

def area_retangulo():
    comprimento = float(input("Digite o comprimento do retângulo: "))
    largura = float(input("Digite a largura do retângulo: "))
    dretangulo = comprimento * largura
    return dretangulo

if a == 1:
    dtriangulo = area_triangulo()
    print("Área do triângulo:", dtriangulo)
elif a == 2:
    dcirculo = area_circulo()
    print("Área do círculo:", dcirculo)
elif a == 3:
    dretangulo = area_retangulo()
    print("Área do retângulo:", dretangulo)
elif a == 4:
    print("Você saiu do programa")
else:
    print("Opção inválida")
