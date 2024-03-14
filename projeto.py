deposito = 0
saque = 500
extrato = []
numero_saque = 0
LIMITE_DE_SAQUE = 3

while True:  # loop infinito ate ter o break
    menu = input("""\n\nCAIXA ELETRÔNICO
[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

Selecione a opção que deseja realizar: 
""")
    if menu == '1':
        while True:  # loop infinito ate ter o break
            valor_deposito = float(input("Digite o valor do depósito: R$"))
            if valor_deposito > 0:  # numero inteiro positivo
                deposito = + valor_deposito
                # registrando a operacao no extrato
                extrato.append(f'Depósito: R${valor_deposito}')
                print("Depósito concluído com sucesso!")
                break  # parar a execução
            else:
                # irá tentar até a condição ser atendida
                print("Valor inválido! Tente novamente.")
    elif menu == '2':
        if numero_saque < LIMITE_DE_SAQUE:  # verifica se a tentativa é menor que 3 vezes
            while True:
                valor_saque = float(
                    input("Digite o valor que deseja sacar: R$"))
                if valor_saque <= saque:  # se o valor digitado for menor que 500
                    print("Sacando...")
                    saque -= valor_saque  # o valor sacado é retirado do saldo atual
                    extrato.append(f'Saque: R${valor_saque}')
                    print("Valor sacado com sucesso")
                    numero_saque += 1  # conta as vezes que foi sacado
                    break
                else:
                    print("Você está sem saldo para realizar saque.")
                    break
        else:
            print("Você atingiu o limite máximo de saques disponíveis por dia")
    elif menu == '3':
        for operacao in extrato:
            print(operacao)
        saldo_final = saque + deposito
        print(f"\nSaldo final: R${saque}")
    elif menu == '0':
        break
    else:
        print("Número selecionado inválido. Tente novamente")
