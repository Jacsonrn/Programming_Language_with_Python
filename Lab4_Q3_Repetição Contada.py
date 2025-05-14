b = int(input("Digite o valor de b: "))
y = 0
for n in range(1, b + 1):
    y += n ** (1 / n)
print("O valor de y é:", y)