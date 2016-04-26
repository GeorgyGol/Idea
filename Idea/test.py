#import mysql.connector
#conn = mysql.connector.connect(host='127.0.0.1', database='Test', user='test_user', password='testpass')

database='Test'
datauser='test_user'
userpass='testpass'
datahost='127.0.0.1'

import pymysql
pymysql.install_as_MySQLdb()
conn = pymysql.connect(host=datahost, database=database, user=datauser, password=userpass)

mycursor = conn.cursor()
mycursor.execute('SELECT * FROM Test.Users')
result = mycursor.fetchall()
for (Id,Name,Email) in result:
    print (Id)
    print (Name + '/' + Email)
    print (Email)
conn.close