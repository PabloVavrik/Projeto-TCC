from flask import Flask, render_template, redirect, url_for
from controllers import competidor_controller



app = Flask(__name__)
app.secret_key = "chave_secreta"


@app.route("/")
def home():
    return render_template("home.html")



@app.route("/competidor", methods=['POST'])
def criar():
        return competidor_controller.cadastrar_competidor()



@app.route("/competidores")
def lista():
     return competidor_controller.exibir_competidores()



@app.route("/deletar/<int:id>")
def deletar(id):
     return competidor_controller.deletar_competidor_controller(id)



@app.route("/editar/<int:id>")
def editar_competidor(id):
     return competidor_controller.editar_competidor_controller(id)


@app.route("/atualizar/<int:id>", methods=['POST'])
def atualizar_competidor(id):
     return competidor_controller.atualizar_competidor_controller(id)


if __name__ == "__main__":
    app.run(debug=True)