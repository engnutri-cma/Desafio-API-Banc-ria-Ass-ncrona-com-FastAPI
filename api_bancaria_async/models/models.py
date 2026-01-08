from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Enum
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.sql import func
from typing import List
from enum import Enum as PyEnum

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    metadata = None  # Para Alembic

class TipoTransacao(str, PyEnum):
    DEPOSITO = "deposito"
    SAQUE = "saque"

class Account(Base):
    __tablename__ = "contas"
    
    id = Column(Integer, primary_key=True, index=True)
    agencia = Column(String(10), nullable=False)
    numero = Column(String(20), unique=True, index=True, nullable=False)
    saldo = Column(Float, default=0.0, nullable=False)
    
    # Relacionamento 1:N com transações
    transacoes = relationship("Transaction", back_populates="conta", cascade="all, delete-orphan")

class Transaction(Base):
    __tablename__ = "transacoes"
    
    id = Column(Integer, primary_key=True, index=True)
    conta_id = Column(Integer, ForeignKey("contas.id"), nullable=False)
    tipo = Column(Enum(TipoTransacao), nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relacionamento N:1 com conta
    conta = relationship("Account", back_populates="transacoes")


