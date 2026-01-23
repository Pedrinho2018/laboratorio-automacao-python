def limpar_cpf(cpf):
    return cpf.replace(".", "").replace("-", "")

def cpf_formatado(cpf_limpo):
    return len(cpf_limpo) == 11 and cpf_limpo.isdigit()

cpf = input("Digite um CPF: ")
cpf_limpo = limpar_cpf(cpf)

if cpf_formatado(cpf_limpo):
    print("✅ CPF válido.")
    print(f"CPF formatado: {cpf_limpo}")
else:
    print("❌ CPF inválido.")
    print("Formato esperado de  11 dígitos")