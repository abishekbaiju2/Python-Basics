import mysql.connector

dbconnect=mysql.connector.connect(host='localhost',user='root',password='password@123',database='products')

mycursor=dbconnect.cursor()

pr_name=input('enter the product name')
price=int(input('enter the price'))

sql=f'insert into product_data(product_name,price) values("{pr_name}",{price})'
# have to put quotes on string to wrk the code
#  have to check that quotes are different otherwise don't wrk

mycursor.execute(sql)

dbconnect.commit()

print(f'{pr_name} is added to table')
