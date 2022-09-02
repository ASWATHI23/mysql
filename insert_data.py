import mysql.connector


conn = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',database='mysql')


cursor = conn.cursor()


sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)VALUES('ASWATHI','SURENDRAN',21,'F',20000)"""

try:
    cursor.execute(sql)
    conn.commit()
    print("Data Inserted")
except:
    conn.rollback()
conn.close()
