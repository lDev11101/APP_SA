import mysql.connector
from mysql.connector import errorcode

try:

    con = mysql.connector.connect(
        host="localhost", user="root", passwd="lunadev1230", db="world"
    )
    cur = con.cursor()

    cur.execute("SELECT * FROM world.city limit 10")
    for i in cur.fetchall():
        print(i)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("algo anda mal con la contraseña o usuario")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    con.close()
