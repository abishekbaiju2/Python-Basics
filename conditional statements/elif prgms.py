#syntax

# if(condition):
#     #body of if
# elif (condition):
# body of elif
# elif (condition):
# body of elif
# .......
# .......
# else:
# body of else

# check a number is positive negative or zero using conditional statement ?

num=int(input('enter the number'))
if(num == 0):
    print(f'{num} is zero')
elif(num > 0):
    print(f'{num} is positive')
else:
    print(f'{num} is negative')

# largest of three number?

a=int(input('enter the first number'))
b=int(input('enter the second number'))
c=int(input('enter the thrid number'))
if(a>b and a>c):
    print(f'{a} is largest')
#second condition only to check b>c becz 1st condition fails so a is small
elif(b>c):
    print(f'{b} is largest')
else:
    print(f'{c} is largest')

#find largest of 4 numbers

a=int(input('enter the first number'))
b=int(input('enter the second number'))
c=int(input('enter the third number'))
d=int(input('enter the fourth number'))
if(a>b and a>c):
    print(f'{a} is largest')
elif(b>c and b>d):
    print(f'{b} is largest')
elif(c>d):
    print(f'{c} is largest')
else:
    print(f'{d} is largest')

#min of 5 numbers?

a=int(input('enter the first number :'))
b=int(input('enter the second number :'))
c=int(input('enter the third number :'))
d=int(input('enter the fourth number :'))
e=int(input('enter the fifth number :'))
if(a < b and a < c):
    print(f'{a} is min')
elif(b < c and b < d):
    print(f'{b} is min')
elif(c < d and c < e):
    print(f'{c} is min')
elif(d < e):
    print(f'{d} is min')
else:
    print(f'{e} is min')

# accept any city from the user and display monument of that city?

city=input('enter the city :')
if (city=='delhi'):
    print(f'red fort')
elif(city=='agra'):
      print('taj mahal')
elif(city=='jaipur'):
    print('jal mahal')
else:
    print('invalid')

# grading system

n=int(input('enter the grade :'))
if(n>=91 and n<=100):
    print('A+')
elif(n>=81 and n<=90):
    print('A')
elif (n >= 71 and n <= 80):
    print('B+')
elif (n >= 61 and n <= 70):
    print('B+')
elif (n >= 51 and n <= 60):
    print('B')
elif (n >= 41 and n <= 50):
    print('C+')
elif (n >= 31 and n <= 40):
    print('C')
else:
    print('failed')

#write a prgm to accept the cost price of the bike and display the road tax to be paid according to the following criteria ?

n=int(input('enter the amount of bike :'))
if(n>100000):
    print("tax amount is:",n*15/100)
elif(n>50000 and n<=100000):
    print("tax amount is:", n * 10 / 100)
else:
    print("tax amount is:", n * 5 / 100)

# a company decide to give bonus to employees according to following criteria
#  time period of service        bonus
#    more than 10 years            10%
#    >=6 and <=10                  8%
#    less than 6 years             5%
#   ask user for their salary and year of service and print net bonus amount

salary=float(input('enter your salary : '))
year=int(input('enter your year of service :'))
if(year>=10):
    print('bouns amount : ',salary*10/100)
elif(year>=6 and year<=10):
    print('bouns amount : ',salary*8/100)
else:
    print('bouns amount : ',salary*5/100)

