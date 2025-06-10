# app/main.py
from fastapi import FastAPI
from app.api import routes_user, routes_role
from app.core.database import Base, engine
from app.monitoring.exporter import start_monitoring


# Crea las tablas en la base de datos (si no existen)
Base.metadata.create_all(bind=engine)
# start_monitoring()


app = FastAPI(
    title="FastAPI Users & Roles API",
    description="Manejo de usuarios y roles conectados a SQL Server",
    version="1.0.0"
)

# Incluir routers definidos en la API
app.include_router(routes_user.router)
app.include_router(routes_role.router)
