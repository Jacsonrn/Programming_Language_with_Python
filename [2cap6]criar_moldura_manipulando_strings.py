def criar_moldura(texto, caractere):
    tamanho = len(texto) + 4
    moldura = caractere * tamanho
    return f"{moldura}\n{caractere} {texto} {caractere}\n{moldura}"


texto = input("Digite o texto a ser moldurado: ")
caractere = input("Digite o caractere para a moldura (padrão é '*'): ") or '-'
resultado = criar_moldura(texto, caractere)
print(resultado)
