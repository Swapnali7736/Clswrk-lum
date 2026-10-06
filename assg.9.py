# 1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
#
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#
# Create an object of the Circle class and call both methods to display the results.

# class Circle:
#     def __init__(self):
#         self.r=float(input("enter the radius:"))
#     def getarea(self):
#         self.area=3.14*(self.r**2)
#         print(self.area)
#     def getperimeter(self):
#         self.perimeter=2*(3.14*self.r)
#         print(self.perimeter)
# c=Circle()     
# c.getarea()  
# c.getperimeter() 

   

# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.


class Account:
    def __init__(self):
        self.ano=int(input("enter the acccount number:"))
        self.aname=input("enter the acccount name:")
        self.balance=int(input("enter the balance:"))
    def withdraw(self):
        amt=int(input("enter the amt to withdraw:"))
        self.balance=self.balance-amt
        print(self.balance)  
    def deposit(self):
        amt=int(input("enter the amt to deposit:"))    
        self.balance=self.balance+amt
        print(self.balance)
    def showbalance(self):
        print(self.balance)    
# a=Account()
# a.withdraw()
# a.deposit()
# a.showbalance() 

###Another method  

a=Account()   
b=Account() 
l=[a,b]
number=int(input("enter account number to know the balance:"))
for i in l:
    if(i.ano==number):
        print("balance:",i.balance) #print the balance of the person whose accountnumber matches with the entered one
        print(f"Account number: {i.ano} Name: {i.aname} Balance: {i.balance}")   # f is formatted string