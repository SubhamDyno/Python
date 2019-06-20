from tkinter import *
root = Tk();

mylabel1 = Label(root, text="Name")
mylabel2 = Label(root, text="Password")

myentry1 = Entry(root, bg="#00ffff")
myentry2 = Entry(root, bg="#00ffff")

'''
Entry is the blank label to enter user input
'''

mylabel1.grid(row=0, column=0, sticky=E)
''' column is default zero '''
mylabel2.grid(row=1)

myentry1.grid(row=0, column=1)
myentry2.grid(row=1, column=1)

mycheck = Checkbutton(root, text="Keep me signed in")
mycheck.grid(row=3,columnspan=2)
