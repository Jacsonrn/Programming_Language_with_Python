import numpy as np 
temperaturas = np.array([
    [ 25.5, 26.1, 27.8, 28.3, 27.9, 26.8, 25.9 ],   # Domingo
    [ 24.8, 25.3, 26.5, 27.1, 26.7, 25.6, 24.9 ],   # Segunda
    [ 23.9, 24.5, 25.8, 26.4, 26.0, 24.9, 24.1 ],   # Terça
    [ 24.2, 24.8, 26.1, 26.7, 26.3, 25.2, 24.4 ],   # Quarta
    [ 25.1, 25.7, 27.0, 27.6, 27.2, 26.1, 25.3 ],   # Quinta
    [ 26.0, 26.6, 28.1, 28.7, 28.3, 27.2, 26.3 ],   # Sexta
    [ 25.4, 26.0, 27.5, 28.0, 27.6, 26.5, 25.7 ]    # Sábado
])
media_diaria = np.mean(temperaturas, axis=1)
print("Temperaturas médias diárias:")
dias_da_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
for i in range(len(dias_da_semana)):
    print(f"{dias_da_semana[i]}: {media_diaria[i]:.2f}°C")
print(f"tempratura máxima da semana:{np.max(temperaturas)} C°")
print(f"tempratura mínima da semana:{np.min(temperaturas)} C°")

temperaturas_maximas = np.max(temperaturas, axis=1)
temperatura_minima = np.min(temperaturas, axis=1)

print("Diferença entre a temperatura máxima e mínima de cada dia:")
for i in range(len(dias_da_semana)):
    diferença = temperaturas_maximas[i] - temperatura_minima[i]
    print(f"{dias_da_semana[i]}: {diferença:.2f}°C")

    