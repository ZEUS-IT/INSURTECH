from pydantic import BaseModel

# Registro y Login
class UsuarioCreate(BaseModel):
    email: str
    password: str

class UsuarioLogin(BaseModel):
    email: str
    password: str

# Crear póliza (desde el frontend)
class PolizaCreate(BaseModel):
    aseguradora: str
    numero: str
    vencimiento: str  # Formato: "2025-12-31"

# Póliza completa (respuesta del backend)
class PolizaOut(BaseModel):
    id: int
    aseguradora: str
    numero: str
    vencimiento: str
    usuario_email: str

    class Config:
        orm_mode = True


