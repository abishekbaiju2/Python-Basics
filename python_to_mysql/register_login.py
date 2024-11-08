import mysql.connector

rgconnect=mysql.connector.connect(host='localhost',user='root',password='password@123',database='website')


mycursor=rgconnect.cursor()

# sql='create database website'
#
# mycursor.execute(sql)
#
# rgconnect.commit()
#
# print('database created successfully...')


# sql='create table register(id int auto_increment primary key,name varchar(50),email varchar(50) unique,phone bigint unique , password varchar(50))'
#
# mycursor.execute(sql)
#
# rgconnect.commit()
#
# print('table create successfully')

