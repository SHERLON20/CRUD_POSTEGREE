from conexao_pg import conn
cursor = conn.cursor()

sql = '''
    UPDATE produtos
    SET categoria = %s
    WHERE nome = %s
'''
cursor.execute(sql,('alimentos','feijão'))
conn.commit()
print('dados atualizados!')
conn.close()