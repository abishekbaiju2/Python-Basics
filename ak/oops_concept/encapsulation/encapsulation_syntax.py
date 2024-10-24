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

class person:
    def __init__(self,name,email):
        self.__name=name
        self.__email=email

    def __display(self): # private
        print(self.__name)
        print(self.__email)

obj2=person('arun','arun@gmail.com')
print(obj2._person__name)
print(obj2._person__email)
obj2._person__name='akhil'
obj2._person__email='akhil@gmail.com'
obj2._person__display()



# name mangling
# it is a method of giving access to the private data members  and the methods inside a class
# _classname__datamember

# protected

class person:
    def __init__(self,name,email):
        self._name=name
        self._email=email

    def _display(self):
        print(self._name)
        print(self._email)

obj3=person('arun','arun@gmail.com')
obj3._display()
obj3._name='akhil'
obj3._email='akhil@gmail.com'
obj3._display()

