from conexao_pg import conn
cursor= conn.cursor()
sql= '''
    DELETE FROM produtos
    WHERE nome = %s
'''
cursor.execute(sql,('macarrão',))
conn.commit()
print('dados excluidos!')
conn.close()

