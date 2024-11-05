# syntax

class A : #parent class, base class
    def functionA(self):
        print('CLASS A')

class B(A): #child class , derived class
    def functionb(self):
        print('class B')
x=B()
x.functionA()
x.functionb()

# create a class person
# with methods
# 1. person_details(name,age)
# 2. person_display() #should print the persons name and age
# create a class student that inherits person class
# 1. student_details(roll,dept,email)
# 2, student_display() # name,age,roll,dept,email

class person:
    def person_details(self,name,age):
        self.name=name
        self.age=age

    def person_display(self):
        print('name=',self.name)
        print('age=',self.age)
class student(person):
    def student_details(self,roll,dept,email):
        self.roll=roll
        self.dept=dept
        self.email=email

    def student_display(self):
        self.person_display() # name and age
        print('roll=',self.roll)
        print('dept=',self.dept)
        print('email=',self.email)


obj1=student()
obj1.person_details('abishek',22)
obj1.student_details(12,'cs','abishek@gmail.com')
obj1.student_display()

# create a parent class vehicle
# 1.vehicle_details(make ,model,year)
# 2.display_info() # make model year
# create a child class car should inherit vehicle
# 1.additional_info(no_of_doors,fuel_type)
# 2.complete_details() # make model year no_of_doors,fuel_type
# create 2 car objects

class vehicle:
    def vehicle_details(self,make ,model,year):
        self.make=make
        self.model=model
        self.year=year

    def display_info(self):
        print('make=',self.make)
        print('model=',self.model)
        print('year=',self.year)

class car(vehicle):
    def additional_info(self,no_of_doors,fuel_type):
        self.no_of_doors=no_of_doors
        self.fuel_type=fuel_type

    def complete_details(self):
        self.display_info()
        print('no of doors=',self.no_of_doors)
        print('fuel type=',self.fuel_type)

obj1=car()
obj1.vehicle_details('toyota','fortuner',2000)
obj1.additional_info(5,'diesel')
obj1.complete_details()

# single inheritance using constructor

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def person_display(self):
        print('name=',self.name)
        print('age=',self.age)

class student(person):
    def __init__(self,name,age,roll,dept,email):
        super().__init__(name,age)
        self.roll=roll
        self.dept=dept
        self.email=email

    def student_display(self):
        self.person_display() # name and age
        print('roll=',self.roll)
        print('dept=',self.dept)
        print('email=',self.email)


obj1=student('abishek',22,12,'cs','abishek@gmail.com')
obj1.student_display()

