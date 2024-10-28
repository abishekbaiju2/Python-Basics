# dictionary

# di={'name':'amal','age':23}
# print(di.keys())
# print(di.values())
# print(di.items())
# print(di.get('name'))
# print(di.pop('name'))
# print(di.popitem())
# di.update({'phone no':6997969769})
# print(di)
# di.update({'phone no':68743543543})
# print(di)
# di['address']='jhk'
# print(di)
# # change the key name
# # di.pop('phone no') it return the value of phone no
# di['mobile']=di.pop('phone no')
# print(di)
# di.clear()
# print(di)

# dictionary iteration

# d={'a':1,'b':2,'c':3}

# for i in d: # print keys
#     print(i)

# for i in d.values(): # print values
    # print(i)

# for i in d.items(): # print key and value in tuple
#     print(i)

# for i,j in d.items(): # print keys and values
#     print(i,j)

# input a string from user and return a dictionary were keys as the character and values as no of occurrence?

# n=eval(input('enter the dictionary : ')) # hello
# f={}
# for i in n: # h:1 e:1 l:2 o:1
#     f[i]=n.count(i) # update function
# print(f)

#or

# n=eval(input('enter the dictionary : ')) # hello
# f={}
# for i in n:# h e l l o
#     if i in f:
#         f[i]+=1 # l:2
#     else:
#         f[i]=1 # h:1 e:1 o:1
# print(f)

# input a list of string from the user ?
# output [hello:5 ,hai:3]

# n=eval(input('enter the string : '))
# f={}
# for i in n:
#     f[i]=len(i)
# print(f)

#or

# n=eval(input('enter the string : '))
# f={}# for i in n:
#     count=0
#     for j in i:
#         count+=1
#     f[i]=count
# print(f)

# input a list of strings from the user ?
#output [1:odd,2:even,3:odd,4:even]

# n=eval(input('enter the string :'))
# f={}
# for i in n:
#     if i%2==1:
#         f[i]='odd'
#     else:
#         f[i]='even'
# print(f)





