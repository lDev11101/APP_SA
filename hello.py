import mysql.connector

print("Resultados de la Base de Datos")

cone = mysql.connector.connect(
    host="localhost", user="root", passwd="lunadev1230", db="world"
)

cur = cone.cursor()

cur.execute("SELECT * FROM world.city limit 10")
# for i in cur.fetchall():
#     if i[-1] > 1000000:
#         print(i)
for i in cur.fetchall():
    print(i)

cone.close()
