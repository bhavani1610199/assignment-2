# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Single Inheritance
class Bank:
    def __init__(self, ACNO, IFSC):    #__init__ function is called automatically class create new objects
        self.ACCOUNTNUMBER = ACNO
        self.IFSCCODE = IFSC
    def printname(self):
        print(self.ACCOUNTNUMBER, self.IFSCCODE)

#Use the Person class to create an object, and then execute the printname method:

x = Bank(3341101015176, "CNRB0123")
x.printname()

# Multiple Inheritance
class Bank:
    def func1(self):
        input("Enter Your Name :")
class ACC(Bank):
    def func2(self):
        input("Enter Your Account Number :")
class IFSC(ACC):
    def func3(self):
        input("Enter IFSC CODE :")
        print("********Thank You*********")
ob=IFSC()
ob.func1()
ob.func2()
ob.func3()

# Hierarchical Inheritance
class web:
    def func1(self):
        input("Enter Your Website Name :")
class link(web):
    def func2(self):
        input("Paste Your Website Link Here :")
class prog(web):
    def func3(self):
        input("Programming Used in Your Website :")
        print("*******Thank You*********")
ob= link()
ob1= prog()
ob.func1()
ob.func2()
ob1.func3()

## Hybrid Inheritance
class Car:
    def func1(self):
        input("Enter Your Company Name :")

class Model(Car):
    def func2(self):
        input("Enter Model Name :")
class Reg(Car):
    def func3(self):
        input("Enter RC Number :")
class year(Car):
    def func4(self):
        input("Enter Year of Purcahse :")
        print("Thank You")

ob.func1()
ob.func1()
ob1.func2()
ob2.func3()
ob3.func4()


# Super Function
class Bank:
    def func1(self):
        input("Enter Bank Name :")
class Branch(Bank):
    def func2(self):
        super().func1()
        input("Enter Branch Name :")
ob=Branch()
ob.func2()

# Method Overriding
class car:
    def func1(self):
        input("Company Name :")
class model(car):
    def func2(self):
        input("Model Name :")
ob= car()
ob1= model()
ob.func1()
ob1.func2()

class Bank:
    def func(self):
        input("Enter Your Name :")
class Branch(Bank):
    def func1(self):
        input("Enter Branch Name:")
class ACC(Bank):
    def func2(self):
        input("Enter Your Account Number :")
class IFSC(ACC):
    def func3(self):
        input("Enter IFSC CODE :")
class amount(Bank):
    def func4(self):
        input("Enter Amount You Want to Deposit :")
        print("********Successful*********")
        print("Credited Amount with be Updated Soon")
        print("Thank You")

ob=Bank()
ob1=Branch()
ob2=ACC()
ob3=IFSC()
ob4=amount()
ob.func()
ob1.func1()
ob2.func2()
ob3.func3()
ob4.func4()