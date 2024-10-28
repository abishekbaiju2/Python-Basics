# positional arguments

# def mult(a,b):
#     print(a*b)
# mult(2,3)

# default argument

# def add(a,b,c=0):
#     print(a+b+c)
# add(1,2)
# add(1,2,3)

# create a product using default argument ?

def prdt(a,b,c=1,d=1):
    print(a*b*c*d)
prdt(1,2)
prdt(1,2,3)
prdt(1,5,4,3)

# arbitrary argument
# stored data type as tuple

def values(*args):
    print(args)
values(1,2,3,4,5,6,7,8,9)

# create a function add that passes any number of arguments ?

# def add(*args):
#     a=0
#     for i in args:
#         a+=i
#     print(a)
# add(1,2,3,4)

# create a function that multiplies any number of args ?

# def prdt(*args):
#     a=1
#     for i in args:
#         a*=i
#     print(a)
# prdt(1,2,3,4)

# create a fn min to find the min value passing into a fn?

# def values(*args):
#     t=args[0]
#     for i in args:
#         if i<t:
#             t=i
#     print(t)
# values(9,7,6,4,5,3)

# create a fn max to find the max value passing into a fn?

# def values(*args):
#     t=args[0]
#     for i in args:
#         if i>t:
#             t=i
#     print(t)
# values(7,6,4,3,9)

# keyword argument

# def add(a,b):
#     print(a+b)
# add(b=2,a=1)

# def person(name,email,phone,address):
#     print(name,email,phone,address)
# person(name='ak',phone=375875,address='uyguyufgug',email='ak@gmail.com')

# arbitrary keyword argument
# stores as dictionary

# def values(**kwargs):
#     print(kwargs)
# values(id=1,name='alex')

# can print list

# def list_sum(li):
#     print(li)
# list_sum([1,2,3,4])







