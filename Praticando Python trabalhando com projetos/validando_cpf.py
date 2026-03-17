def validar_cpf(cpf):
    if not cpf.isdigit():
        return "Erro: o CPF deve conter apenas numeros"
    if len(cpf) != 11:
        return "Erro: O CPF deve ter exatamente 11 digitios."
    return "CPF Válido"

cpf = input("Digite seu CPF: ")
print(validar_cpf(cpf))