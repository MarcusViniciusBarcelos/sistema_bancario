# app/interfaces/menu_admin.py
from app.domain.use_cases.cliente_use_cases import ClienteUseCases
from app.domain.use_cases.conta_use_cases import ContaUseCases


class MenuAdmin:
    def __init__(self, cliente_use_cases: ClienteUseCases, conta_use_cases: ContaUseCases):
        self.cliente_use_cases = cliente_use_cases
        self.conta_use_cases = conta_use_cases

    @staticmethod
    def exibir_menu():
        print('\nMenu Administrador')
        print('1 - Listar Contas')
        print('2 - Listar Clientes')
        print('3 - Cadastrar Cliente')
        print('4 - Cadastrar Conta')
        print('5 - Excluir Cliente')
        print('6 - Excluir Conta')
        print('7 - Atualizar Cliente')
        print('8 - Atualizar Conta')
        print('9 - Voltar')

    def listar_clientes(self):
        print('\nLista de Usuários:')
        clientes = self.cliente_use_cases.listar_clientes()
        for cliente in clientes:
            print(f'Nome: {cliente.nome} | CPF: {cliente.cpf} | Endereço: {cliente.endereco}')

    def listar_contas(self):
        print('\nContas Bancárias:')
        contas = self.conta_use_cases.listar_contas()
        for conta in contas:
            print(f'Agência: {conta.agencia} | Conta: {conta.numero_conta} | Cliente: {conta.cliente.nome}')

    def cadastrar_cliente(self):
        nome = input('Nome: ')
        data_nascimento = input('Data de Nascimento: ')
        cpf = input('CPF: ')
        logradouro = input("Digite o logradouro: ")
        numero = input("Digite o número: ")
        bairro = input("Digite o bairro: ")
        cidade_uf = input("Digite a cidade/UF: ")
        endereco = f"{logradouro}, {numero} - {bairro} - {cidade_uf}"
        novo_cliente = self.cliente_use_cases.cadastrar_cliente(nome, data_nascimento, cpf, endereco)
        print("\n=== Usuário cadastrado com sucesso ===\n")
        print(
            f"Nome: {novo_cliente.nome}\nData de Nascimento: {novo_cliente.data_nascimento}\nCPF: {novo_cliente.cpf}\n"
            f"Endereço: {novo_cliente.endereco}")

    def cadastrar_conta(self):
        cpf_cliente = input("Digite o ID do cliente: ")
        senha = input("Digite a senha da conta: ")

        cliente = self.cliente_use_cases.buscar_cliente_por_cpf(cpf_cliente)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        nova_conta = self.conta_use_cases.cadastrar_conta(cliente, senha)
        print("\n=== Conta cadastrada com sucesso ===\n")
        print(f"Agência: {nova_conta.agencia}\nNúmero da Conta: {nova_conta.numero_conta}\nCliente: {cliente.nome}")

    def excluir_cliente(self):
        cpf = input("Digite o CPF do usuário que deseja excluir: ")
        if self.cliente_use_cases.excluir_cliente(cpf):
            print("Usuário excluído com sucesso.")
        else:
            print("Usuário não encontrado.")

    def excluir_conta(self):
        numero_conta = int(input("Digite o número da conta que deseja excluir: "))
        if self.conta_use_cases.excluir_conta(numero_conta):
            print("Conta excluída com sucesso.")
        else:
            print("Conta não encontrada.")

    # Dentro da classe MenuAdmin

    def atualizar_cliente(self):
        cpf = input("Digite o CPF do cliente que deseja atualizar: ")
        cliente = self.cliente_use_cases.buscar_cliente_por_cpf(cpf)

        if cliente:
            print(f'Cliente encontrado: {cliente.nome} | CPF: {cliente.cpf}')
            novo_nome = input("Novo nome (deixe em branco para manter o mesmo): ")
            novo_endereco = input("Novo endereço (deixe em branco para manter o mesmo): ")

            if novo_nome:
                cliente.nome = novo_nome
            if novo_endereco:
                cliente.endereco = novo_endereco

            self.cliente_use_cases.atualizar_cliente(cliente)
            print("Cliente atualizado com sucesso.")
        else:
            print("Cliente não encontrado.")

    def atualizar_conta(self):
        numero_conta = int(input("Digite o número da conta que deseja atualizar: "))
        nova_senha = input("Digite a nova senha da conta: ")

        conta = self.conta_use_cases.buscar_conta_por_id(numero_conta)

        if conta is None:
            print("Conta não encontrada.")
            return

        conta.senha = nova_senha
        self.conta_use_cases.atualizar_conta(conta)
        print("Senha da conta atualizada com sucesso.")

    def executar(self):
        while True:
            self.exibir_menu()
            opcao = int(input('Digite o número da operação desejada: '))

            if opcao == 1:
                self.listar_contas()
            elif opcao == 2:
                self.listar_clientes()
            elif opcao == 3:
                self.cadastrar_cliente()
            elif opcao == 4:
                self.cadastrar_conta()
            elif opcao == 5:
                self.excluir_cliente()
            elif opcao == 6:
                self.excluir_conta()
            elif opcao == 7:
                self.atualizar_cliente()
            elif opcao == 8:
                self.atualizar_conta()
            elif opcao == 9:
                break

            else:
                print('Opção inválida. Tente novamente.')
