# Cabeçalho do sistema bancário
cabecalho = " ================ MRA INTERNET BANK ============="
print(cabecalho)

# Menu com as opções disponíveis para o usuário
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Variáveis iniciais
saldo = 0  # Saldo inicial da conta
limite = 500  # Limite máximo para saques
extrato = ""  # Histórico das operações realizadas
numero_saques = 0  # Contador de saques realizados
LIMITE_SAQUES = 3  # Número máximo de saques permitidos por dia

# Loop principal do programa (menu)
while True:
    # Exibe o menu e solicita a entrada do usuário
    opcao = input(menu)

    # Condicional para depósitos
    if opcao == "d":
        # Solicita o valor a ser depositado
        valor = float(input("Informe o valor do depósito: "))
        
        # Verifica se o valor é válido (maior que zero)
        if valor > 0:
            saldo += valor  # Atualiza o saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra no extrato
        else:
            # Mensagem de erro para valores inválidos
            print("Operação falhou! O valor informado é inválido.")

    # Condicional para saques
    elif opcao == "s":
        # Solicita o valor a ser sacado
        valor = float(input("Informe o valor para sacar: "))

        # Verificações de restrições
        excedeu_saldo = valor > saldo  # Verifica se o saque excede o saldo
        excedeu_limite = valor > limite  # Verifica se o saque excede o limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES  # Verifica se o limite de saques foi atingido

        # Condicionais para tratar as restrições
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número de saques excedido.")
        elif valor > 0:
            saldo -= valor  # Atualiza o saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Registra no extrato
            numero_saques += 1  # Incrementa o contador de saques
        else:
            # Mensagem de erro para valores inválidos
            print("Operação falhou! O valor informado é inválido.")

    # Condicional para exibir o extrato
    elif opcao == "e":
        print("\n========= EXTRATO =========")
        # Exibe mensagem padrão caso não haja movimentações
        print("Não foram realizadas movimentações." if not extrato else extrato)
        # Exibe o saldo atual
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================")

    # Condicional para sair do programa
    elif opcao == "q":
        # Encerra o loop principal
        break

    # Caso o usuário insira uma opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
