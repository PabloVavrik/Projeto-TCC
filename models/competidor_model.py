from models.db import get_conexao


def criar_competidor(nome, idade, modalidade):

    conexao = get_conexao()
    cursor = conexao.cursor()

    sql = "INSERT INTO competidores (nome, idade, modalidade) VALUES (%s, %s, %s)" 
    valores = (nome, idade, modalidade)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

def retornar_competidores():

    conexao = get_conexao()
    cursor = conexao.cursor(dictionary=True)

    sql = "SELECT * FROM competidores"
    cursor.execute(sql)

    competidores = cursor.fetchall()

    cursor.close()
    conexao.close()

    return competidores

def deletar_competidor(id):
    conexao = get_conexao()
    cursor = conexao.cursor()

    sql = "DELETE FROM competidores WHERE id = %s"
    cursor.execute(sql, (id,))
    conexao.commit()
    
    cursor.close()
    conexao.close()

def atualizar_competidor(id, nome, idade, modalidade):
    
    conexao = get_conexao()
    cursor = conexao.cursor()

    sql = """
        UPDATE competidores
        SET nome = %s, idade = %s, modalidade = %s
        WHERE id = %s
    """

    valores = (nome, idade, modalidade, id)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()