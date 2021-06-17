# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#dictionary
capitals ={"tamil nadu" : "chennai","karnataka":"bengaluru","bihar":"patna"}
print(capitals)
print(capitals["tamil nadu"])
print(capitals["bihar"])
#length
print(len(capitals))
#type
print(type(capitals))
#keys
x=capitals.get("model")
print(x)
x=capitals.keys()
print(x)
#changing values

dress = {
    "brand": "myntra",
    "type":"tops",
    "color":"pink",
    "price":550
}
x = dress.keys()
print(x)
dress["color"] = "blue"
print(x)
#values changing
x = dress.values()
print(x)
dress["price"]=650
print(x)
#update
dress.update({"price":750})
print(dress)
#pop
dress.pop("type")
print(dress)
#clear
dress.clear()
print(dress)
#copy
dress.copy()
print(dress)


for x in capitals.values():
    print(x)

for x in capitals.keys():
    print(x)

#sets
x = {"dhoni","virat","bravo"}
print(x)
#update
x = {"dhoni","virat","bravo"}
y = {"bhavi","vicky","abi"}
x.update(y)
print()
#remove
x = {"dhoni","virat","bravo"}
x.remove("virat")
print(x)
#exercise 1
x = {"dhoni","virat","bravo"}
y = {"bhavi","vicky","abi"}
x1 =x.copy()
x1.update(y)
print(x1)
#exercise 2
x = {"dhoni","virat","bravo"}
x.remove("bravo")
print(x)
#exercise 3
x = ["red","blue","green"]
y = ["101","102","103"]
color_dictionary = dict(zip(x,y))
print(color_dictionary)
#exercise 4
setn = {5, 10, 3, 15, 2, 20}
print("Original set elements:")
print(setn)
print(type(setn))
print("\nLength of the said set:")
print(len(setn))
#exercise 5
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("\nRemove the intersection of a 2nd set from the 1st set using difference_update():")
sn1.difference_update(sn2)
print("sn1: ",sn1)
print("sn2: ",sn2)






