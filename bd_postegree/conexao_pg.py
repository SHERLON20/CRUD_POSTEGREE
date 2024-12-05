import psycopg2

conn = psycopg2.connect(
    database= 'eskina',
    user= 'postgres',
    password='lelobarril2014',
    host= 'localhost',
    port = '1234',
)