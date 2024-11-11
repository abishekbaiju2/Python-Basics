# zero division error

try:
    a=int(input('enter a: '))
    b=int(input('enter b: '))
    print(a / b)
except:
    print("can't divide a number by zero.... ")


# value error

try:
    num=int(input('enter the number'))
    print(num)
except:
    print('plz input an int value..')

# index error

try:
    lst=['a','b','c','d']
    indexposition=int(input('enter the index position'))
    print(lst[indexposition])
except:
    print('index out of range')


