from DB.db import db
from app import app

# Inicializa o banco de dados e cria as tabelas
with app.app_context():
    db.create_all()
