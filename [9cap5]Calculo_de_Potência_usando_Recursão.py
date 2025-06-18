def calcular_potencia_recursiva(base, expoente):
    if expoente == 0:
        return 1
    elif expoente < 0:
        # Lidar com expoentes negativos (retornando 1 / base ^ (-expoente))
        return 1 / calcular_potencia_recursiva(base, -expoente)
    else:
        return base * calcular_potencia_recursiva(base, expoente - 1)

resultado = calcular_potencia_recursiva(2, 30)
print(resultado)

