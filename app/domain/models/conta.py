# app/domain/models/conta.py
from datetime import datetime
from sqlalchemy import (Column,
                        String,
                        Integer,
                        ForeignKey)
from sqlalchemy.orm import relationship

from app.domain.models.transacao import Transacao
from app.persistence.database import Base


class ContaBancaria(Base):
    __tablename__ = "contas_bancarias"

    id = Column(Integer, primary_key=True)
    agencia = Column(String)
    numero_conta = Column(Integer)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    senha = Column(String)
    saldo = Column(Integer)
    saques = Column(Integer)

    cliente = relationship("Cliente", back_populates="contas")
    transacoes = relationship("Transacao", back_populates="conta")

    def depositar(self, valor):
        self.saldo += valor
        self.registrar_transacao("Depósito", valor)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.saques += 1
            self.registrar_transacao("Saque", -valor)
        else:
            print("Saldo insuficiente.")

    def registrar_transacao(self, tipo, valor):
        transacao = Transacao(tipo=tipo, valor=valor, data=datetime.now(), conta=self)
        self.transacoes.append(transacao)

    num_conta = 1

    def __init__(self, cliente, senha):
        self.agencia = "0001"
        self.numero_conta = ContaBancaria.num_conta
        ContaBancaria.num_conta += 1
        self.cliente = cliente
        self.senha = senha
        self.saldo = 0
        self.saques = 0
