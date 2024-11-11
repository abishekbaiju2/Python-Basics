# zerodivisionerror ,value error

try:
    a = int(input('enter a: '))
    b = int(input('enter b: '))
    print(a / b)

except ZeroDivisionError:
    print("can't divide a number by zero.... ")

except ValueError:
    print('plz input an int value..')

# solve quadratic equation using exception handling

try:


