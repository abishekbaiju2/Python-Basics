# same function name with same number of arguments
# inheritance always required
# replacing a function body with same name and args

class A:
    def functionA(self):
        print('welcome to python')

class B(A): # here B inherits A
    def functionA(self):
        print('welcome to javascript')

obj=B()
obj.functionA() # here B functionA overrides A functionA (replace)


# create a parent class shapes with a function area() that returns zero
# create a child class rectangle that passes two values length and width with function area
# create a child class circle that passes radius with a function area

class shapes:
    def area(self):
        return 0

class rectangle(shapes):
    def  __init__(self,length ,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

class circle(shapes):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius

obj=rectangle(2,5)
print(obj.area())
obj1=circle(5)
print(obj1.area())