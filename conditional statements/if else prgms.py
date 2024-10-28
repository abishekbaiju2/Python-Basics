# syntax

# if(condition):
#     #body of if
# else:
#     #body of else

#find the largest of two numbers ?

a=int(input('enter the first number : '))
b=int(input('enter the second number : '))
if(a>b):
    print(f'largest number is {a}')
else:
    print(f'largest number is {b}')

# check a character input from the user is vowel or not?

char=input('enter the character : ')
if(char in 'aeiouAEIOU'):
    print(f'yes, {char} is a vowel ')
else:
    print(f'no, {char} is not a vowel ')

# find the smallest of two numbers ?

a=int(input('enter the first number : '))
b=int(input('enter the second number : '))
if(a<b):
    print(f'smallest number is {a}')
else:
    print(f'smallest number is {b}')

# check a number is even or not?

num=int(input("enter the number"))
if(num%2==0):
     print(f'{num} is even')
else:
    print(f'{num} is odd')

# check a number input by the user is positive or negative?

num=int(input("enter the number : "))
if(num>0):
    print(f'{num} is positive number')
else:
    print(f'{num} is negative number')

# voting eligibility , if the age is >=18,eligible for voting ,else not eligible for voting?

name=input('enter your name : ')
age=int(input(f' enter age of {name} : '))
if(age>=18):
    print(f'{name} eligible for voting')
else:
    print(f'{name} not eligible for voting')

# imple authentication , if the username is user  and password is pass , print authentication success , ele print authentication failed

name=input('enter username= ')
password=input('enter password=')
if (password=='pass' and name=='user'):
    print('authentication success')
else:
    print('authentication failed')

# check the number is divisible by both 2 and 3 ?

num=int(input('enter the number : '))
if(num%2==0 and num%3==0):
    print('the number is divisible by both 2 and 3')
else:
    print('the number is not divisible by both 2 and 3')

# check a number is a multiple of 5?

num=int(input('enter the number : '))
if (num % 5 == 0 ):
 print('number is a multiple of 5')
else:
     print('number is not a multiple of 5')

#check whether a day input by the user is weekday or weekend?

day=input('enter the day :')
if(day in ["mon",'tue','wed','thu','fri']):
    print(' day input by the user is weekday')
else:
    print(" day input by the user is weekend")

