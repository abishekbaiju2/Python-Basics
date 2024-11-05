import mysql.connector

dbconnect=mysql.connector.connect(host='localhost',user='root',password='password@123')
# create cursor object
#  it is used to execute sql commands and also to fetch datas in mysql

mycursor=dbconnect.cursor()

sql='create database products'

mycursor.execute(sql)

dbconnect.commit()

print('database created successfully...')
