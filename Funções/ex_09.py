def senha_forte(senha):
    tem_numero = False

    for ch in senha:
        if ch.isdigit():
            tem_numero = True

    if len(senha) >= 8 and tem_numero:
        return True
    else:
        return False

senha = input("Digite uma senha: ")

if senha_forte(senha):
    print("✅ Senha forte.")
else:
    print("❌ Senha fraca.")
