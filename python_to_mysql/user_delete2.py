import mysql.connector

dbconnect=mysql.connector.connect(host='localhost',user='root',password='password@123',database='products')

mycursor=dbconnect.cursor()

id=int(input('enter the id'))

sql='select * from product_data ' # complete data selection

mycursor.execute(sql)

result=mycursor.fetchall()

for i in result:
    if id==i[0]:
        sql=f'delete from product_data where id={id}'
        mycursor.execute(sql)
        print('id deleted')
        break
    else:
        print('id not found')

dbconnect.commit()