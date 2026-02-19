from flask import Flask, render_template, redirect, url_for
from controllers.competidor_controller import (
     cadastrar_competidor, 
     exibir_competidores, 
     deletar_competidor_controller
     )




app = Flask(__name__)
app.secret_key = "chave_secreta"


@app.route("/")
def home():
    return render_template("home.html")



@app.route("/competidor", methods=['POST'])
def criar():
        return cadastrar_competidor()



@app.route("/competidores")
def lista():
     return exibir_competidores()



@app.route("/deletar/<int:id>")
def deletar(id):
     return deletar_competidor_controller(id)



if __name__ == "__main__":
    app.run(debug=True)