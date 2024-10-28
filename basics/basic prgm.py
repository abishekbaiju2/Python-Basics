#take to integer inputs from user and display the sum and the product o the true values

a=int(input('enter the first number'))
b=int(input('enter the first number'))
print(f'sum of {a} and {b} is {a+b} and the product is {a*b}')

#take a number from user and display the square of the number

a=int(input('enter the first number'))
print(f'the square of {a} is {a**2}')

#find the cube of a number from the excepted output

a=int(input('enter the first number'))
print(f'the square of {a} is {a**3}')

#find the area of circle

a=int(input('enter the radius'))
print(f'the area of the circle is {3.14*a**2}')

#find the area of the triangle

a=int(input('enter the breath'))
b=int(input('enter the hight'))
print(f'the area of the triangle is {0.5*a*b}')

#find the square root of a number

a=int(input('enter the number'))
print(f'the square root of a number is {a**0.5}')

#find the last digit of number input my the user

a=int(input('enter the number'))
print(f'the last digit of number is {a%10}')

# create a quadratic equation solver

a=int(input('enter the value of a :'))
b=int(input('enter the value of b :'))
c=int(input('enter the value of c :'))
d=(b**2-4*a*c)**0.5
x1=(-b+d)/(2*a)
x2=(-b-d)/(2*a)
print(x1)
print(x2)

