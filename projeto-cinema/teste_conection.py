import mysql.connector

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        database='dbcinema',
        user='suporte',
        password='suporte'
    )
    print("Conexão bem-sucedida!")
    conn.close()
except mysql.connector.Error as e:
    print(f"Erro: {e}")