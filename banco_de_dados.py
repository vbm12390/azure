import mysql.connector
from conexoes import config

def banco():
    mydb = mysql.connector.connect(**config)

    dado = "INSERT INTO teste values(default, 'teste')"

    cursor = mydb.cursor()
    cursor.execute(dado)
    mydb.commit()
    mydb.close()