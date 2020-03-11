from tkinter import *

root=Tk()

root.geometry("655x444")
root.title("Functions")
#
# root.wm_iconbitmap("1.ico")   # not working
# Setting icon like this :-
root.tk.call('wm','iconphoto',root._w,PhotoImage(file='1.png'))
root.config(background="grey")


width=root.winfo_screenmmwidth()
height=root.winfo_screenheight()

print(f"the height is {height} and width is {width}")

Button(text="Close",command=root.destroy).pack()

root.mainloop()