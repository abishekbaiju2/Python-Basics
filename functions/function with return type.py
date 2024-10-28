# return : stores the data
# print : output to the console

# def add(a,b):
#     return  a+b
# print(add(1,2))

# find a number is odd or even using fn with return type?

# def oe(a):
#     if a%2==0:
#         c='even'
#     else:
#         c='odd'
#     return c
# print(oe(2))

# find the largest of 3 numbers?

# def largest(a,b,c):
#     if(a>b and a>c):
#         f=a
#     elif(b>c):
#         f=b
#     else:
#         f=c
#     return f
# print(largest(3,5,7))

# check a number disarium?

# def disarium(a):
#     t=a
#     sum=0
#     for i in range(len(str(a)),0,-1):
#         rem=a%10
#         sum+=rem**i
#         a//=10

#     if sum==t:
#         f='disarium'
#     else:
#         f='not disarium'
#     return f
# print(disarium(135))

# create a fn list_elements_square() and pass a list as an arg and return a list that contains square of each values?

# def list_elements_square(li):
#     li1=[]
#     for i in li:
#         li1+=[i**2]
#     return li1
# print(list_elements_square([1,2,3]))

# pass a list into fn and return a list that contains the revers of each numbers ?

# def reverse(li):
#     li1=[]
#     for i in li:
#         rev=0
#         while(i!=0):
#             rem=i%10
#             rev=rev*10+rem
#             i//=10
#         li1+=[rev]
#     return li1
# print(reverse([123,456,876]))

# write a fn unique_chars(s) that returns a list of unique characters in a string ?

# def unique_chars(s):
#     li1=[]
#     for i in s:
#         if s.count(i)==1:
#             li1+=[i]
#     return li1
# print(unique_chars('hello'))

# pass any number of strings into fn and return a dictionary that contains string and its revers as value ?

# def dic(d):
#     s={}
#     for i in d:
#         s[i]=i[::-1]
#     return s
# print(dic(['hello','hai']))

#write a python fn to pass list of numbers and return the even numbers from the given list ?

# def even(li):
#     li1=[]
#     for i in li:
#         if i%2==0:
#             li1+=[i]
#     return li1
# print(even([1,3,5680,2,5,6,8,9]))

# quadratic

# def quad(a,b,c):
#     e = (b ** 2 - (4 * a * c)) ** 0.5
#     x1=(-b+e)/2*a
#     x2=(-b-e)/2*a
#     return x1,x2
# q=1
# for i in quad(1,5,6):
#     print(f'x{q} = {i}')
#     q+=1

#or

# def quad(a,b,c):
#     e = (b ** 2 - (4 * a * c)) ** 0.5
#     x1=(-b+e)/2*a
#     x2=(-b-e)/2*a
#     return x1,x2
# x=quad(1,5,6)
# print('x1 =',x[0])
# print('x2 =',x[1])




