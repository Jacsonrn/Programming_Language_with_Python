a = int(input('Digite um número inteiro entre 100 e 1000'))
if a < 100 or a > 1000:
    print("Número fora do intervalo")
else: b = a % 5
print(a,b)