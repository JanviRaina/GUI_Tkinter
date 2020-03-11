# This one is about radiobuttons
from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()

root.geometry("544x543")
root.title("Radiobuttons etc")

def order():
    tmsg.showinfo("Order Received!", f"We have received your order for {var.get()}. Thanks for ordering")


# var=IntVar()
# to set an initial value
# var.set(1)
var=StringVar()
var.set("Radio")
Label(root,text="What would you like to have mam?",justify=LEFT,font="lucida 19 italic",pady=18).pack()
radio=Radiobutton(text="Idli",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(text="Dosa",padx=14,variable=var,value="Idli").pack(anchor="w")
radio=Radiobutton(text="Paneer Fry",padx=14,variable=var,value="Paneer Fry").pack(anchor="w")


Button(text="Order Now", command=order).pack()

root.mainloop()