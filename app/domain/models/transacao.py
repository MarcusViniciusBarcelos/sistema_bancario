# app/domain/models/transacao.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.persistence.database import Base
from datetime import datetime


class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    valor = Column(Integer)
    data = Column(DateTime)
    conta_id = Column(Integer, ForeignKey("contas_bancarias.id"))

    conta = relationship("ContaBancaria", back_populates="transacoes")

    def __init__(self, tipo, valor, data, conta):
        self.tipo = tipo
        self.valor = valor
        self.data = data
        self.conta = conta
