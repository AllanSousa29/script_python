menu = """

================= OPÇÕES =================

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("\nDeposito efetuado com sucesso\n")
        
        else:
            print("Operação falhou! O valor informado é invalido")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = saldo < valor

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do seu saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\nSaque efetuado com sucesso\n")
        
        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "e":
        print("\n================= EXTRATO =================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")
    
    elif opcao == "q":
        print("Sessão encerrada")
        break
    
    else:
        print("Operação Invalida, por favor selecione novamente a operação desejada.")