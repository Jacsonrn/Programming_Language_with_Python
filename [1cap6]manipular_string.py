def manipular_string(s):
    if not s: # Verifica se a string está vazia
        print("A string não pode ser vazia.")
        return None, None, None, None, None, None # Retorna None para todos os valores

    primeiro_caractere = s[0]
    ultimo_caractere = s[-1]
    tresprimeiros = s[:3]
    tresultimos = s[-3:]
    invertida = s[::-1]
    remove_voagais = ''.join(c for c in s if c.lower() not in 'aeiou')
    # A variável 'resultado' não está sendo usada no retorno, então pode ser removida ou usada para depuração.
    # resultado = [primeiro_caractere, ultimo_caractere, tresprimeiros, tresultimos, invertida,remove_voagais]
    return primeiro_caractere, ultimo_caractere, tresprimeiros, tresultimos, invertida, remove_voagais
    
def main():
    s = input('Digite uma string:')
    primeiro, ultimo, tres_primeiros, tres_ultimos, invertida, sem_vogais = manipular_string(s)
    
    if primeiro is not None: # Verifica se a manipulação foi bem-sucedida (string não vazia)
        print(f'Primeiro caractere: {primeiro}')
        print(f'Último caractere: {ultimo}')
        print(f'Três primeiros caracteres: {tres_primeiros}')
        print(f'Três últimos caracteres: {tres_ultimos}')
        print(f'String invertida: {invertida}')
        print(f'String sem vogais: {sem_vogais}')
    else:
        print("Não foi possível processar a string.")
main()