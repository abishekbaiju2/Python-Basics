class person:
    def create_person(self,name,age,gender): # create object
        self.name=name #public
        self.age=age
        self.gender=gender

    def display_person(self):
        print('name=',self.name)
        print('age=',self.age)
        print('gender=',self.gender)

obj1= person()
obj1.create_person('alex',20,'male')

obj2= person()
obj2.create_person('manju',23,'female')

obj1.display_person()
obj2.display_person()

# name,age,gender : dynamic : we can change  the value