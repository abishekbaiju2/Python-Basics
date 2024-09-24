#syntax

#if(condition):
   #body of if


  # take a integer input from a user if the input falls including the range 1 to 10 the prgm to print hello

num=int(input("enter the number"))
if(num>=1 and num<=10):
      print('hello')

# write a prgm to take a char from user and check wheather the char is vowel or not?

char=input('enter the character : ')
if(char in 'aeiouAEIOU'):
    print(f'yes, {char} is a vowel ')

#even checker?

num=int(input("enter the number"))
if(num%2==0):
     print(f'yes, {num} is even')

#odd checker

num=int(input("enter the number"))
#num%2!==0
if(num%2==1):
    print(f'yes, {num} is odd')