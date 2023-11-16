import secrets
import string

print('=================================\n||      GERADOR DE SENHAS      ||\n=================================')

tamanho = int(input("Digite o tamanho desejado da senha: "))

print('=================================\n')

def gerar_senha(tamanho):
    letras = string.ascii_letters
    digitos = string.digits
    pontuacao = string.punctuation

    caracteres = letras + digitos + pontuacao
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    
    return senha

senha = gerar_senha(tamanho)
print("Sua senha é: " f"{senha}")

print('=================================\n')