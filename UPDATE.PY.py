import mysql.connector

conn = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',database='mysql')

cursor = conn.cursor()
sql = '''UPDATE DATA SET AGE = AGE + 1 WHERE CLASS = 'PYTHON' '''
try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()

sql = '''SELECT * from DATA'''
cursor.execute(sql)
print(cursor.fetchall())
conn.close()