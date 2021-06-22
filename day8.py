# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#Python script to merge two Python dictionaries

def merge(car, bike):
    return (car.update(bike))


car = {
    '1': "City",
    '2': "Toyota",
    '3': "i20"}
bike = {
    '4': "Royal enfeild",
    '5': "Himalayan",
    '6': "k20"}
print(merge(car, bike))
print(car)

#ascending in list and convert a set

# Initialize array
list1 = [12, 2, 90, 6, 18];
temp = 0;

# Displaying elements of original array
print("Elements of original array: ");
for i in range(0, len(list1)):
    print(list1[i], end=" ");

# Sort the array in ascending order
for i in range(0, len(list1)):
    for j in range(i + 1, len(list1)):
        if (list1[i] > list1[j]):
            temp = list1[i];
            list1[i] = list1[j];
            list1[j] = temp;
            print()

# Displaying elements of the array after sorting

print("Elements of array sorted in ascending order: ");
for i in range(0, len(list1)):
    print(list1[i], end=" ");

print("Converting the list to set :", set(list1))

dict1 = {
    'C': "Bhavani",
    'A': "s",
    'Z': "Vicky",
    'E': "Amman"
}
print("The original dictionary is : ", dict1)

# Sort Dictionary key and values List
# Using dictionary comprehension + sorted()
res = {key: sorted(dict1[key]) for key in sorted(dict1)}

# printing result
print("The sorted dictionary : " + str(res))

dict1={
    'C':"Bhavani",
    'A':"s",
    'Z':"Saravanan",
    'E':"Vignesh"
}
print("Original List :",dict1)
sort=sorted(dict1)
print("Sorted List :",sort)

# declaring a string variable
str =input("Enter Your Data")
# declaring an empty string variable for storing modified string
modified_str = ''

# iterating over the string
for char in range(0, len(str)):
# checking if the character at char index is equivalent to 'a'
    if(str[char] == 'a'):
    # append $ to modified string
        modified_str += '$'
    else:
        # append original string character
        modified_str += str[char]

print("Modified string : ")
print(modified_str)

# declaring a string variable
str1 =input("Enter Your Data")
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '')
  str1 = char + str1[1:]

  return str1

print(str.capitalize())

l=[26,5,21,6,5,26,6,87]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end= " ")


a=int(input("Enter a value :"))
b=int(input("Enter b value :"))
c=int(input("Enter c value :"))
sum= a+b+c
div= (a+b+c)/c
print("sum of three elements :",sum)
print("divided by a value",div )

#Swapping a and b
a=[3,5,7,9,11]
b=[1,6,5,8,9]
temp=0
print("Before Swapping is :",a,b)
for i in a,b :
    if a>b :
        temp=a;
        a=b;
        b=temp;
        print("After Swapping is :",a,b)

#program to convert an integer to binary & octa decimal
a=10
b=5
print("integer into binary is:",bin(a))
print("integer into octa decimal is :",oct(a))





