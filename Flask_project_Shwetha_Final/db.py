import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='flask_db1',
        cursorclass=pymysql.cursors.DictCursor

    )