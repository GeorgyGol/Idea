#!/usr/bin/python
# -*- coding: utf-8 -*-
#import mysql.connector
#conn = mysql.connector.connect(host='127.0.0.1', database='Test', user='test_user', password='testpass')
"""
import pymysql, settings


database=settings.DATABASES['default']['NAME']
datauser=settings.DATABASES['default']['USER']
userpass=settings.DATABASES['default']['PASSWORD']
datahost='127.0.0.1'

def readUserDB():
    pymysql.install_as_MySQLdb()
    conn = pymysql.connect(host=datahost, database=database, user=datauser, password=userpass)
    mycursor = conn.cursor()
    '''
    mycursor.execute('SELECT * FROM Test.Users')
    result = mycursor.fetchall()

    outp=''
    for (Id, Name, EMail) in result:
        outp+= "Name={1}, Id={0}, EMail={2}<BR/>".format(Id, Name, EMail) 
    
    conn.close
    '''
    return ''

def readUserDB_list():
    pymysql.install_as_MySQLdb()
    conn = pymysql.connect(host=datahost, database=database, user=datauser, password=userpass)
    mycursor = conn.cursor()
    mycursor.execute('SELECT * FROM Test.Users')
    result = mycursor.fetchall()
    conn.close
    return result
    #outp=list()
    
    #for r in result:
    #    outp.append(r) 
    
    
    #return outp

#print (readUserDB_list())
readUserDB()
'''
u_l=readUserDB_list()
for u in u_l:
    print(u[0], u[1], u[2])
''' 
"""