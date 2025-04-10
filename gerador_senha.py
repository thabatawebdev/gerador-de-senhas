import random
import string

def gerar_senha(tamanho, usar_letras=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ''

    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros: 
        caracteres += string.digits 
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Você precisa selecionar pelo menos um tipo de caractere!" 

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))  
    return senha

# Interação com o usuário
try:
    tamanho = int(input("Digite o tamanho da senha: "))

    incluir_letras = input("Incluir letras? (s/n): ").strip().lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").strip().lower() == 's'
    incluir_simbolos = input("Incluir símbolos? (s/n): ").strip().lower() == 's'

    senha = gerar_senha(tamanho, incluir_letras, incluir_numeros, incluir_simbolos)
    print("Senha gerada:", senha)

except ValueError:
    print("Por favor, digite um número válido para o tamanho da senha.")    
    

