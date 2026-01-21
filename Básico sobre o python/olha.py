import random   

def jogar():
    usuario = input("escolha : pedra, papel ou tesoura: ")
    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)

    print(f"Você escolheu: {usuario}")
    print(f"Computador escolheu: {computador}")

    if usuario == computador:
        print("Empate!")
    
    if venceu(usuario, computador):
        print("Você venceu!")
    else:
        print("Você perdeu!")   

def venceu(jogador, oponente):
    if (jogador == "pedra" and oponente == "tesoura") or \
       (jogador == "papel" and oponente == "pedra") or \
       (jogador == "tesoura" and oponente == "papel"):
        return True
    return False
print(jogar())