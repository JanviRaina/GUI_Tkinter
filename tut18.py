# Message box in Tkinter
from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("644x344")
root.title("This is about menus")

def myfunc():
    print(f"it prints sth.")

def myfunc1():
    print(f"it has been saved")

def help():
    print("i will help you ")
    tmsg.showinfo("Help","jen can help you")

def rate():
    print("Rate us")
    #in askquestion 1st argument will five value on top and second value next to question mark
    value=tmsg.askquestion("Would you like to continue further?","Now press Yes or No")
    if value=="yes":
        msg="Thanks for that"
    else:
        msg="you can try other options."
    tmsg.showinfo("ok",msg)

def pro():
    ans=tmsg.askyesnocancel("want to go ahead?","like to have thrills? ")
    if ans:
        print("ok")
    else:
        print("good that u cancelled")


mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="Save", command=myfunc)
m1.add_command(label="Copy", command=myfunc1)
m1.add_separator()
m1.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc1)
m2.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate Us",command=rate)
m3.add_command(label="Proposal",command=pro)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help", menu=m3)


root.mainloop()