from Entity.livro import Livro
from DB.db import db

class LivroRepository:
    def listar_todos(self):
        return Livro.query.all()

    def buscar_por_id(self, id):
        return Livro.query.filter_by(id=id).first()

    def salvar(self, livro):
        db.session.add(livro)
        db.session.commit()

    def atualizar(self):
        db.session.commit()

    def excluir(self, livro):
        db.session.delete(livro)
        db.session.commit()
