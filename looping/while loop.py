
# syntax
from os import remove

# while(condition):
    # body of while loop

# write a pgrm to print first 10 natural using while loop ?

i=1
while(i<10):
    print(i)
    i+=1

# write a pgrm to print 0 to 50 using while loop?

i=0
while(i<=50):
    print(i)
    i+=1

# print first 10 even numbers using while loop ?

i=2
while(i<=10):
    print(i)
    i+=2

#or

i=2
while(i<=10):
    if(i%2==0):
        print(i)
    i+=1

# print 5 odd numbers?

i=1
while(i<=5):
    print(i)
    i+=2

#or

i=1
while(i<=5):
    if(i%2==1):
        print(i)
    i+=2

# to print the sum of numbers fall in range 1 to 10

sum=0
i=1
while(i<=10):
    sum+=i
    i+=1
print(sum)

# write a pgrm to find the product of both even  and odd numbers fall in the range  1 to 10

i=1
e=1
o=1
while(i<=10):
    if(i%2==0):
        e*=i
    elif(i%2==1):
        o*=i
    i+=1
print(e)
print(o)

# write a pgrm to find the count of even and odd number fall in the range input by the user?

initial=int(input('enter the initial number : '))
final=int(input('enter the final  number : '))
e=0
o=0
i=initial
while(i<=final):
    if(i%2==0):
        e+=1
    elif(i%2==1):
        o+=1
    i+=1
print(e)
print(o)

# print first 10 natural number in reverse order ?

i=10
while(i>=1):
    print(i)
    i-=1

#multiplication table of a number input by the user ?

n=int(input('enter the number'))
i=1
while(i<=10):
    print(f'{n} * {i} = {n*i}')
    i+=1

# print the reverse of first 5 even numbers?

i=10
while(i>=1):
    if (i %2 ==0):
        print(i)
    i-=1

# write a prgm to print the first 10 integers and there square? 2 : 4

i=1
while(i<=10):
    print(f'{i} : {i**2}')
    i+=1

# find the factorial of a number input by the user ?

n=int(input('enter the number :'))
i=n
k=1
while(i>=1):
    k=k*i
    i-=1
print(f"factorial of {n} is = {k}")



# skip the numbers that a divisible by 11 fall in range 1100 ?

i=1
while(i<=100):
    if(i % 11 != 0):
        print(i)
    i+=1

#or

i=1
while(i<=100):
    if(i%11==0):
#have to increment in condition when skip is used
        i+=1
        continue
    else:
        print(i)
        i+=1

# write a prgm that sums all the multiple of 3  up to the give number n using while loop?

n=int(input('enter the number'))
i=3
s=0
while(i<=n):
    if(i%3==0):
        s+=i
    i+=1
print(s)


# count the total even number fall in the range input by the user ?

n=int(input('enter the number'))
i=1
count=0
while(i<=n):
    if(i%2==0):
        count+=1
    i += 1
print(count)

# find the sum of digits of number input by user ? len()

n=int(input('enter the number'))
l=len(str(n))
s=0
i=1
while(i<=l):
    rem=n%10
    s+=rem
    n//=10
    i+=1
print(s)

#or

n=int(input('enter the number'))
sum=0
while(n!=0):
    rem = n%10
    sum+=rem
    n//=10
print(sum)

# reverse of a number using while loop?

n=int(input("enter the number"))
rev=0
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n//=10
print(rev)

# palindrome or not

n=int(input("enter the number"))
rev=0
t=n
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n//=10
if(rev==t):
    print('palindrome')
else:
    print('not palindrome')

# check the number is harshad or not?
# sum each digit of the number then divide the by the sum then rem is zero then harshad

n=int(input('enter the number'))
t=n
sum=0
while(n!=0):
    rem=n % 10
    sum+=rem
    n//= 10
if(t % sum == 0):
    print(f'the number {t} is harshad')
else:
    print(f'the number {t} is not harshad')

# check the number is disarium or not ? 135= 1^1 + 3^2 + 5^3

n=int(input('enter the number'))
l=len(str(n))
t=n
sum=0
while(n!=0):
    rem=n%10
    sum+=rem**l
    n//=10
    l-=1
if(t==sum):
    print(f'the number {t} is disarium')
else:
    print(f'the number {t} is not disarium')

# check the number is armstrong or not?
# 153 = 1^3 + 5^3 + 3^3

n=int(input('enter the number :'))
l=len(str(n))
sum=0
t=n
while(n!=0):
    rem=n%10
    sum+=rem**l
    n//=10
if(t==sum):
    print(f'the number {t} is armstrong')
else:
    print(f'the number {t} is not armstrong')

# input numbers from the user till user input zero and at the end it should display the total number of even and odd numbers?

n=1
count=0
count2=0
while (n!=0):
    n = int(input('enter the number :'))
    if(n%2==0):
        count += 1
    if(n%2!=0):
        count2 += 1
print(f'total even number :{count}')
print(f'total odd number:{count2}')
