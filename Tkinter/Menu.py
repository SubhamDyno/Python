from tkinter import *
root = Tk();

def Do_it():
    print(" We are under Submenu - 1")


def Do_Edit():
    print(" We are under Submenu - 2")
    
root.geometry(newGeometry = "600x300")

Mainmenu = Menu(root);
Submenu1 = Menu(Mainmenu)
Submenu1.add_command(label="New File",command=Do_it);
Submenu1.add_command(label="Open",command=Do_it);
Submenu1.add_separator()
Submenu1.add_command(label="Save as...",command=Do_it);
Submenu1.add_command(label="Save copy as...",command=Do_it);
Submenu1.add_separator()
Submenu1.add_command(label="Close",command=quit);

Mainmenu.add_cascade(label="File", menu=Submenu1)


Submenu2 = Menu(Mainmenu)
Submenu2.add_command(label="Undo",command=Do_Edit);
Submenu2.add_command(label="Redo",command=Do_Edit);
Submenu2.add_command(label="Cut",command=Do_Edit);
Submenu2.add_command(label="Paste",command=Do_Edit);
Submenu2.add_separator()
Submenu2.add_command(label="Quit",command=quit);

Mainmenu.add_cascade(label="Edit", menu=Submenu2)
root.config(menu=Mainmenu)
