
from ast import main
import numpy as np

def analise_turma( notas):
    media = np.mean(notas)
    variancia = np.var(notas)
    desvio_padrao = np.std(notas)
    return media, variancia, desvio_padrao

def relatorio(media, variancia, desvio_padrao):
    print(f"Média das notas: {media:.2f}")
    print(f"Variancia das notas: {variancia:.2f}")
    print(f"Desvio padrão das notas: {desvio_padrao:.2f}")

notas_str = input("Digite as notas da turma, separadas por vírgula: ").split(",")
notas = np.array([float(n.strip()) for n in notas_str])
media, variancia, desvio_padrao = analise_turma(notas)
relatorio(media, variancia, desvio_padrao)

main()