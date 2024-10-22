 # syntax:

# class class_name :
    # body of class

class first :
    def hello(self):
        print('welcome to oops')

x=first() # when class call then use fn bracket
# x is known as reference variable
x.hello()

# create a class calculator with 4 method add sub mult div that passes 2 arguments?

class calculator :
    def add(self,a,b):
        print(a+b)
    def prdt(self,a,b):
        print(a*b)
    def sub(self,a,b):
        print(a-b)
    def div(self,a,b):
        print(a/b)

f=calculator()
f.prdt(1,2)
f.sub(3,1)
f.div(6,3)
f.add(3,5)