# break keyword

# for i in range(1,10):
#     if (i==5):
#         break
#     else:
#         print(i)

# continue keyword

# for i in range(1,10):
#     if (i==5):
#         continue
#     else:
#         print(i)

# write a pgrm to skip the numbers which are divisible by 2  and not by 3 fall in the range 1 to 100

# for i in range(1,100):
#     if(i%2==0 and i%3!=0):
#         continue
#     else:
#         print(i)

# write a pgrm to skip the numbers which are divisible by 3 btwn 1 t0 100

# for i in range(1,100):
#     if(i%3==0):
#         continue
#     else:
#         print(i)

# for loop with else

# for i in range(1,10):
#     print(i)
# else:
#     print('completed')

# first for loop work cheyum annittu else work cheyum

#check a number input by the user is prime or not

n=int(input('enter the number : '))
# prime will start in 2
if (n<=1):
    print('not prime')
else:
# ending range n  not n+1
    for i in range(2,n): # (2,2 ) same number vannal loop work cheyilla direct else verum
        if(n%i==0): #5%2==0 5%3==0
            # 8 eduthu for lopp 0ne condition true ayal not prime
            print('not prime')
            break
    else:
        print('prime')

# what is diff btwn break and exit() in python