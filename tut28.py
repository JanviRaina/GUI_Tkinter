from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.0,END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',
                               filetypes=[("All Files", "*.*"),
                                          ("Text Documents", "*.txt")]
                               )
        if file=="":
            file=None
        else:
            # Save a file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()



def quitFile():
    root.destroy()
def cut():
    # Tkinter handles this on its own. Cut Copy Paste "<<Event>>"
    TextArea.event_generate("<<Cut>>")
def copy():
    TextArea.event_generate("<<Copy>>")
def paste():
    TextArea.event_generate("<<Paste>>")
def about():
    # For showinfo we need to import showinfo from message box.Its first argument is title
    showinfo("Notepad","This is a notepad by Janvi")


if __name__ == '__main__':
    # Basic tkinter setup
    root=Tk()
    root.geometry("544x346")
    root.title("My Notepad")
    root.tk.call('wm','iconphoto',root._w,PhotoImage(file='2.png'))
    # Adding text area
    TextArea=Text(root,font="lucida 16 italic")
    file=None
    TextArea.pack(expand=True,fill=BOTH)

    # lets create a menubar
    MenuBar=Menu(root)
    # File menu starts here
    FileMenu=Menu(MenuBar,tearoff=0)
    # To add a new file:
    FileMenu.add_command(label="New",command=newFile)
    # To open a file:
    FileMenu.add_command(label="Open",command=openFile)
    # To save a new file:
    FileMenu.add_command(label="Save",command=saveFile)
    # FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitFile)
    MenuBar.add_cascade(label="File",menu=FileMenu)
    # File menu ends here

    # Edit menu starts here
    EditMenu=Menu(MenuBar,tearoff=0)
    # Feature of cut copy paste
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    # Edit menu ends here

    # Help menu starts here

    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    # Help menu ends here
    root.config(menu=MenuBar)

    #Adding Scrollbar using rules from Tkinter lecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()