
# 6]check if a number is armstrong or not?

n=int(input('enter the number :'))
l=len(str(n))
t=n
sum=0
while(n!=0):
    rem=n%10
    sum+=rem**l
    n//=10
if(t==sum):
    print(f'{t} is a armstrong')
else:
    print(f'{t} is not a armstrong')

# 7] checkmif the number is disarium or not?

n=int(input('enter the number :'))
l=len(str(n))
t=n
sum=0
while(n!=0):
    rem=n%10
    sum+=rem**l
    n//=10
    l-=1
if(t==sum):
    print(f'{t} is a disarium')
else:
    print(f'{t} is not a disarium')

# 9] factorial of a number?

n=int(input('enter the number : '))
k=1
i=1
while(i<=n):
    k*=i
    i+=1
print(k)

# 10] print odd numbers between 1 and 20

for i in range(1,21):
    if(i%2==0):
        continue
    elif(i%2==1):
        print(i)

# 8]sum of even numbers?

n=int(input('enter the end limit :'))
i=1
sum=0
while(i<=n):
    if(i%2==0):
        sum+=i
    i+=1
print(sum)

# 4] sum of first n natural numbers ?

n=int(input('enter the number :'))
sum=0
i=1
while(i<=n):
    sum+=i
    i+=1
print(sum)

# 3] atm withdrawal ?

n=int(input('enter the amount : '))
if(n%100==0):
    print('transaction succes')
else:
    print('sorry, transaction not complete , plz input an amount divisible by 100')

# 1] simple calculator?

print(' 1] addition \n 2]subtraction \n 3]multiplication \n 4] division')
n=int(input('enter the number :'))
if(n<=4):
    first = float(input('enter the first number :'))
    second = float(input('enter the second number :'))
if (n == 1):
    print(f'{first} + {second} = {first + second}')
elif (n == 2):
    print(f'{first} - {second} = {first - second}')
elif (n == 3):
    print(f'{first} * {second} = {first * second}')
elif (n == 4):
    print(f'{first} / {second} = {first / second}')
else:
    print('invalid')

# 5] check if a number is palindrome ?

n=int(input('enter the number :'))
t=n
l=len(str(n))
rev=0
for i in range(l):
    rem=n%10
    rev=rev*10+rem
    n//=10
if(t==rev):
    print('the number is a palindrome:')
else:
    print('the number is not a palindrome')

# 2] bmi calculator ?

n=float(input('enter your weight :'))
m=float(input('enter your height:'))
bmi = (n/(m**2))
i=bmi
if(i<18.5):
    print('under weight')
elif(18.5<=i<24.9):
    print('overweight')
elif(25<=i>=30):
    print('overweight')
elif(i>=30):
    print('obese')