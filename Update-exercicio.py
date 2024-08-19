import mysql.connector
from mysql.connector import Error

# Atualizar registros em um banco de dados MySQL

def conectar():
    try:
        global con
        con = mysql.connector.connect(host='localhost',database='db_Biblioteca', user='root', password='')
    except Error as erro:
        print("Erro de conexão.")

def consulta(idProd):
    try:
        conectar()
        consulta_sql = 'select * from tbl_produto where IdProduto = ' + idProd
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print("Id: ", linha[0])
            print("Produto: ", linha[1])
            print("Preço: ", linha[2])
    except Error as erro:
        print("Falha ao consultar a tabela: {}".format(erro))
    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()

def atualiza(declaracao):
    try:
        conectar()
        altera_preco = declaracao
        cursor = con.cursor()
        cursor.execute(altera_preco)
        con.commit()
        print("Preço alterado com sucesso.")
    except Error as erro:
        print("Falha ao inserir dados na tabela: {}".format(erro))
    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()

if __name__=='__main__':

    print("Atualizar preço de produtos no banco de dados.")
    print("Entre com os dados conforme solicitado:")
    
    print("\nDigite o código do produto a alterar: ")
    idProd = input("Id do Produto: ")

    consulta(idProd)

    print("\nEntre com o novo preço do produto: ")
    precoProd = input("Preço: ")

    declaracao = """ update tbl_produtos
    set Preco = """ + precoProd + """
    where IdProduto = """ + idProd

    print(declaracao)

    # Executar o UPDATE no banco de dados....
    atualiza(declaracao)

    verifica = input("\nDeseja consultar a atualização ? s = sim, n = não\n")
    if(verifica == 's'):
        consulta(idProd)
    else:
        print("\nAté mais")
