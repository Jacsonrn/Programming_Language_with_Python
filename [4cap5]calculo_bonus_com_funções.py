def calcular_bonificacao(medalhas, recorde_mundial, primeira_medalha_pais):
    # Define os valores base para cada medalha
    valores = {"ouro": 50000, "prata": 30000, "bronze": 10000}
    total = 0
    # Soma o valor de cada medalha recebida
    for medalha in medalhas:
        medalha = medalha.strip().lower()
        if medalha in valores:
            total += valores[medalha]
    # Adiciona bônus se aplicável
    if recorde_mundial.strip().lower() == "sim":
        total += 100000
    if primeira_medalha_pais.strip().lower() == "sim":
        total += 50000
    return total

medalhas = input("Digite as medalhas separadas por vírgula: ").split(",")
recorde_mundial = input("Quebrou recorde mundial? (Sim/Nao): ")
primeira_medalha_pais = input("Primeira medalha do país? (Sim/Nao): ")
bonus = calcular_bonificacao(medalhas, recorde_mundial, primeira_medalha_pais)
print(bonus)