# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

list=[22,25,28,32,40]
for i,val in enumerate(list):
    print(i,':',val+2)

for i in range(5,0,-1) :
    for j in range(i,0,-1):
        print(j,end="")
    print()

n = int(input("How many terms you want? "))
# first two terms
n1 = 4
n2 = 2
count = 1
# check if the number of terms is valid
if n <= 0:
    print("Plese enter a positive integer")
elif n == 1:
    print("Fibonacci sequence:")
    print(n1)
else:
    print("Fibonacci sequence:")
    print(n1,",",n2,end=', ')
    while count < n:
        nth = n1 + n2
        print(nth,end=' , ')
        # update values
        n1 = n2
        n2 = nth
        count += 1


num=int(input("Enter a Number :"))
sum=0
temp=num
while temp>0 :
    digit=temp % 10
    sum+=digit**3
    temp//=10
if num==sum:
    print("It is an Armstrong")
else:
    print("It is not Armstrong")

num = 9
for i in range(1, 15):
    print(num, 'x', i, '=', i * num)

num = int(input("Enter a positive or Negative Number :"))
if (num > 0):
    print("It is a Positive Number")
else:
    print("It is a Negative Number")


print("Enter the days::")

d= int(input())
y=None
w=None
# Conversion of days in to years, weeks and days
y = (int)(d / 365)
w = (int)((d % 365) / 7)
d = (int)(d - ((y * 365) + (w)))
a=y,w,d
print("Age is :",y, " Year, ", w, " Weeks, and ", d, " Days\n")

import math
a=int(input("Enter a Value :"))
print("The value of the sine is :",end="")
print(math.sin(a))
print("The value of the cosine is :",end="")
print(math.cos(a))
print("The value of the tan is :",end="")
print(math.tan(a))


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("Select the operator :")
print("1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division")
choice=input("Select Your Choice (1/2/3/4 :")
num1=float(input("Enter First Number :"))
num2=float(input("Enter second Number :"))
if choice=='1':
    print("Addition of Two Number is :",num1,"+",num2,"=",add(num1,num2))
if choice=='2':
    print("Subtraction of Two Numbers is :",num1,"-",num2,"=",sub(num1,num2))
if choice=='3':
    print("Multiplication of Two Numbers is :",num1,"*",num2,"=",mul(num1,num2))
if choice=='4':
    print("Division of Two Numbers is :",num1,"/",num2,"=",div(num1,num2))












