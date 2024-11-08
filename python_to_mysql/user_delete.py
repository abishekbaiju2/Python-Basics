import mysql.connector

dbconnect=mysql.connector.connect(host='localhost',user='root',password='password@123',database='products')

mycursor=dbconnect.cursor()

n=input('enter the id')

sql='select * from product_data where id=%s'

mycursor.execute(sql,(n,))# indo annu nokkan vendi use cheyunnathu # params take string

result= mycursor.fetchone()

if result:
    sql='delete from product_data where id=%s'
    mycursor.execute(sql,(n,))
    print('id deleted')
else:
    print('id not found')

dbconnect.commit()
