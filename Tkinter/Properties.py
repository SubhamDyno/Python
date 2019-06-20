from tkinter import *

root = Tk();

root.geometry(newGeometry = "600x300")

Label(root, text="My window", bg ="lightgreen" , fg="black", relief = "groove", borderwidth=6).pack(side=LEFT, fill="x", pady =20)

root.mainloop()
