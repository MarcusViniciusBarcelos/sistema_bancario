# app/domain/use_cases/conta_use_cases.py
from datetime import datetime

from sqlalchemy.orm import Session
from app.domain.models.cliente import Cliente
from app.domain.models.transacao import Transacao
from app.domain.repositories.conta_repository import ContaRepository


class ContaUseCases:
    def __init__(self, session: Session):
        self.conta_repository = ContaRepository(session)

    def cadastrar_conta(self, cliente, senha):
        return self.conta_repository.create(cliente, senha)

    def listar_contas(self):
        return self.conta_repository.read_all()

    def buscar_conta_por_id(self, conta_id):
        return self.conta_repository.read_by_id(conta_id)

    def atualizar_conta(self, conta):
        self.conta_repository.update(conta)

    def excluir_conta(self, conta):
        self.conta_repository.delete(conta)

    def autenticar_conta(self, numero_conta, senha):
        conta = self.conta_repository.read_by_numero_conta(numero_conta)

        if conta and conta.senha == senha:
            return conta
        else:
            return None

    def sacar(self, conta, valor):
        if 0 < valor <= conta.saldo:
            conta.saldo -= valor
            conta.saques += 1
            transacao = Transacao(valor=-valor, data=datetime.now(), conta=conta, tipo="Saque")
            self.conta_repository.session.add(transacao)
            self.conta_repository.session.flush()
            conta.transacoes.append(transacao)
            self.conta_repository.update(conta)
            return True, conta.saldo
        else:
            return False, conta.saldo

    def depositar(self, conta, valor):
        if valor > 0:
            conta.saldo += valor
            transacao = Transacao(valor=valor, data=datetime.now(), conta=conta, tipo="Depósito")
            self.conta_repository.session.add(transacao)
            self.conta_repository.session.flush()
            self.conta_repository.update(conta)
            return True, conta.saldo
        else:
            return False, conta.saldo

    @staticmethod
    def extrato(conta):
        return conta.transacoes
