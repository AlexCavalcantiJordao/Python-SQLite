import mysql.connector
from mysql.connector import Error
# Inserir 
print("Rotina para cadastro de produtos no banco de dados.")
print("Entre com os dados conforme solicitado.")

idProd = input("ID do Produto: ")
nomeProd = input("Nome do Produto: ")
precoProd = input("Preço: ")
quantidade = input("Quantidade: ")

dados = idProd + ',\'' + nomeProd + '\',' + precoProd + ',' + quantProd + ')'
declaracao = """insert into tbl_produtos
(IdProduto, NomeProduto, Preco, Quantidade) values("""
sql = declaracao + dados 

try:
    con = mysql.connector.connect(host='localhost',database='db_Biblioteca',
                                  user='root', password='')
    insert_produtos = sql
    cursor = con.cursor()
    cursor.execute(insert_produtos)
    con.commit()
    print(cursor.rowcount, "Registros inserido na tabela.")
except Error as erro:
    print("Falha ao inserir dados  no MySQL: {}".format(erro))
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL finalizada.")
