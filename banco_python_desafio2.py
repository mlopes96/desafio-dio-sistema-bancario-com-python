# Sistema Bancário com Python
# Segundo desafio de projeto da Formação Python da DIO
# Versão 1, por Matheus Lopes

def menu():
    menu = '''
    Bem vindo ao Banco Python!
    +++++++++++++++++++++++++++++++++++++++++++++
    Escolha uma das opções abaixo para prosseguir:
    [0] Encerrar sessão
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar novo correntista
    [5] Criar nova conta
    [6] Listar contas criadas
    [7] Listar correntistas   
    '''
    return input(menu)


def depositar(saldo, deposito, extrato, /):

    if deposito > 0:
        saldo += deposito
        extrato += f'Depósito:\tR$ {deposito:.2f}\n'
        print(f'Depósito de R$ {deposito:.2f} realizado com sucesso!\n')
    else:
        print("ERRO: Não é permitido depositar valores negativos.")

    return saldo, extrato


def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = saque > saldo
    excedeu_limite = saque > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("ERRO: Saldo de conta insuficiente para este saque.")

    elif excedeu_limite:
        print(f"ERRO: Valor limite de saque excedido. O limite é R$ {limite:.2f}")

    elif excedeu_saques:
        print("ERRO: Limite de saques excedido. Tente novamente amanhã.")

    elif saque > 0:
        saldo -= saque
        numero_saques += 1
        extrato += f'Saque:\tR$ {saque:.2f}\n'
        print(f'Saque de R$ {saque:.2f} realizado com sucesso!\n')

    else:
        print('ERRO: Não é permitido saque de valor negativo.')

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):

    print("Banco Python\nExtrato da conta XXXXX\n")

    if extrato == '':
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
        print(f"O saldo da conta é R$ {saldo:.2f}")


def cadastrar_correntista(correntistas):
    cpf = input("Informe o CPF (somente números): ")
    correntista = filtrar_correntista(cpf, correntistas)

    if correntista:
        print("ERRO: Já existe correntista com esse CPF!\n")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    correntistas.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Correntista criado com sucesso!\n")


def filtrar_correntista(cpf, correntistas):
    correntistas_filtrados = [correntista for correntista in correntistas if correntista['cpf'] == cpf]
    return correntistas_filtrados[0] if correntistas_filtrados else None


def criar_conta(agencia, numero_conta, correntistas):
    cpf = input("Informe o CPF do correntista (somente números): ")
    correntista = filtrar_correntista(cpf, correntistas)

    if correntista:
        print("Conta criada com sucesso!")
        return{"agencia": agencia, "numero_conta": numero_conta, "correntista": correntista}
    else:
        print("ERRO: Correntista não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['correntista']['nome']}
        '''
        print(linha)


def listar_correntistas(correntistas):
    for correntista in correntistas:
        linha = f'''\
            Correntista:\t{correntista['nome']}
            CPF:\t\t{correntista['cpf']}
            Endereço:\t{correntista['endereco']}
        '''
        print(linha)


def main():
    # Variáveis para controle do banco
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    correntistas = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == '0':
            print("Sua sessão foi finalizada!")
            break

        elif opcao == '1':
            # Depositar
            deposito = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, deposito, extrato)

        elif opcao == '2':
            # Sacar
            saque = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(saldo=saldo, saque=saque, extrato=extrato,
                                   limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == '3':
            # Gerar extrato
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            cadastrar_correntista(correntistas)

        elif opcao == '5':
            conta = criar_conta(AGENCIA, numero_conta, correntistas)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == '6':
            listar_contas(contas)

        elif opcao == '7':
            listar_correntistas(correntistas)

        else:
            print("Operação inválida, por favor informe novamente sua opção escolhida.")


main()
