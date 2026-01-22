usuario = "Ana"
senha = "1234"
input_usuario = input("Digite o nome de usuário: ")
input_senha = input("Digite a senha: ")
if input_usuario == usuario and input_senha == senha:
    print("Acesso concedido.")
else:
    print("Acesso negado.")