import mysql.connector

def get_conexao():
    conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'pabu123',
    database = 'natacao'
    )
    return conexao


    

#Este arquivo é responsável somente por fornecer a conexão com o BD. 