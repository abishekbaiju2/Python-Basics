# syntax
# class baseclass:
#     def funbase(self):
#         print('class base')
#
# class a(baseclass):
#     def funa(self):
#         print('class a')
#
# class b(baseclass):
#     def funb(self):
#         print('class b')
#
# class c (a,b):
#     def func(self):
#         print('class c')
#
# obj=c()
# obj.funbase()
# obj.funa()
# obj.funb()
# obj.func()

# university : university_name, location
# university_info()
# under_graduate_program : name_of_ug_students, ug_course
#post_graduate_program : name_of_pg_students , pg_project
# program director : director_name

class university:
    def __init__(self,university_name, location):
        self.university_name=university_name
        self.location=location

    def university_info(self):
        print('university_name=',self.university_name)
        print('location=',self.location)

class under_graduate_program(university):
    def __init__(self,university_name, location,name_of_ug_students, ug_course):
        university.__init__(self,university_name, location)
        self.name_of_ug_students=name_of_ug_students
        self.ug_course=ug_course

    def display(self):
        self.university_info()
        print('name_of_ug_students=',self.name_of_ug_students)
        print('ug_course=',self.ug_course)

class post_graduate_program(university):
    def __init__(self,university_name, location,name_of_pg_students , pg_project):
        university.__init__(self,university_name, location)
        self.name_of_pg_students=name_of_pg_students
        self.pg_project=pg_project

    def display2(self):
        self.university_info()
        print('name_of_pg_students=',self.name_of_pg_students)
        print('pg_project=',self.pg_project)

class program_director(under_graduate_program,post_graduate_program):
    def __init__(self,university_name, location,name_of_ug_students, ug_course,name_of_pg_students , pg_project,director_name ):
        under_graduate_program.__init__(self,university_name, location,name_of_ug_students, ug_course)
        post_graduate_program.__init__(self,university_name, location,name_of_pg_students , pg_project)
        self.director_name=director_name

    def display3(self):
        self.display()
        self.display2()
        print('director_name=',self.director_name)

obj=program_director('ktu','tvm','arun','btech','akhil','drone','appu')
obj.display3()