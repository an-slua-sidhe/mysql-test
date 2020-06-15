import os
import datetime
import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Ansluasidhe2',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'bob']
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({})".format(
            format_strings), list_of_names)
            
        connection.commit()

finally:
    connection.close()
