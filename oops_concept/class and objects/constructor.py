# class student:
#     def __init__(self,stud_name,roll_num,age):
#         self.stud_name=stud_name
#         self.roll_num=roll_num
#         self.age=age
#
#     def display(self):
#         print(self.stud_name)
#         print(self.roll_num)
#         print(self.age)
#
# obj1=student('arun',12,22) # directly pass input
# obj1.display()


# create  a class library_management
# 1. __init__ method , initialize the library_name
# and set public variable , book=[]
# 2. add_book(title)
# 3. remove_book(title)
# 4.list_books()

class library_management:
    def __init__(self,library_name):
        self.library_name=library_name
        self.book=[]

    def add_book(self,title):
        self.book.append(title)

    def remove_book(self,title):
        if title in self.book:
            self.book.remove(title)
        else:
            print('book not found')

    def list_books(self):
        print('library_name=',self.library_name)
        print(self.book)

obj1=library_management('ak library')
obj1.add_book('IT')
obj1.add_book('DUNE')
obj1.add_book('EVE')
obj1.list_books()
obj1.remove_book('HOPE')