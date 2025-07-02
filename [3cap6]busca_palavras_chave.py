def contar_ocorrencias_palavras_chave(texto, palavras_chaves):
    """
    Conta as ocorrências de palavras-chave em um texto e retorna um dicionário.

    :param texto: Texto onde as palavras-chave serão buscadas.
    :param palavras_chaves: Lista de palavras-chave a serem buscadas.
    :return: Dicionário com as palavras-chave como chaves e suas contagens como valores.
    """
    # Normaliza o texto: minúsculas e remove pontuações básicas para uma contagem precisa.
    texto_limpo = texto.lower().replace(',', '').replace('.', '')
    palavras_do_texto = texto_limpo.split()

    # Cria um dicionário para armazenar a contagem de cada palavra-chave.
    # Usamos uma "dictionary comprehension" para uma solução concisa.
    contagem_palavras = {
        palavra_chaves: palavras_do_texto.count(palavra_chaves.lower())
        for palavra_chaves in palavras_chaves
    }
    
    return contagem_palavras

# --- Parte principal do programa ---

# O texto deve ser uma única string, não uma lista.
texto = input("Digite o texto para a busca: ")
# As palavras-chave são separadas por vírgula, então usamos split() e strip() para limpar espaços.
palavras_chaves_input = input("Digite as palavras-chave separadas por vírgula: ")
palavras_chaves = [p.strip() for p in palavras_chaves_input.split(",")]

# Chama a função e obtém o dicionário de ocorrências
ocorrencias = contar_ocorrencias_palavras_chave(texto, palavras_chaves)

print(ocorrencias)

# Exibe o resultado de forma mais clara
"""print("\n--- Relatório de Ocorrências ---")
if not any(ocorrencias.values()):
    print("Nenhuma das palavras-chave foi encontrada no texto.")
else:
    for palavra, contagem in ocorrencias.items():
        print(f"- A palavra '{palavra}' apareceu {contagem} vez(es).")"""