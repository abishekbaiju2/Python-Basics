from gettext import install


# class maths:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# x=maths()
# x.add(1,2,3)
# print(x)
# x.add(2,3)
# print(x)

# you achieve method overloading directly using multipledispatch we can achieve method  overloading
# multipledispatch : external package
# pip install multipledispatch

from multipledispatch import dispatch

class maths:
    @dispatch(int,int)
    def add(self,a,b):
        print(a+b)
    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(a+b+c)

x=maths()
x.add(2,3)
x.add(1,2,3)


# what is a decorator ?
# extend a function without any modification
