import numpy as np

def gerar_matrizes(N, semente):
    """
    Gera duas matrizes quadradas (N x N) com inteiros aleatórios.

    Args:
        N (int): A dimensão das matrizes quadradas.
        semente (int): A semente para o gerador de números aleatórios.

    Returns:
        tuple: Uma tupla contendo as duas matrizes NumPy (matriz_A, matriz_B).
    """
    # Define a semente aleatória para garantir a reprodutibilidade dos resultados
    np.random.seed(semente)

    # Gera as matrizes com números inteiros aleatórios entre 1 e 10.
    # O limite superior (high) em randint é exclusivo, por isso usamos 11.
    matriz_A = np.random.randint(1, 11, size=(N, N))
    matriz_B = np.random.randint(1, 11, size=(N, N))

    return matriz_A, matriz_B

def main():
    """
    Função principal para solicitar entradas do usuário, gerar e exibir as matrizes.
    """
    try:
        # Solicita a dimensão e a semente ao usuário
        N = int(input("Digite a dimensão das matrizes (N): "))
        semente = int(input("Digite a semente para o gerador aleatório: "))

        # Gera as matrizes
        matriz_A, matriz_B = gerar_matrizes(N, semente)

        # Exibe os resultados
        soma = matriz_A + matriz_B
        produto = np.dot(matriz_A, matriz_B)
        transposta_produto = produto.T
        determinante_produto = np.linalg.det(produto)
        if determinante_produto != 0:
            inversa_produto = np.linalg.inv(produto)
        else:
            print("O produto das matrizes não é invertível (determinante é zero).")
        

    except ValueError:
        print("\nErro: Por favor, insira apenas números inteiros válidos.")

# Executa a função principal quando o script é rodado
if __name__ == "__main__":
    main()