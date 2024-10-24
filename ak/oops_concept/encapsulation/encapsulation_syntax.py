# syntax

# class encapsulation:
#     def __init__(self,name,address,phone):
#         self.name=name # public data member
#         self._address=address # protected data members
#         self.__phone= phone # private data member

# public access modifier

class person:
    def __init__(self,name,email):
        self.name=name
        self.email=email

    def display(self):
        print(self.name)
        print(self.email)

obj1=person('arun','arun@gmail.com')
obj1.display()
print(obj1.name)
obj1.name='akhil'
obj1.email='akhil@gmail.com'
obj1.display()

# private access modifier

