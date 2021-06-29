# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#errors listing
L1=[2,5,7,9,11]
print(L1[5])

dict={'car1':'I20','car2':'toyoto'}
print(dict['key'])

# Type error
print(5+'10')

# Value Error
print(int("abcd"))

#Nameerror
print(bhavi)


def addition(a, b):
    try:
        result = a + b
        print("Addition is : ", result)
    except Exception as e:
        print(e)


def subtraction(a, b):
    try:
        result = a - b
        print("subtraction is : ", result)
    except Exception as e:
        print(e)


def multiplication(a, b):
    try:
        result = a * b
        print("multiplication is : ", result)
    except Exception as e:
        print(e)


def division(a, b):
    try:
        result = a / b
        print("division is : ", result)
    except Exception as e:
        print(e)


def calculation():
    try:
        a = int(input("enter first number : "))
        b = int(input("enter second number : "))
        addition(a, b)
        subtraction(a, b)
        multiplication(a, b)
        division(a, b)

    except Exception as e:
        print("Only Integers Allowed")
        calculation()

    except Exception as e:
        print("Only Integers Allowed")
calculation()
# call a function
calculation()

try :
    print(a)
except NameError :
    print("a is not defined")
except :
    print("Refresh")

try :
    a=input("Enter Your Details : ")
except :
    print("Enter Your Data in Any Type ")
finally :
    print("Try And Exception are finished")






