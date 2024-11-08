import mysql.connector

dbconnect=mysql.connector.connect(host='localhost',user='root',password='password@123',database='products')

mycursor=dbconnect.cursor()

n=input('enter the product_name').strip()

sql=f'select product_name , price from product_data where product_name="{n}"'

mycursor.execute(sql)

data=mycursor.fetchone()

if data: # if data return then it is true
    print(' product_name=',data[0],'price=',data[1])
else:
    print('not found')