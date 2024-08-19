import mysql.connector

try:
    # Criar conexão ao banco e dados
    con = mysql.connector.connect(host='localhost',database='db_Biblioteca',
                                  user='root', password='')
    # Declaração SQL a ser executada
    criar_tabela_SQL = """create table tbl_produtos(
                             IdProduto int(11) not null,
                             NomeProduto varchar(70) not null,
                             Preco float not null,
                             Quantidade tinyint not null,
                             primary key (IdProduto)"""    
    # Criar cursor e executar SQL no Banco de Dados
    cursor = con.cursor()
    cursor.execute(criar_tabela_SQL)
    print("Tabela de Produto criada com sucesso !")
except mysql.connector.Error as erro:
    print("Falha ao criar tabela no MySQL: {}".format(erro))
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi finalizada")
print("\n Próxima aula: Inserção de Registro na tabela criada.")
 
