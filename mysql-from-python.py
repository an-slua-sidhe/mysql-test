import os
import pymysql

connection = pymysql.connect(host='localhost',
                            user='root',
                            password='Ansluasidhe2',
                            db='Chinook')

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()