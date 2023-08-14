# app/domain/use_cases/cliente_use_cases.py
from sqlalchemy.orm import Session
from app.domain.models.cliente import Cliente
from app.domain.repositories.cliente_repository import ClienteRepository


class ClienteUseCases:
    def __init__(self, session: Session):
        self.cliente_repository = ClienteRepository(session)

    def cadastrar_cliente(self, nome, data_nascimento, cpf, endereco):
        return self.cliente_repository.create(nome, data_nascimento, cpf, endereco)

    def listar_clientes(self):
        return self.cliente_repository.read_all()

    def buscar_clientes_por_id(self, cliente_id):
        return self.cliente_repository.read_by_id(cliente_id)

    def atualizar_cliente(self, cliente):
        self.cliente_repository.update(cliente)

    def excluir_cliente(self, cpf_cliente):
        cliente = self.cliente_repository.read_by_cpf(cpf_cliente)  # Buscar cliente por CPF
        if cliente:
            self.cliente_repository.delete(cliente)
            return True
        return False

    def buscar_cliente_por_cpf(self, cpf_cliente):
        return self.cliente_repository.read_by_cpf(cpf_cliente)

