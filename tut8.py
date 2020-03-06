# FRAME IN TKINTER

# In a website we use div similarly here in GUI -> FRAME

from tkinter import *

root=Tk()

root.geometry("233x555")
root.title("Raina")
f=Frame(root,bg="green",borderwidth=6,relief=SUNKEN)
f.pack(side=LEFT,fill="y")

f2=Frame(root,bg="blue",borderwidth=3,relief=SUNKEN)
f2.pack(side=TOP,fill="x")
l=Label(f2,text="WELCOME all")
l.pack()


label=Label(f,text="Frames in GUI",font="Helvetica 16 bold", fg="red", pady=22)
label.pack(padx=6,pady=4)
root.mainloop()

