from flask import Flask
from Controller.livro_controller import livro_blueprint

app = Flask(__name__)
app.config.from_object('config')

# Registra o blueprint do controlador de livros
app.register_blueprint(livro_blueprint, url_prefix="/livros")

if __name__ == "__main__":
    app.run(debug=True)