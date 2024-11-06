import mysql.connector

dbconnect=mysql.connector.connect(host='localhost',user='root',password='password@123',database='products')

mycursor=dbconnect.cursor()

pr_name=input('enter the product name')
price=int(input('enter the price'))

sql=f'insert into product_data(product_name,price) values({pr_name},{price})'

mycursor.execute(sql)

dbconnect.commit()

print('data created successfully')