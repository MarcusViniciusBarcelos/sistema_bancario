# app/domain/repositories/conta_repository.py
from sqlalchemy.orm import Session
from app.domain.models.conta import ContaBancaria


class ContaRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, cliente, senha):
        nova_conta = ContaBancaria(cliente=cliente, senha=senha)
        self.session.add(nova_conta)
        self.session.commit()
        return nova_conta

    def read_all(self):
        return self.session.query(ContaBancaria).all()

    def read_by_id(self, conta_id):
        return self.session.query(ContaBancaria).filter_by(id=conta_id).first()

    def update(self, conta):
        self.session.commit()

    def delete(self, conta):
        self.session.delete(conta)
        self.session.commit()

    def read_by_numero_conta(self, numero_conta):
        return self.session.query(ContaBancaria).filter_by(numero_conta=numero_conta).first()
