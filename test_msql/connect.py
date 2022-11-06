import pymysql

# def get_con():
conn = pymysql.connect(
        host="172.16.0.101",
        user="root",
        password="111111",
        port=3306
    )
cursor =conn.cursor()
cursor.execute("select version()")
vers=cursor.fetchone()
print(vers)
conn.close()




