# Entry Widget and Grid Layout

from tkinter import *
root=Tk()
root.geometry("655x333")

def getvals():
    print(f"the value of username is{uservalue.get()}")
    print(passvalue.get())


user=Label(root,text="Username")
password=Label(root,text="Password")

# grid used for packing

user.grid()
password.grid(row=1)

# Entry widget is like textarea in js
# Variable classes in Tkinter:
# BooleanVar  DoubleVar  StringVar inVar

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)

# packing using .grid() instead of .pack()

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

# lets modify it by using buttons

Button(text="Sumbit",command=getvals).grid()

root.mainloop()