import mysql.connector

conn = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',database='mysql')
cursor = conn.cursor()
print("contents of the table:")
cursor.execute("SELECT * from EMPLOYEE")
print(cursor.fetchall())
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (25)

try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()
print("Contents of the table after delete operation")
cursor.execute("SELECT * from EMPLOYEE")
print(cursor.fetchall())
conn.close()

