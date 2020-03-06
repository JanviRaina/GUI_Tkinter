# FRAME IN TKINTER

# In a website we use div similarly here in GUI -> FRAME

from tkinter import *

root=Tk()

root.geometry("233x555")
root.title("Raina")
f=Frame(root,bg="green",borderwidth=6,padx=7,pady=5)
f.pack(side=LEFT)
label=Label(f,text="Frames in GUI")
label.pack()
root.mainloop()

