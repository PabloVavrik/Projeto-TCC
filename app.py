from flask import Flask, request, redirect, render_template, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "chave_secreta"

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'pabu123',
    database = 'natacao'
)

cursor = conexao.cursor()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/competidor", methods=['POST'])
def criar_competidor():
    nome = request.form['nome']
    idade = request.form['idade']
    modalidade = request.form['modalidade']

    sql = "INSERT INTO competidores (nome, idade, modalidade) VALUES (%s, %s, %s)" 
    valores = (nome, idade, modalidade)

    cursor.execute(sql, valores)
    conexao.commit()

    flash("Competidor cadastrado com sucesso!") #Esse flash é responsável por guardar uma mensagem durante a sessão do usuário
                                                #Ele é puxado la no HTML, a partir da linha 16

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)