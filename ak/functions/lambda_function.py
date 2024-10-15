from functools import reduce
# syntax :
# x = lambda args: expression

# adding two numbers using lambda function ?

# x=lambda a,b: a+b
# print(x(1,2))

# find the square root of a number?

# x=lambda a:a**0.5
# print(x(4))

# find cube of an arqument ?

# h= lambda a:a**3
# print(h(3))

# find area of a circle ?

# f=lambda r: 3.14*(r**2)
# print(f(2))

# find area of a triangle ?

# c=lambda a,b: 0.5*a*b
# print(c(2,3))

#  conditions in lambda
# syntax:
# in if condition return value is infront of if and in else condition return value after that

# find the largest of two numbers

# x=lambda a,b : a if(a>b) else b
# print(x(3,4))

# or

# x=lambda a,b : f' {a} is greater ' if(a>b) else f'{b} is greater'
# print(x(3,4))

# using lambda find a number is odd or even ?

# v=lambda a: f"{a} is even"if (a%2==0) else f'{a} is odd'
# print(v(2))

# check a char entered by the user is vowel or not ?


# h=lambda a: f'{a} is a vowel' if (a in 'aeiouAEIOU') else f"{a} is not vowel"
# print(h(input('enter the char')))

# check a number is positive or negative ?

# g=lambda a:f"{a} is positive" if(a>0) else f'{a} is negative'
# print(g(-3))

# check a number is positive negative or zero using lambda?

# f=lambda a: f'{a} is positive' if(a>0) else(f'{a} is negative 'if(a<0) else f'{a} is zero')
# print(f(-4))

# find the largest of three numbers ?

# j=lambda a,b,c: f'{a} is largest' if(a>b and a>c) else (f'{b} is largest 'if(b>c) else f'{c} is largest')
# print(j(4,5,2))
# print(j(6,7,9))
# print(j(8,7,6))

# find the min of 5 numbers using lambda ?

# h=lambda a,b,c,d,e:f'{a} is min 'if(a<b and a<c and a<d and a<e) else(f'{b} is min 'if( b<c and b<d and b<e) else (f'{c} is min'if(c<d and c<e) else (f'{d} is min'if(d<e)else f'{e} is min')) )
# print(h(3,5,1,4,9))

# filter ()
#syntax:
# x= filter(lambda args: expression , sequence element )
# output have to mention the data type
# filter even numbers from the given list using lambda ?

# li=[1,2,3,4,5,6]
# x=filter(lambda i: i%2==0 ,li )
# print(list(x))

# or

# li=[1,2,3,4,5,6]
# x=list(filter(lambda i: i%2==0 ,li ))
# print(x)

# filter out alphabets ?

# g=eval(input('enter the numbers : '))
# f=list(filter(lambda i: str(i).isalpha(),g))
# print(f)

# filter out number which are divisible by 2 and 3 ?

# li=eval(input('enter the numbers : '))
# f=list(filter(lambda i: i%2==0 and i%3==0,li))
# print(f)

# input a string and filter out vowels ?

# g=eval(input('enter the numbers : '))
# h=list(filter(lambda i: i in 'aeiouAEIOU',g ))
# print(h)

# map()
# x= map(lambda args: expression , sequence element )

# find the square of each numbers in a given list ?

# li=[2,3,4,5,6]
# x=map(lambda i:i**2,li)
# print(list(x))

# covert only the first letter of each words to upper case?

# g=['hello','welcome']
# d=list(map(lambda i:i.capitalize(),g))
# print(d)

# print the reverse of each word in a list input by user using lambda ?

# l=['hello','hai']
# f=list(map(lambda i:i[::-1],l))
# print(f)

# reduce()
# syntax
# x=reduce(lambda arg: expression , sequence_name)
# from functools import reduce

from functools import reduce
# li=[1,2,3,4]
# x=reduce(lambda a,b:a+b,li)
# print(x)

# find the product of a list input by the user ?

# n=eval(input('enter the list'))
# x=reduce(lambda a,b:a*b,n)
# print(f' product is {x}')

# find the max value input by the user ?

# g=eval(input('enter the list'))
# f=reduce(lambda a,b:a if(a>b) else b,g)
# print(f'{f} is max')

# find the min value input by the user ?

# h=eval(input('enter the list'))
# d=reduce(lambda a,b: a if(a<b) else b,h)
# print(f'{d} is min')

