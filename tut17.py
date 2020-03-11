from tkinter import *

root=Tk()

root.geometry("644x344")
root.title("This is about menus")

def myfunc():
    print(f"it prints sth.")

# myMenu=Menu(root)
# myMenu.add_command(label="File",command=myfunc)
# # quit is inbuilt
# myMenu.add_command(label="Exit",command=quit)
# # to pack:
# root.config(menu=myMenu)


def myfunc():
    print(f"it has been saved")


def myfunc1():
    print("your text has been copied")

# We want dropdowns usually. So for that:-


mainmenu = Menu(root)
# tearoff used so that on clicking at --- it doesnt separate out
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="Save", command=myfunc)
m1.add_command(label="Copy", command=myfunc1)
# line comes,used when we need to separate commands
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


root.mainloop()