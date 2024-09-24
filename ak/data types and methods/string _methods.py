# greet='hello world'
# string_1= str() # create an empty string
# string_2=greet[1:]
from email.policy import strict

# string formation

# name='anzil'
# desigination = 'python django trainer'
# company='luminar'
# self_intro='i am '+ name +" i am working as a "+ desigination +' at '+ company
# print(self_intro)
#
# self_intro_1='i am {0} i am working as a {1} at {2}'.format(name,desigination,company)
# print(self_intro_1)

# name='abishek'
# current_course='python django'
# age=22
# completed ='b.tech'
# place='thrissur'
# #{1:s} giving the data type only string
# introduction ='i am {0:s} and my age is {1:d} and my place is {2:s} and i completed {3:s} and i am doing the current course is {4:s} '.format(name,age,place,completed,current_course)
# print(introduction)
# introduction_1 ='i am %s and my age is %d and my place is %s and i completed %s and i am doing the current course is %s ' % (name,age,place,completed,current_course)
# print(introduction_1)


# name[0]='h'
# # string is immutable
# print(name)

#1.upper()
#2.lower()

# string_input=input()
# h=string_input.upper()
# print(h)

# n=input('enter your name : ')
# k=n.upper()
# j=n.lower()
# print(k)
# print(j)

# only j has to be uppercase
# n='johndoe'
# k=n[0].upper()
# j=n[1:]
# print(k+j)

# 10 characters odd number must be upper case and even be lower case?

# n=input('enter the string :')
# l=len(n)
# k = ''
# for i in range(l):
#     if i%2==0:
#         k += n[i].upper()
#     else:
#         k += n[i].lower()
# print(k)

#or

# n=input('enter the string :')
# l=len(n)
# for i in range(l):
#     if i%2==0:
#         print(n[i].upper(),end='')
#     else:
#         print(n[i].lower(),end='')

