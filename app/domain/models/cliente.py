# app/domain/models/cliente.py
from sqlalchemy import (Column,
                        Integer,
                        String)
from sqlalchemy.orm import relationship
from app.persistence.database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    data_nascimento = Column(String)
    cpf = Column(String)
    endereco = Column(String)

    contas = relationship("ContaBancaria", back_populates="cliente")

    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
