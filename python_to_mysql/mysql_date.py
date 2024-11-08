import mysql.connector


dbconnect=mysql.connector.connect(host='localhost',user='root',password='password@123',database='products')

mycursor=dbconnect.cursor()

# sql='alter table product_data add added_date date'
#
# mycursor.execute(sql)
# print('column added')

#date : yyyy - mm - dd

product_name=input('enter the product name')
add_date = input('enter the date ')

sql=f'update product_data set added_date="{add_date}" where product_name="{product_name}" '

mycursor.execute(sql)
dbconnect.commit()
print('table updated')