# Adding buttons to our GUI

from tkinter import *

root=Tk()

root.geometry("233x444")

def name():
    print("janvi")

frame=Frame(root,borderwidth=5,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1=Button(frame,fg="red",text="Click Me")
b1.pack()


b2 = Button(frame, fg="red", text="Tell me name now", command=name)
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg="red", text="Print now")
b3.pack(side=LEFT, padx=23)

b4 = Button(frame, fg="red", text="Print now")
b4.pack(side=LEFT, padx=23)


root.mainloop()