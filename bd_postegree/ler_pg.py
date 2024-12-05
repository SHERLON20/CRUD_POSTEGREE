import psycopg2

conn = psycopg2.connect(
    database= 'eskina',
    user= 'postgres',
    password='lelobarril2014',
    host= 'localhost',
    port = '1234',
)
cursor=conn.cursor()
produtos=[
    (5,'macarrão','alimentos',20.80),
    (6,'leite','alimentos',8.75),
]
for item in produtos:
    cursor.execute(
        '''
            INSERT INTO produtos(id,nome,categoria,preco)
            VALUES (%s,%s,%s,%s)
        ''',item
    )
conn.commit()
print("dados inseridos com sucesso!")
conn.close()