import random
import string

def gerar_senha(tamanho=12):
    simbolos = "!@#$%&*_-+=" 
    caracteres = string.ascii_letters + string.digits + simbolos

    senha = ""
    for _ in range(tamanho):
        senha += random.choice(caracteres)

    return senha

tam = int(input("Tamanho da senha (12 a 64): "))

if tam < 12 or tam > 64:
    print("Tamanho inválido. Use de 12 a 64.")
else:
    print("Senha gerada:", gerar_senha(tam))
    print("Dica: use WPA2/WPA3, desative WPS e troque o usuário/senha do roteador.")
