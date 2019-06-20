from tkinter import *

root = Tk();

height=200;
width=100;

canvas = Canvas(root,height=height,width=width);
canvas.pack();
canvas.create_line(0,200, 200, 200);

canvas.create_rectangle(100,100,50,50);

canvas.create_oval(100,100,50,50)

root.mainloop();

