import mysql.connector

rgconnect=mysql.connector.connect(host='localhost',user='root',password='password@123',database='website')

mycursor=rgconnect.cursor()

class website:

    def register_user(self,name,email,phone,password):
        self.name=name
        self.email=email
        self.phone=phone
        self.password=password
        sql=f'insert into register(name,email,phone,password) values("{self.name}","{self.email}",{self.phone},"{self.password}")'
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
                print('invalid user')

    def delete_user(self,email,password):
        print('deleted')
    # def user_display(self,email,password):


obj=website()

# obj.register_user('akhil','akhil@gmail.com',9988665533,'akhil123')
# obj.register_user('alex','alex@gmail.com',9877747474,'alex123')
# obj.register_user('arun','arun@gmail.com',424242352,'arun123')

# obj.login_user('akhil','akhil@gmail.com')
# obj.delete_user()