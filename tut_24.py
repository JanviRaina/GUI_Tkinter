# statusbar
from tkinter import *

def upload():
    statusvar.set("Busy...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")

root=Tk()
root.geometry("548x457")
root.title("Statusbars")

statusvar=StringVar()
statusvar.set("Ready")

# fill=X so that it spreads in x
# anchor=w  so that text comes in west or left side
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(fill=X,side=BOTTOM)
Button(root,text="Upload",command=upload).pack()



root.mainloop()