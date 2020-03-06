# FRAME IN TKINTER

# In a website we use div similarly here in GUI -> FRAME

from tkinter import *

root=Tk()

root.geometry("233x555")
root.title("Frames in")
label=Label(text="this is label")
label.pack()
f=Frame(root,width="200",height="100")

root.mainloop()

