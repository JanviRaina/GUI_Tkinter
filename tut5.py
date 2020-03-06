# how we can use image
# its also a label with which user cant interact
from tkinter import *
from PIL import Image,ImageTk

# python image library
root=Tk()
root.geometry("233x444")
# photo=PhotoImage(file="fairy.png")
# for jpg images
# since it doesnt support jpg file format sow e hv to do these formalities like installing pillow nd writing in this way
image=Image.open("fairy.jpg")
photo=ImageTk.PhotoImage(image)
# we hv to put it in label
label=Label(image=photo)
label.pack()
root.mainloop()
