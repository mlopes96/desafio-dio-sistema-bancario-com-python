# Sistema Bancário com Python
# Primeiro desafio de projeto da Formação Python da DIO
# Versão 1, por Matheus Lopes

menu = '''
Bem vindo ao Banco Python!
Escolha uma das opções abaixo para prosseguir:
    
[1] Depositar
[2] Sacar
[3] Extrato
[0] Encerrar sessão

O que você deseja?
'''

# Variáveis para controle do banco
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == '0':
        print("Sua sessão foi finalizada!")
        break

    elif opcao == '1':
        # Depositar
        deposito = float(input("Informe o valor do depósito: "))

        if deposito > 0:
            saldo += deposito
            mensagem = f'Depósito de R$ {deposito:.2f} realizado.\n'
            extrato += mensagem
            print(mensagem)
        else:
            print("Não é permitido depositar valores negativos.")

    elif opcao == '2':
        # Sacar
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("Informe o valor do saque: "))
            if saque > 0:
                if saque <= limite:
                    if saldo >= saque:
                        saldo -= saque
                        numero_saques += 1
                        mensagem = f'Saque de R$ {saque:.2f} realizado.\n'
                        extrato += mensagem
                        print(mensagem)
                    else:
                        print("Saldo de conta insuficiente para este saque.")
                else:
                    print(f"Valor limite de saque excedido. O limite é R$ {limite:.2f}")
            else:
                print('Não é permitido saque de valor negativo.')
        else:
            print("Limite de saques excedido. Tente novamente amanhã.")

    elif opcao == '3':
        # Gerar extrato
        print("Banco Python\nExtrato da conta XXXXX\n")
        if extrato == '':
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print(f"O saldo da conta é R$ {saldo:.2f}")

    else:
        print("Operação inválida, por favor informe novamente sua opção escolhida.")
