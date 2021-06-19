# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def display(x):                                   # Here x is parameter
    print("Welcome to Day-6")
    print("Marks of Last Task",x)
display(12)

def team(p):
    print("Name of the Player is :",p)
team("Dhoni")
team("KL Rahul")

def state(AP_cap,KA_cap,TN_cap):                 #Assigning multiple parameters to a function
    print("Captial of AP is :",AP_cap)
    print("Captial of KA is :",KA_cap)
    print("Captial of TN is :",TN_cap)
state("Hyderabad","Banglore","Chennai")

# * is used when we don't know how many arguments is passed
def ipl(*teams):
    print("Name of the Team is :",teams)
ipl("CSK","KXIP","MI","SRH","RR","RCB","KKR","DD")

# we can assign the key and value in the argument
def player(player1,player2,player3):
    print("My Favorite Player is :", player1)
    print("My Best Player is :", player2)
    print("My Fantasy Player is", player3)
player(player1="Dhoni",player2="Rohit",player3="KL Rahul")


# return a value, use the return statement
def days(y):
    return y*10
print(days(3))

# passing a default value while initiation
def myfunc(fname,lname="saravanan"):
    print("First Name :",fname)
    print("Last Name :",lname)
myfunc("bhavi")

#exercise
a=int(input("Enter First Number :"))
b=int(input("Ebter Second Number :"))
def math_function(a,b):
    print("Addition of two numbers is :",(a + b))
    print("Subtraction of two numbers is :",(a - b))
    print("Division of two numbers is  :",(a/b))
    print("Multiplication of two numbers is :",(a*b))
math_function(a,b)

def covid(patientname,bodytemperature= 97):
    print("please Enter Patient Name :",patientname)
    print("Body Temperature of Patient :",bodytemperature)
covid("bhavani")






