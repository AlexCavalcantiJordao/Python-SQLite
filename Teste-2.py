import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost',database='db_Biblioteca',
                                  user='root', password='')
    consulta_sql = "Select * from tbl_produtos"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linha = cursor.fetchall()
    print("Números total de registros retornados: ", cursor.rowcount)

    print("\nMostrando os auotres cadastrados.")
    for linha in linhas:
        print("Id do produto:", linha[0])
        print("Nome do produto:", linha[1])
        print("Preço:", linha[2], "\n")
        print("Quantidade:", linha[3], "\n")
except Error as e:
    print("Erro ao acessar tabela MySQL", e)
finally:
    if(con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão ao MySQL encerrada.")
