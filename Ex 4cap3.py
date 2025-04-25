A = int(input("Digite um número entre 10 e 20: "))
if A > 10 and A < 20:
    B = bin(A)[2:]  # Converte o número para binário
  
    bits = list(B)
    print(bits)
    
else:
    print("O número está fora do intervalo.")
