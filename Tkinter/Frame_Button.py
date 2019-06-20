from tkinter import *


root = Tk();
''' TK() is the class for tkinter & root is the object assignment'''

myframe = Frame(root);
myframe.pack(side=BOTTOM)

'''
Frame is to create different frame to place different widgets into different frames
'''

mybotton2 = Button(root,text = "Click Me!!", fg="red");
mybotton2.pack(side=RIGHT);

'''
For the above Button , Button is in buttom frame  and is present in left side
While defining the 'side' input should be in captital letters i.e LEFT, RIGHT, TOP, BOTTOM
'''

root.mainloop();

'''
mainloop() to keep the prog into the continuos loop
It is not required in this python version
'''
