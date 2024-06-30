def saque():
    global limite_saque, limite, saque_total
    if limite_saque > 0:                
            valor = int(input("Qual valor será sacado? "))
            if valor <= 500 and valor <= limite:
                print("Saque efetuado com sucesso! ")
                saque_total += valor
                limite_saque -= 1
                limite -= valor
            else: 
                print("Saldo insuficiente!")
    else:
        print("Limite de saque excedido!")

def deposito():
    global limite, deposito_total
    valor = int(input("Quanto gostaria de depositar? "))
    limite = limite + valor
    deposito_total = deposito_total + valor
    print("Depósito realizado com sucesso!")

def extrato():
    print(f"Valor depositado: {deposito_total}")
    print(f"Valor sacado: {saque_total}")
    print(f"Extrato: {limite}")


def cadastro_cliente(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF!")
        return
    nome = input("Informe seu nome completo: ")
    nascimento = input("Informe a data de nascimento: ")
    usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf})
    print("Usuário cadstrado!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}
    print("Usuário não encontrado!")
    



menu ="""
        MENU

    D - Depósito
    S - Saque
    E - Extrato
    1 - Novo Usuário
    2 - Nova Conta
    0 - Sair
"""
print(menu)

limite_saque = 3
deposito_total = 0
limite = 500
saque_total = 0
opcao = -1
usuarios = []
contas = []
AGENCIA = "0001"
    

while opcao != "0":
    opcao = input("Qual opção gostaria de escolher? ").upper()

    if opcao == "D":
        deposito()
        
    elif opcao == "S":
        saque()               
        
    elif opcao == "E":
        extrato()
    elif opcao == "1":
        cadastro_cliente(usuarios)
    elif opcao == "2":
        numero_conta = len(contas)+1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
    elif opcao =="0":
        print("Saindo do programa...")
    else:
        print("Opção inválida")