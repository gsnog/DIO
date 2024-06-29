menu ="""
        MENU

    D - Depósito
    S - Saque
    E - Extrato
    0 - Sair
"""
print(menu)

limite_saque = 3
deposito = 0
limite = 500
saque = 0
opcao = -1

while opcao != "0":
    opcao = input("Qual opção gostaria de escolher? ").upper()

    if opcao == "D":
        valor = int(input("Quanto gostaria de depositar? "))
        limite = limite + valor
        deposito = deposito + valor
        
    elif opcao == "S":
        if limite_saque > 0:                
            valor = int(input("Qual valor será sacado? "))
            if valor <= 500 and valor <= limite:
                print("Saque efetuado com sucesso! ")
                saque += valor
                limite_saque -= 1
                limite -= valor
            else: 
                print("Saldo insuficiente!")
        else:
            print("Limite de saque excedido!")        
        
    elif opcao == "E":
        print(f"Valor depositado: {deposito}")
        print(f"Valor sacado: {saque}")
        print(f"Extrato: {limite}")
    
    elif opcao =="0":
        print("Saindo do programa...")
    else:
        print("Opção inválida")
        