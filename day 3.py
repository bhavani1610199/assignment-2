#importing library
from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter import ttk
window = Tk()
#declarin window Title
window.title("Registration Screen")
#declaring Window size
window.geometry('300*300')
#declaring window color
window.configure(background = "green");
#declaring four fields 
Firstname =  Label(window,text = "First Name").grid(row = 0,column = 0)
Lastname =  Label(window,text = "Last Name").grid(row = 1,column = 0)
Email =  Label(window,text = "Email Id").grid(row = 2,column = 0)
Mobile =  Label(window,text = "Contact Number").grid(row = 3,column = 0)

Firstname1 =  Entry(window).grid(row = 0,column = 0)
Lastname1 =  Entry(window).grid(row = 1,column = 0)
Email1 =  Entry(window).grid(row = 2,column = 0)
Mobile1 =  Entry(window).grid(row = 3,column = 0)

#function declaration 
def clicked():
    res = "Welcome to"+txt.get()
    Ibl.configure(text=res)
btn = ttk.Button(window,text="Submit").grid(row=4,column=0)
window.mainloop()



