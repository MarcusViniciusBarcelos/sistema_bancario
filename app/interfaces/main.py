from sqlalchemy.orm import sessionmaker

from app.persistence.database import (initialize_db,
                                      get_session)
from app.domain.use_cases.cliente_use_cases import ClienteUseCases
from app.domain.use_cases.conta_use_cases import ContaUseCases
from app.interfaces.menu_admin import MenuAdmin
from app.interfaces.menu_cliente import MenuCliente


def main():
    initialize_db()
    session = get_session()

    cliente_use_cases = ClienteUseCases(session)
    conta_use_cases = ContaUseCases(session)

    while True:
        print('\nBem-vindo ao meu sistema bancário')
        print('1 - Acessar como Cliente')
        print('2 - Acessar como Administrador')
        print('3 - Sair')
        opcao = int(input('Digite o número da opção desejada: '))

        if opcao == 1:
            menu_cliente = MenuCliente(conta_use_cases)
            menu_cliente.executar()
        elif opcao == 2:
            menu_admin = MenuAdmin(cliente_use_cases, conta_use_cases)
            menu_admin.executar()
        elif opcao == 3:
            break
        else:
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    main()
