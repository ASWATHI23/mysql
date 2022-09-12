import mysql.connector

conn = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',database='mysql')

cursor = conn.cursor()
sql = '''SELECT * from DATA LIMIT 2'''
cursor.execute(sql)
result = cursor.fetchall()
print(result)
conn.close()
