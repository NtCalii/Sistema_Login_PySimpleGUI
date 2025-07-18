from sqlalchemy import Column, Integer, String
from bd import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(100), nullable=False)
    email = Column("email", String(100), nullable=False)
    senha = Column("senha", String, nullable=False)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha =senha
