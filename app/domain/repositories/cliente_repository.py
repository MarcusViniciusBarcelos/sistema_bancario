# app/domain/repositories/cliente_repository.py
from sqlalchemy.orm import Session
from app.domain.models.cliente import Cliente


class ClienteRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, nome, data_nascimento, cpf, endereco):
        novo_cliente = Cliente(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
        self.session.add(novo_cliente)
        self.session.commit()
        return novo_cliente

    def read_all(self):
        return self.session.query(Cliente).all()

    def read_by_id(self, cliente_id):
        return self.session.query(Cliente).filter_by(id=cliente_id).first()

    def update(self, cliente):
        self.session.commit()

    def delete(self, cliente):
        self.session.delete(cliente)
        self.session.commit()

    def read_by_cpf(self, cliente_cpf):
        return self.session.query(Cliente).filter_by(cpf=cliente_cpf).first()
