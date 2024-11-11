import mysql.connector

rgconnect=mysql.connector.connect(host='localhost',user='root',password='password@123',database='website')

mycursor=rgconnect.cursor()

class website:

    def register_user(self,name,email,phone,password):
        sql=f'insert into register(name,email,phone,password) values("{name}","{email}",{phone},"{password}")'
        mycursor.execute(sql)
        rgconnect.commit()
        print('user registered')

    def login_user(self,email,password):
        sql='select email,password from register'
        mycursor.execute(sql)
        n = mycursor.fetchall()
        for i in n:
            if i[0]==email and i[1]==password:
                print('login successfully')
                break
            else:
                print('login failed')
                break

    def delete_user(self,email,password):
        sql = 'select email,password from register'
        mycursor.execute(sql)
        n = mycursor.fetchall()
        for i in n:
            if i[0]==email and i[1]==password:
                sql=f'delete from register where email="{email}" and password="{password}"'
                mycursor.execute(sql)
                rgconnect.commit()
                print('deleted')
                break
            else:
                print('invalid user')
                break

    def user_display(self,email,password):
        sql = 'select email,password from register'
        mycursor.execute(sql)
        n = mycursor.fetchall()
        for i in n:
            if i[0]==email and i[1]==password:
                sql = f'select * from register where email="{email}" and password="{password}"'
                mycursor.execute(sql)
                m = mycursor.fetchall()
                print(m)
                break
            else:
                print('invalid user')
                break




obj=website()

# obj.register_user('akhil','akhil@gmail.com',9988665533,'akhil123')
# obj.register_user('alex','alex@gmail.com',9877747474,'alex123')
# obj.register_user('arun','arun@gmail.com',424242352,'arun123')

# obj.login_user('akhil@gmail.com','akhil123')

obj.delete_user('akhil@gmail.com','akhil123')

# obj.user_display('akhil@gmail.com','akhil123')