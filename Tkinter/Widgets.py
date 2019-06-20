from tkinter import *

root = Tk();

def Track(event):
    print(f"Hey You clicked me once at the coordinates <{event.x},{event.y}>")
root.geometry("500x800");

root.title("GUI Tkinter");

widget = Button(root, text="Click me once");
widget.pack();

widget.bind('<Button-1>', Track);
widget.bind('<Double-1>', quit);

root.mainloop();
