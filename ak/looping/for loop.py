#syntax

# for i in range(n):
    # body of for loop

for i in range(10):
    print('hello')

n=int(input("enter the number"))
for i in range(n):
    print('hello')

# write a prgm to print first 10 natural numbers using for loop

n=int(input('enter the number'))
for i in range(n):
    print(i+1)

# start and end

for i in range(100,201):
    print(i+1)

# enter the starting range : 1000
# enter the ending range : 2000

n=int(input('enter the starting number'))
m=int(input('enter the ending number'))
for i in range(n,m+1):
    print(i)

# write a pgrm to print even numbers fall in the range input by the user ?

n=int(input('enter the starting number'))
m=int(input('enter the ending number'))
for i in range(n,m+1):
    if(i%2==0):
        print(i)

# write a pgrm to print odd numbers fall in the range input by the user ?

n=int(input('enter the starting number'))
m=int(input('enter the ending number'))
for i in range(n,m+1):
    if(i%2==1):
        print(i)

# enter the number of odd values :5 ?

n=int(input('enter the number'))
for i in range(1,n):
    if(i%2==1):
        print(i)

# enter the number of even values :2 ? 

n=int(input('enter the number'))
for i in range(1,n):
    if(i%2==0):
        print(i)

# multiplication table

n=int(input("enter the number"))
for i in range(1,11):
    print(f'{i} * {n}={i*n}')

# sum of first 10 natural numbers

sum=0
# always sum =0 initialize
for i in range(1,11):
    sum +=i
print(sum)

# sum of first five odd no

sum=0
for i in range(1,10):
    if(i%2==1):
        sum += i
print(sum)

# product of even no in (1,21)

prdt=1
# always initialize product=1
for i in range(1,21):
    if (i % 2 == 0):
        prdt *= i
print(prdt)

#sum of even and odd

k=0
j=0
for i in range(1,21):
    if(i%2==0):
        k += i
    else:
        j += i

#put the print in last so it will print two condition
print('sum of even =',k)
print('sum of odd =',j)

# factorial of a number

prdt=1
n=int(input('enter the number :'))
for i in range(1,n+1):
    prdt*=i
print(f'factorial of {n} is {prdt}')

# find count

count = 0
# initialize count =0
for i in range(1,101):
    if(i % 5 == 0):
        count += 1
# always count +1
print(count)

# sum of digit of num

sum=0
n=int(input('enter the number :'))
l=len(str(n))
#find the lenght of the number to find how many times to loop
for i in range(l):
    rem= n%10
# last digit of the number and save to sum
    sum +=rem
    n//=10
# float division use to reduce the number
print(f'sum of digits={sum}')

# write a prgm to find the product of digits input by the user

n=int(input('enter the number'))
prdt=1
l=len(str(n))
for i in range(l):
    rem=n%10
    prdt*=rem
    n//=10
print(f'product of digits={prdt}')

# write a prgm to find a reverse of a number input by the user

n=int(input('enter the number'))
l=len(str(n))
rev=0
for i in range(l):
    rem=n%10
    rev= rev * 10 + rem
# use  rev * 10 and add rem eg: 0*10 +3 = 30 then 30 *10 + 2 = 32
    n//=10
print(rev)

# write a prgm  to check a number is palindrome or not?

n=int(input('enter the number'))
t=n
# have to take a copy of input number in temporary variable
rev=0
l=len(str(n))
for i in range(l):
    rem=n%10
    rev= rev * 10 + rem
    n//=10
# n will always change the value
if(t == rev):
    print('palindrome')
else:
    print('not palindrome')

#for i in range(initial  , final ,inc/dec )

# write a pgrm to print given series 5 10 15 20 25 30 ?

for i in range(5,31,5):
# end  is used to print the series in a line and how much space have you given is printed
    print(i , end="  ")

# \t is tab space

print() # new line oru pgrm kazhijittu

# write a pgrm given series 1000 2000 3000 4000?

for i in range(1000,4001,1000):
    print(i,end='\t' )

# print first  10 natural number in reverse order ?

for i in range(10,0,-1):
    print(i ,end=' ')

for i in range(9,0,-2):
    print(i ,end=' ')

print()

for i in range(50,9,-10):
    print(i ,end=' ')

print()

for i in range(10,-1,-2):
    print(i ,end=' ')
