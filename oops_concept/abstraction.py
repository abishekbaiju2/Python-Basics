from abc import ABC , abstractmethod

# abc : package
# ABC : module

class Shapes(ABC): # abstract class # here ABC is the base class where the content is hidden
    @abstractmethod
    def area(self):
        pass # define empty function
    @abstractmethod
    def perimeter(self):
        pass

class rectangle(Shapes):
    def __init__(self,w,h):
        self.w=w
        self.h=h

    def area(self):
        return self.w * self.h

    def perimeter(self): # both function of shape have to use else it won't work
        return 2* (self.w+self.h)

class circle(Shapes):
    def __init__(self,r):
        self.r=r

    def area(self):
        return 3.14* self.r**2

    def perimeter(self):
        return 2*3.14*self.r


obj=rectangle(4,5)
print(obj.area())
print(obj.perimeter())

obj1=circle(6)
print(obj1.area())
print(obj1.perimeter())

