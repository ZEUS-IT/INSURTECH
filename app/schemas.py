from pydantic import BaseModel
from datetime import date

class UsuarioCreate(BaseModel):
    email: str
    password: str

class UsuarioLogin(BaseModel):
    email: str
    password: str

class PolizaCreate(BaseModel):
    numero: str
    dni: str
    fecha_vencimiento: date
    monto: float
    tipo: str
    email_cliente: str
    patente: str
