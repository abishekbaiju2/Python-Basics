import mysql.connector

dbconnect=mysql.connector.connect(host='localhost',user='root',password='password@123',database='products')

mycursor=dbconnect.cursor()

sql='select * from product_data'

mycursor.execute(sql)

data=mycursor.fetchall()
#  to get all the datas from the table

# print(data)
# it return list of tuples

for i in data :
    print('id=',i[0],'product_name=',i[1],'price=',i[2])