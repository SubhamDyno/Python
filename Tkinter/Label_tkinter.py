from tkinter import *


root = Tk();
''' TK() is the class for tkinter & root is the object assignment'''

mylabel1 = Label(root, text = "Hey! MY length is equal to the text length", bg="black", fg="white");
mylabel1.pack();

'''
Label is to set the Label for GUI
bg = Background Color
fg = foreground color
text= to display what is there in label
Label length depends on the text length
'''
mylabel2 = Label(root, text = "Hey! I can be strectched to X-axis", bg="Yellow", fg="Black");
mylabel2.pack(fill=X);
'''
fill = X : means it can be strechted to X direction as long as you strech the window
'''
mylabel3 = Label(root, text = "Hey! I can be strectched to Y-axis", bg="Green", fg="white");
mylabel3.pack(side=LEFT,fill=Y);

'''
fill = Y : means it can be strechted to Y direction as long as you strech the window
'''

root.mainloop();
