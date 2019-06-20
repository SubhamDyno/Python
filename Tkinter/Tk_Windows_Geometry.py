from tkinter import *

root1 = Tk()
root2=Tk()

'''
Geometry will set the Tkinter window to the desirable size
Syntax - var.geometry("widthxheight+x+y)
'''

root1.geometry("500x200")

'''
minsize decides the min size windows can shrink and
maxsize will decide max size the window can extend
'''

root1.minsize(300,100)
root1.maxsize(800,400)


A = Label(root1, text="I am in root1")
A.pack()

root2.geometry(newGeometry="722x344+20+40")
B = Label(root2, text="I am in root2")
B.pack()

