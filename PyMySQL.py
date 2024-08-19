# Como inserir registros em banco de dados MySQL com PyMySQL Python
import mysql.connector.django.base
#!pip install pymysql

# Import biblioteca

import pymysql
from Teste import res


#from Teste import linha, res


def conecta():
    global con
    con = pymysql.connect(
        host = 'localhost',
        user = 'root',
        database='db_biblioteca',
        password='',
        cursorclass=pymysql.cursors.DictCursor
    )

    def consulta_editora():
        conecta()

        with con.cursor() as c:
            sql = 'select * from tbl_editoras'
            c.execute(sql)

            # Método fecthall(): Retornar todas as linha obtidas pela consulta na tabela.....
            res = c.fetchall()
            print(res)
            print()

        # Mostrar os dados retornados, um por linha, iterando sobre o resultados.....
        for linha in res:
            print(f"Editora {linha['IdEditora']}: {linha['NomeEditora']}")

def consulta_autor():
    conecta()

with con.cursor() as c:
    sql = 'select * from tbl_autores'
    c.excute(sql)

    # Método fetchall(): retorno todas as linhas obtidas pela consultas na tabelas.....

# Mostrar os dados retornados, um por linhas, iterando sobre o resultados....
for linha in res:
    print(f"Autor: {linha['NomeAutor']} {linha['SobrenomeAutor']}")