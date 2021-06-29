# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):

f.open("myfile.txt","a")
f.close()



#Writing a File
f=open("myfile.txt","w")
L=["This is bhavi \n","CSE \n"]
f.write("Anna university \n")
f.writelines(L)
f.close()
f=open("myfile.txt", "r+")
print("Output of the file when read and write")
print(f.read())
print

# seek(n) takes the file handle to the nth
f.seek(10)
print("The Output of file when readlines")
print(f.readline(10))
print(f.close())




#Appending-will add the element at last
file1=open("myfile.txt","a")
L=["Today \n"]
file1.writelines(L)
print("The Output of the File After Appending")

file1=open("myfile.txt","r")
print(file1.read())
file1.close()


#Task :
file2=open("30 days 30 hour operations.txt","w")
file2.write("I have completed 10 days successfully \n")
print("The Output Of The Task :")
file2=open("30 days 30 hour operations.txt","a")
file2.write("B HARSHA VARDHAN REDDY")
file2=open("30 days 30 hour operations.txt","r")
print(file2.read())
file2.close()














