from app.persistence.database import initialize_db, get_session


class MenuCliente:
    def __init__(self, conta_use_cases):
        self.conta_use_cases = conta_use_cases
        self.conta_autenticada = None  # Inicialmente não há conta autenticada

    def autenticar_cliente(self):
        numero_conta = int(input("Digite o número da conta: "))
        senha = input("Digite a senha: ")

        self.conta_autenticada = self.conta_use_cases.autenticar_conta(numero_conta, senha)

        if self.conta_autenticada:
            print("\nAutenticação bem-sucedida!")
        else:
            print("\nCredenciais inválidas. Tente novamente.")

    def sacar(self):
        if self.conta_autenticada:
            valor = float(input("Digite o valor que deseja sacar: "))
            sucesso, saldo_atual = self.conta_use_cases.sacar(self.conta_autenticada, valor)
            if sucesso:
                print(f"Saque realizado com sucesso. Saldo atual: {saldo_atual}")
            else:
                print("Saldo insuficiente.")

    def depositar(self):
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        if valor_deposito > 0:
            self.conta_autenticada.saldo += valor_deposito
            self.conta_use_cases.atualizar_conta(self.conta_autenticada)
            print(f"Depósito de {valor_deposito:.2f} realizado com sucesso.")
        else:
            print("Valor inválido.")

    def exibir_extrato(self):
        print("\nExtrato:")
        print(f"Saldo atual: {self.conta_autenticada.saldo:.2f}")
        print(f"Número de saques realizados: {self.conta_autenticada.saques}")
        print("Histórico de transações:")

        if self.conta_autenticada.transacoes:
            print("\nHistórico de transações:")
            for idx, transacao in enumerate(self.conta_autenticada.transacoes, start=1):
                print(f"{idx}. Tipo: {transacao.tipo}, Valor: {transacao.valor:.2f}, Data: {transacao.data}")
        else:
            print("\nNenhuma transação registrada.")

    @staticmethod
    def exibir_menu_cliente_autenticado():
        print('\nMenu Cliente')
        print('1 - Sacar')
        print('2 - Depositar')
        print('3 - Extrato')
        print('4 - Sair')

    def executar(self):
        while True:
            if not self.conta_autenticada:
                self.autenticar_cliente()
                if not self.conta_autenticada:
                    continue

            self.exibir_menu_cliente_autenticado()
            opcao = int(input('Digite o número da operação desejada: '))

            if opcao == 1:
                self.sacar()
            elif opcao == 2:
                self.depositar()
            elif opcao == 3:
                self.exibir_extrato()
            elif opcao == 4:
                self.conta_autenticada = None  # Deslogar
                print("Você saiu da sua conta.")
            else:
                print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    from app.domain.use_cases.conta_use_cases import ContaUseCases

    # Inicialize o banco de dados e a sessão aqui, como feito no main.py
    initialize_db()
    session = get_session()
    conta_use_cases = ContaUseCases(session)

    menu_cliente = MenuCliente(conta_use_cases)
    menu_cliente.executar()
