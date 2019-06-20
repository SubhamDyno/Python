from tkinter import *
import datetime
import tkinter.messagebox as tm

now = datetime.datetime.now()
Today = str(now)
def Submitted():
    print(f'The value submitted are {userval.get()} and {passval.get()}');
    display = tm.showinfo("Thanks","Visit Again");
    with open("./Logs/Tkinter.txt", "a") as f:
        f.write(f'{Today}\n-------------------------------------\nThe value entered : {userval.get()} with Password {passval.get()}\n')

root = Tk();

root.geometry(newGeometry = "600x300")

Label(root, text="Name", bg ="white" , fg="black", borderwidth=6).grid(row=0,column=0, sticky="w")
Label(root, text="Password", bg ="white" , fg="black", borderwidth=6).grid(row=1, column=0)


''' Varibales in Python - BooleanVar, DoubleVar, IntVar, StringVar '''
userval = StringVar();
passval = StringVar();

Entry(root, textvariable=userval, width=2).grid(row=0,column=1)
Entry(root, textvariable=passval).grid(row=1,column=1)

Checkbutton(root, text="Signed me always").grid(columnspan=2)

Button(root, text="SUBMIT", font="Helvetica 8 bold", padx=10,pady=10, command=Submitted).grid(row=3,columnspan=2);

root.mainloop()
