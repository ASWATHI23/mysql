import mysql.connector


conn = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1')


cursor = conn.cursor()
cursor.execute("DROP database IF EXISTS MyDatabase")

sql = "CREATE database MYDATABASE"

cursor.execute(sql)

print("List of database:")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

conn.close()


