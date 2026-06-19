saldo = 0.0

def exibir_menu():
    print("\n--- MENU DO CAIXA ---")
    print("1) Consultar Saldo")
    print("2) Depositar")
    print("3) Sacar")
    print("4) Sair")

def consultar_saldo():
    print("Seu saldo é: R$", saldo)

def depositar():
    global saldo
    valor = float(input("Digite o valor do depósito: "))
    if valor <= 0:
        print("Erro: Você não pode depositar um valor negativo ou zero!")
    else:
        saldo = saldo + valor
        print("Depósito realizado com sucesso!")

def sacar():
    global saldo
    valor = float(input("Digite o valor do saque: "))
    if valor <= 0:
        print("Erro: O valor do saque deve ser maior que zero!")
    elif valor > saldo:
        print("Erro: Você não tem saldo suficiente!")
    else:
        saldo = saldo - valor
        print("Saque realizado com sucesso!")

opcao = 0

while opcao != 4:
    exibir_menu()
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        consultar_saldo()
    elif opcao == 2:
        depositar()
    elif opcao == 3:
        sacar()
    elif opcao == 4:
        print("Programa encerrado.")
    else:
        print("Opção inválida! Digite um número de 1 a 4.")