def dados():
    peso = float(input("Digite seu peso:"))
    altura = float(input("Digite sua altura:"))
    return peso, altura
def imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def resultado(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25.9:
        return "Peso noormal"
    elif 25.9 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 40:
        return "Obesidade"
    else:
        return "Obesidade mórbida"
peso, altura = dados()
imc = imc(peso, altura)
classifucacao = resultado(imc)
print(f"Seu IMC é {imc:.2f} e você está classificado como {classifucacao}")
# Esse código calcula o IMC de uma pessoa e classifica seu estado nutricional