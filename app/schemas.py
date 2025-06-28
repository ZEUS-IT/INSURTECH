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
class PolizaCreate(BaseModel):
    aseguradora: str
    numero: str
    vencimiento: str  # formato: "2025-12-31"

class PolizaOut(BaseModel):
    id: int
    aseguradora: str
    numero: str
    vencimiento: str
    usuario_email: str

    class Config:
        orm_mode = True

