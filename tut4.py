# To learn to use labels
from tkinter import*

root = Tk()

# width x height
root.geometry("444x234")
# width,height
root.minsize(300,100)      # using this we cant minimise the window below a limit
# width,height
root.maxsize(1200,998)

Janvi=Label(text="Janvi is a good girl")
# Its imp to pack :-P
Janvi.pack()
root.mainloop()

