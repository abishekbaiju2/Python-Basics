# in hierarchical inheritance all child has to create object

# syntax
# class a: # parent class
#     def funa(self):
#         print('class A')
# class b(a): # child class
#     def funb(self):
#         print('class B')
# class c(a):# child class
#     def func(self):
#         print('class C')
#
# obj=c()
# obj.funa()
# obj.func()
#
# obj1=b()
# obj1.funa()
# obj1.funb()

# details : name,email,phone
# doctor : hospital_name,specialization
# engineer : company_name,designation


# class details:
#     def __init__(self,name,email,phone):
#         self.name=name
#         self.email=email
#         self.phone=phone
#
#     def display(self):
#         print('name=',self.name)
#         print('email=',self.email)
#         print('phone=',self.phone)
#
# class doctor(details):
#     def __init__(self,name,email,phone,hospital_name,specialization):
#         details.__init__(self,name,email,phone)
#         self.hospital_name=hospital_name
#         self.specialization=specialization
#
#     def display1(self):
#         self.display()
#         print('hospital_name=',self.hospital_name)
#         print('specialization=',self.specialization)
#
# class engineer(details):
#     def __init__(self,name,email,phone,company_name,designation):
#         details.__init__(self,name,email,phone)
#         self.company_name=company_name
#         self.designation=designation
#
#     def dispaly2(self):
#         self.display()
#         print('company_name=',self.company_name)
#         print('designation=',self.designation)
#
# obj=doctor('arun','arun@gmail.com',9887776,'apollo','eye')
# obj.display1()
# print()
# obj1=engineer('appu','appu@gmail.com',33666577,'tcs','tester')
# obj1.dispaly2()

