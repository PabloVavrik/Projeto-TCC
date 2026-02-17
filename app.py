from flask import Flask, render_template
from controllers.competidor_controller import cadastrar_competidor, exibir_competidores


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








if __name__ == "__main__":
    app.run(debug=True)