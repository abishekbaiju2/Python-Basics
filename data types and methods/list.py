# li=[1,2,'a','b','c']
# print(li)

# element aceessing

# print(li[0])

# list slicing

# print(li[::-1])
# print(li[:4])
# print(li[3:])
# print(li[::2])
# print(li[:])

# list iteration

# for i in li:
    # print(i,end=' ')

# find the lenght of the list input by the user without using len function ?

# eval()
# have to input like which data type

# n=eval(input('enter the list : '))
# count=0
# for i in n :
#     count+=1
# print(f' length of the list {count}')

# input integer list from user and display the sum of elements ?

# n=eval(input('enter the integer list : '))
# sum=0
# for i in n :
#     sum+=i
# print(sum)

# remove duplicate elements from the list input by the user ?

# n=eval(input('enter the list : '))
# m=[]
# for i in n:
#     if i not in m:
#         m+=[i]
# print(m)

# find the reverse of the list input by the user ?

# n=eval(input('enter the string : '))
# rev=[]
# for i in n :
#     rev=[i]+rev
# print(rev)

#or

# n=eval(input('enter the string : '))
# rev=[]
# for i in range(len(n)-1,-1,-1) :
#     rev+=[n[i]]
# print(rev)

# input a list of words and print list that contains revers of each words without slicing
# ['olleh','iah'] expected output
#
# n=eval(input('enter the string : '))
# rev2=[]
# for i in n:
#     rev = ''
#     for j in range(len(i)-1,-1,-1):
#         rev+=i[j]
#     rev2+=[rev]
# print(rev2)

# or

# n=eval(input('enter the string : '))
# rev2=[]
# for i in n:
#     rev = ''
#     for j in i:
#         rev=j+rev
#     rev2+=[rev]
# print(rev2)

# find the minimium value in list ?

# n=eval(input('enter the list : '))
# t=n[0]
# for i in range(len(n)):
#     if n[i]<t:
#         t=n[i]
# print(t)

# find the maximum value in list ?

# n=eval(input('enter the list : '))
# t=n[0]
# for i in range(len(n)):
#     if n[i]>t:
#         t=n[i]
# print(t)

# input a list of number from user and return a list with factorial of each numbers ?

# n=eval(input('enter the list : '))
# m=[]
# for i in n:
#     fact = 1
#     for j in range(1,i+1):
#         fact*=j
#     m+=[fact]
# print(m)

# find the reverse of each number input by the user ?

# n=eval(input('enter the list :'))
# m=[]
# for i in n:
#     rev = 0
#     l=len(str(i))
#     for j in range(l):
#         rem=i%10
#         rev= rev * 10 + rem
#         i//=10
#     m+=[rev]
# print(m)

# list methods

# append()

# li=['a','b','c']
# li.append('d')
# print(li)
# li.insert(0,'hello')
# print(li)
# li.extend([1,2,3])
# print(li)
# print(li.index('hello'))
# li.pop()
# print(li)
# li.pop(3)
# print(li)
# li.remove('d')
# print(li)
# li1=['a','A','b','B']
# li1.sort()
# print(li1)
# li.reverse()
# print(li)
# li.clear()
# print(li)
# li1=[9,6,4,7,3,2,1,8]
# li1.sort(reverse=True)
# print(li1)

