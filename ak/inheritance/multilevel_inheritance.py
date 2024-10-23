# class A:
#     def funA(self):
#         print('class A')
#
# class B(A):
#     def funB(self):
#         print('class B')
#
# class C(B):
#     def funC(self):
#         print('class C')

# create 3 class vehicle ,car ,electric_car
# method vehicle:
# __init__(model make year)
# car :
# __init__(num_ doors)
# display_car_info()
# electric car:
# __init__(battery)
# display()
# complete_display()


# class vehicle:
#     def __init__(self,model,make,year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def display_info(self):
#         print('make=',self.make)
#         print('model=',self.model)
#         print('year=',self.year)
#
# class car(vehicle):
#     def __init__(self,model,make,year,num_doors):
#         vehicle.__init__(self,model,make,year)
#         self.no_of_doors = num_doors
#
#     def display_car_info(self):
#         self.display_info()
#         print('no of doors=',self.no_of_doors)
#
# class electric_car(car):
#     def __init__(self,model,make,year,num_doors,battery_capacity):
#         car.__init__(self,model,make,year,num_doors)
#         self.battery_capacity=battery_capacity
#
#     def display(self):
#         self.display_car_info()
#         print('battery_capacity=',self.battery_capacity)
#
# obj1=electric_car('tata','tiago',2000,5,5000)
# obj1.display()
