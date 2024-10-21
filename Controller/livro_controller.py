from flask import Blueprint, request, jsonify
from Service.livro_service import LivroService
from Exception.livro_exception import LivroNaoEncontradoException

livro_blueprint = Blueprint('livros', __name__)

livro_service = LivroService()

@livro_blueprint.route("/", methods=["GET"])
def listar_livros():
    livros = livro_service.listar_livros()
    return jsonify([livro.to_dict() for livro in livros])

@livro_blueprint.route("/", methods=["POST"])
def adicionar_livro():
    dados = request.get_json()
    novo_livro = livro_service.adicionar_livro(dados)
    return jsonify(novo_livro.to_dict()), 201

@livro_blueprint.route("/<int:id>", methods=["PUT"])
def editar_livro(id):
    dados = request.get_json()
    try:
        livro_atualizado = livro_service.editar_livro(id, dados)
        return jsonify(livro_atualizado.to_dict())
    except LivroNaoEncontradoException:
        return jsonify({"erro": "Livro não encontrado"}), 404

@livro_blueprint.route("/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    try:
        livro_service.excluir_livro(id)
        return '', 204
    except LivroNaoEncontradoException:
        return jsonify({"erro": "Livro não encontrado"}), 404
