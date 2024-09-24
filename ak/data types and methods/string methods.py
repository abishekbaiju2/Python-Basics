# word='hello world'
# print(word)

# string concatenation

# a='hello'
# b='hai'
# print(a+' '+b)

# element accessing
# to access index position

# print(word[4])

# string slicing
# #to access the part of the sequence

# print(word[0:5])
# print(word[6:11])
# print(word[:5]) # it print starting of the string to given index
# print(word[6:]) # it print given index of the string to ending index
# print(word[:]) # whole index of the string is
#
# print(word[0:5:2])  # print the index by incrementing 2
#
# print(word[::-1]) # to print the reverse order of the string

# string iteration
# for i in word:
#     print(i)

# find the length of the string input by the user without using len function?
#
# word=input('enter the word : ')
# count=0
# for i in word:
#     count+=1
# print(f' length of the string is : {count}')

# find the last index position of strings input by the user?

# word=input('enter the string : ')
# count=0
# for i in word:
#     count+=1
# print(f' the last index is {count-1}')

# write a program to remove spaces from a string input by the user ?

# word=input('enter the string :')
# for i in word:
#     if(i!=" "):
#         print(f"{i}",end='')

# or

# word=input('enter the string :')
# for i in word:
#     if(i==" "):
#         continue
#     else:
#         print(f"{i}",end='')

# string concate!!!!

# word=input('enter the string :')
# word2="" # save it in memory space
# for i in word:
#     if(i!=" "):
#         word2+=i # concate
# print(word2)

# write a program to reverse a string input by a user without using slice operation?

# word=input("enter the string : ")
# rev=''
# for i in word:
#     rev=i+rev
# print(rev)

#or

# word=input("enter the string : ")
# rev=''
# l=len(word)-1
# for i in range(l,-1,-1):
#     rev+=word[i]
# print(rev)

# write a program to check a string input by the the user is palindrome or not?

# word=input("enter the string : ")
# rev=''
# l=len(word)-1
# for i in range(l,-1,-1):
#     rev+=word[i]
# if(rev==word):
#     print('palindrome')
# else:
#     print('not palindrome')

# input a string from a user find  total count of vowels?
# input a string and print the vowels?

# n=input('enter the string : ')
# vowels='AEIOUaeiou'
# count=0
# for i in n:
#         if i in vowels:
#                  count+=1
#                  print(i,end=' ')
# print(f"\n{count}")



