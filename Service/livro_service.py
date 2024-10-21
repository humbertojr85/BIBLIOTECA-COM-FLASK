from Repository.livro_repository import LivroRepository
from Entity.livro import Livro
from Exception.livro_exception import LivroNaoEncontradoException

class LivroService:
    def __init__(self):
        self.livro_repository = LivroRepository()

    def listar_livros(self):
        return self.livro_repository.listar_todos()

    def adicionar_livro(self, dados):
        novo_livro = Livro(
            titulo=dados.get("titulo"),
            autor=dados.get("autor"),
            ano_publicacao=dados.get("ano_publicacao")
        )
        self.livro_repository.salvar(novo_livro)
        return novo_livro

    def editar_livro(self, id, dados):
        livro = self.livro_repository.buscar_por_id(id)
        if not livro:
            raise LivroNaoEncontradoException()

        livro.titulo = dados.get("titulo")
        livro.autor = dados.get("autor")
        livro.ano_publicacao = dados.get("ano_publicacao")
        self.livro_repository.atualizar()
        return livro

    def excluir_livro(self, id):
        livro = self.livro_repository.buscar_por_id(id)
        if not livro:
            raise LivroNaoEncontradoException()
        self.livro_repository.excluir(livro)
