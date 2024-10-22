# syntax
# class A : # parent1
#     def funA(self):
#         print('class A')
#
# class B:# parent2
#     def funB(self):
#         print('class B')
#
# class C(A,B):# child class
#     def funC(self):
#         print('class c')

#school --> parent1
# school_details : school_name , location
# school_display
# parent --> parent2
# parent_details=parent_name,address
# parent_display
# student --> child
# student_details : roll_no ,name,dept
# student_display()
# view_complete_details() # schoolname loc parent address roll name dept

class school:
    def school_details(self,school_name,location):
        self.school_name=school_name
        self.location=location

    def school_display(self):
        print('school_name=',self.school_name)
        print('location=',self.location)

class parent:
    def parent(self,parent_name,address):
        self.parent_name=parent_name
        self.address=address

    def parent_display(self):
        print('parent_name=',self.parent_name)
        print('address=',self.address)

class student(school,parent):
    def student_details(self,roll_no,name,dept):
        self.roll_no=roll_no
        self.name=name
        self.dept=dept

    def student_display(self):
        print('roll_no=',self.roll_no)
        print('name=',self.name)
        print('dept=',self.dept)

    def view_complete_details(self):
        self.school_display()
        self.parent_display()
        self.student_display()

obj1=student()
obj1.school_details('csm','vadanappally')
obj1.parent('baiju','thalikulam')
obj1.student_details(22,'abishek','cse')
obj1.student_display()
obj1.view_complete_details()

# using constructor

# syntax
# class A:
#     def __init__(self,a,b):
# class B:
#     def __init__(self,c,d):
# class C(A,B):
#     def __init__(self,a,b,c,d,e,f):
#         A.__init__(self,a,b) # more one class to inherit then use class to call don't use super()
#         B.__init__(self,c,d)
# obj=C(1,2,3,4,5,6)


# company --> company_name,location
# company_display
# team_leader --> team_leader_name,department
#teamlead_display
# worker : emp_name,designation,salary
# display()

class company:
    def __init__(self,company_name,location):
        self.company_name=company_name
        self.location=location

    def company_display(self):
        print('company_name=',self.company_name)
        print('location=',self.location)

class team_leader:
    def __init__(self,team_leader_name,department):
        self.team_leader_name=team_leader_name
        self.department=department

    def teamlead_display(self):
        print('team_leader_name =',self.team_leader_name)
        print('department=',self.department)

class worker(company,team_leader):
    def __init__(self,company_name,location,team_leader_name,department,emp_name,designation,salary):
        company.__init__(self,company_name,location)
        team_leader.__init__(self,team_leader_name,department)
        self.emp_name=emp_name
        self.designation=designation
        self.salary=salary

    def display(self):
        self.company_display()
        self.teamlead_display()
        print('emp_name=',self.emp_name)
        print('designation',self.designation)
        print('salary=',self.salary)

obj1=worker('tcs','kakkand','abishek','cse','akhil','tester',15000)
obj1.display()



