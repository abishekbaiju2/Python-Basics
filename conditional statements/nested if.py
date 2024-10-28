#syntax

#if (condition):
      # body of if
         # if( condition):

#create a simple calculator using nested if ?

print('1] addition \n 2] substraction \n 3] multiplication \n 4] division')
# \n : is for break the line
choice=int(input("plz enter your choice :"))
if(choice in [1,2,3,4]):
    num1=int(input('enter the first number :'))
    num2=int(input('enter the second number :'))
    if(choice == 1):
        print(f'{num1} + {num2} = {num1 + num2}')
    elif(choice == 2):
        print(f'{num1} - {num2} = {num1 - num2}')
    elif(choice == 3):
        print(f'{num1} * {num2} = {num1 * num2}')
    elif(choice == 4):
        print(f'{num1} / {num2} = {num1 / num2}')
else:
    print('invalid')


# accept each  gender and no of  working days from user and display the wages according to the following criteria using nested if ?
#      age
#      >=18 and <30       : male     : 700
#                         : female   : 750
#    >=30 and <=40        : male     : 800
#                         : female   : 850

gender=input('enter the gender : ')
age=int(input('enter the age : '))
days=int(input("enter the no of working days : "))
if(age >= 18 and age < 30):
    if(gender == 'male'):
        print(f" wages is {700 * days}")
    elif(gender== 'female'):
        print(f" wages is {750 * days}")
elif(age >= 30 and age <= 40):
    if (gender == 'male'):
        print(f" wages is {800 * days}")
    elif (gender == 'female'):
        print(f" wages is {850 * days}")
else:
    print('invalid')

