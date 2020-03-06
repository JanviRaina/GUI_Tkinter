# CHECKBOXES AND TAKING VALUES
from tkinter import *
root=Tk()
root.geometry("655x333")


def getvals():
    print("It works!")

# Heading
Label(root,text="Welcome to Tution Classes",font="comicsansns 13 bold",pady=6).grid(row=0,column=1)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
subject=Label(root,text="Subject")
gender=Label(root,text="Gender")
payment_mode=Label(root,text="paymentMode")

# Packed using grid
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
subject.grid(row=3,column=2)
gender.grid(row=4,column=2)
payment_mode.grid(row=5,column=2)

# Variables taken
nameValue=StringVar()
phoneValue=StringVar()
subjectValue=StringVar()
genderValue=StringVar()
payment_modeValue=IntVar()
check=IntVar()

# Entry for our form
nameentry=Entry(root,textvariable=nameValue)
phoneentry=Entry(root,textvariable=phone)
subjectentry=Entry(root,textvariable=subjectValue)
genderentry=Entry(root,textvariable=genderValue)
payment_modeentry=Entry(root,textvariable=payment_modeValue)

# Packing entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
subjectentry.grid(row=3,column=3)
genderentry.grid(row=4,column=3)
payment_modeentry.grid(row=5,column=3)


#Checkbox & Packing it
checking= Checkbutton(text="Are you a member already", variable = check)
checking.grid(row=6, column=3)

#Button & packing it and assigning it a command
Button(text="Submit to class", command=getvals).grid(row=7, column=3)


root.mainloop()