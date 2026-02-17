from flask import request, redirect, flash, render_template
from models.competidor_model import criar_competidor, retornar_competidores



def cadastrar_competidor():
    nome = request.form['nome']
    idade = request.form['idade']
    modalidade = request.form['modalidade']

    criar_competidor(nome, idade, modalidade)

    flash("Competidor cadastrado com sucesso!") #Esse flash é responsável por guardar uma mensagem durante a sessão do usuário
                                                #Ele é puxado la no HTML, a partir da linha 16
    return redirect("/")

def exibir_competidores():
    competidores = retornar_competidores()
    return render_template("lista_competidores.html", competidores = competidores)