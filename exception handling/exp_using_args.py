# try:
#     lst=['a','b','c','d']
#     indexposition=int(input('enter the index position'))
#     print(lst[indexposition])
#
# except IndexError as err:
#     print(err)
#
# except ValueError as a:
#     print(a)
#


try:
    age=int(input('enter the age :'))

    if age>=18:
        print('registered')
    else:
        raise ValueError('plz input age greater than 17')

except ValueError as a:
    print(a)
