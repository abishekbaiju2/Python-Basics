import mysql.connector


dbconnect=mysql.connector.connect(host='localhost',user='root',password='password@123',database='products')

mycursor=dbconnect.cursor()

sql='create table product_data(id int auto_increment primary key , product_name varchar(50),price int)'

mycursor.execute(sql)

dbconnect.commit()

print('table create successfully')