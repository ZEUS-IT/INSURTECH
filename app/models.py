from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Poliza(Base):
    __tablename__ = "polizas"

    id = Column(Integer, primary_key=True, index=True)
    aseguradora = Column(String, nullable=False)
    numero = Column(String, unique=True, nullable=False)
    vencimiento = Column(Date, nullable=False)
    usuario_email = Column(String, ForeignKey("usuarios.email"), nullable=False)



