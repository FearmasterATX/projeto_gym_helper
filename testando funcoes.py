import mysql.connector
nome = 'mario de andrade'

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Manteigaderretida76',
    database='registro_de_alunos'
)
cursor = banco.cursor()
comando_sql1 = 'select * from alunos;'
cursor.execute(comando_sql1)
dados_lidos = cursor.fetchall()
print(dados_lidos[1][0])
