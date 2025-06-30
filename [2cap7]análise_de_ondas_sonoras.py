import numpy as np
import matplotlib.pyplot as plt

# Dados: tempo em segundos e amplitudes correspondentes
tempo = np.linspace(0, 2*np.pi, 1000)
amplitudes = np.sin(2*tempo) + 0.5*np.cos(5*tempo)
valor_maximo = np.max(amplitudes)
valor_minimo = np.min(amplitudes)

print(f"Valor máximo da amplitude: {valor_maximo:.4f}")
print(f"Valor mínimo da amplitude: {valor_minimo:.4f}")

# Encontrar os pontos de tempo onde a amplitude é próxima de zero
# Usamos np.isclose para comparar com uma tolerância (atol)
indices_proximos_zero = np.where(np.isclose(amplitudes, 0, atol=1e-3))
tempos_proximos_zero = tempo[indices_proximos_zero]

# Imprimir os resultados
print("\nPontos de tempo onde a amplitude é próxima de zero (tolerância de 1e-3):")
for t in tempos_proximos_zero:
    print(f"{t:.4f} segundos")

# Calcule a energia total do sinal (soma dos quadrados das amplitudes)
# A forma vetorizada do NumPy é muito mais eficiente que um loop for.
energia_total = np.sum(amplitudes**2)

print(f"\nEnergia total da onda sonora: {energia_total:.4f}")


# Definindo os dados para os eixos X e Y
x = tempo
y = amplitudes

# Criando o gráfico de linha
plt.plot(x, y)

# Adicionando rótulo ao eixo X
plt.xlabel('Tempo (s)')

# Adicionando rótulo ao eixo Y
plt.ylabel('Amplitude')

# Adicionando título ao gráfico
plt.title('Análise de Onda Sonora')

# Exibindo o gráfico
plt.show()