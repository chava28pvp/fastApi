from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus


SQLALCHEMY_DATABASE_URL = (
    "mssql+pyodbc:///?odbc_connect="
    + quote_plus(
        "DRIVER=ODBC Driver 17 for SQL Server;"
        "SERVER=GAMEZ28\\SQLEXPRESS;"
        "DATABASE=UsuariosConnection;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
