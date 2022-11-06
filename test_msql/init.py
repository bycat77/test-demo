import pymysql

def get_conn():
    conn = pymysql.connect(
        host="172.16.0.101",
        user="root",
        password="123456",
        port=3306,
        database="hualong_uums"
    )

    return conn


