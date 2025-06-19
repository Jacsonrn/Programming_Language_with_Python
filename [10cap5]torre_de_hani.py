def torre_de_hani(n, origem, auxiliar, destino):
    """
    Resolve o problema da Torre de Hanói recursivamente.

    Args:
        n (int): O número de discos a serem movidos.
        origem (str): O nome da haste de origem.
        auxiliar (str): O nome da haste auxiliar.
        destino (str): O nome da haste de destino.
    """
    if n == 1:
        print(f"Move disco 1 de {origem} para {destino}")
    else:
        torre_de_hani(n - 1, origem, destino, auxiliar)
        print(f"Move disco {n} de {origem} para {destino}")
       

# Exemplo de uso com 3 discos
torre_de_hani(2, 'A', 'B', 'C') # Saída:
# Move disco 1 de A para C
# Move disco 2 de A para B
# Move disco 1 de C para B
# Move disco 3 de A para C
# Move disco 1 de B para A
# Move disco 2 de B para C
# Move disco 1 de A para C