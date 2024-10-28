# create a class company with two satic variables company name and location ?
# 1. employee_details() with attributes emp_id , emp_name , designation,salary
# 2. employee_display()
# company_name = 'TCS'
# company_location='Kakkanad'
# emp_id=123
# emp_name=akhil
# designation=tester
# salary=180000



class company:
    company_name = 'TCS'
    company_location='Kakkanad'
    def employee_details(self,emp_id,emp_name,designation,salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.designation=designation
        self.salary=salary

    def employee_display(self):
        print('company_name =',company.company_name)
        print('company_location =',company.company_location)
        print('emp_id =',self.emp_id)
        print('emp_name =',self.emp_name)
        print('designation =',self.designation)
        print('salary =',self.salary)

obj1=company()
obj1.employee_details(123,'arun','developer',15000)
obj1.employee_display()


# create a class bank_account:
# with 2 static variables bank_name,branch
# 1.  set_account_info(ac_num,ac_holder)
# also set a public attribute,balance=0
# 2.deposit(amount)
# 3. withdraw (amount) : checking
# 4. account_info() : bank_name,branch,ac_num,ac_holder
# 5. check_balance() : current_balance



class bank:
    bank_name='SBI'
    branch='vadanapally'
    def set_account_info(self,ac_num,ac_holder):
        self.ac_num=ac_num
        self.ac_holder=ac_holder
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} deposited, balance =",self.balance)

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance -= amount
            print(f"{amount} withdrawed, balance =", self.balance)
        else:
            print('insufficient balance')

    def account_info(self):
        print('bank_name =',bank.bank_name)
        print('branch',bank.branch)
        print('ac_num=',self.ac_num)
        print('ac_holder=',self.ac_holder)
        print('bank_balance=',self.balance)

    def check_balance(self):
        print('current_balance =',self.balance)

obj1=bank()
obj1.set_account_info(123,'arun')
obj1.deposit(50000)
obj1.withdraw(30000)
obj1.account_info()
obj1.check_balance()



