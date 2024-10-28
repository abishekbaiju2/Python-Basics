from gettext import install
from itertools import count

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

# from multipledispatch import dispatch
#
# class maths:
#     @dispatch(int,int)
#     def add(self,a,b):
#         print(a+b)
#     @dispatch(int,int,int)
#     def add(self,a,b,c):
#         print(a+b+c)
#
# x=maths()
# x.add(2,3)
# x.add(1,2,3)

from multipledispatch import dispatch
class length:
    @dispatch(int)
    def ln(self,num):
        if num == 0:
            count = 1
        else:
            count = 0
            num = abs(num)
            while num > 0:
                num //= 10
                count += 1
        print(count)
    @dispatch(list)
    def ln(self,lst):
        count = 0
        for i in lst:
            count += 1
        print(count)
    @dispatch(dict)
    def ln(self,dct):
        count = 0
        for i in dct:
            count += 1
        print(count)
    @dispatch(str)
    def ln(self,st):
        count=0
        for i in st:
            count+=1
        print(count)
    @dispatch(set)
    def ln(self,se):
        count=0
        for i in se:
            count+=1
        print(count)
    @dispatch(tuple)
    def ln(self,tp):
        count=0
        for i in tp:
            count+=1
        print(count)

k=length()
k.ln({'A':2,'B':4,'C':5})
k.ln([1,2,34,4])
k.ln(16894)
k.ln('asdcsdff')
k.ln({1,2,6,8,3})
k.ln((1,5,3,8,5))

    # what is a decorator ?
# extend a function without any modification
