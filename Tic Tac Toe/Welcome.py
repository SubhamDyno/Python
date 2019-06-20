import tkinter as tk

class window2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("750x500")
        panel2 = tk.Frame(self)
        panel2.grid()
        tk.Button(panel2,text="Button").grid()
        text1 = tk.Entry(panel2)
        text1.grid()
        text1.focus()
        self.bind("<1>", self.set_focus)

    def set_focus(self, event=None):
        x, y = self.winfo_pointerxy()
        self.winfo_containing(x, y).focus()


window2().mainloop()
