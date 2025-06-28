from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models, database
from app.routers import auth, polizas

# 🧱 Crear tablas en base de datos
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# 🌐 CORS para conexión con frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📦 Rutas de la API
app.include_router(auth.router)
app.include_router(polizas.router)


