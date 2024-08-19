import pymysql.cursors
# Abrir uma conexão a um banco de dados....
con = pymysql.connect(host='localhost',user='root',database='db_biblioteca', password='',cursorclass=pymysql.cursors.DictCursor)

# Preparar um cursor com o método .cursor()
with con.cursor() as c:
    # Criar uma consulta
    sql = "select NomeLivro, ISBN13 from tbl_livro where IdLivro = 104"
    c.execute(sql)
    res = c.fetchone()
    print(res)
    print()
    print("Livro Retornado: ",res['NomeLivro'])

    #Outra consulta: dados da tabela de editoras
    sql = "select NomeEditora from tbl_editoras"
    c.execute(sql)
    res = c.fetchall()
    print("\n",res)
    print()
    for linha in res:
        print(linha['NomeEditora'])
        
con.close()
