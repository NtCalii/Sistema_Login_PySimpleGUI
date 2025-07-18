from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///banco_usuarios.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()
