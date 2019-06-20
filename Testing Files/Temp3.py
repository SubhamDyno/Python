import tkinter as Tkinter
import random

class App:
    def __init__(self, master):

        frame = Tkinter.Frame(master)

        self.data_readout = Tkinter.Button(frame, text="Collect Data", bd=10, height=2, width=10, command=lambda: self.dataReadout(self.table_values))
        self.data_readout.grid(row=0, column=0, padx=5, pady=5)

        self.table_values = Tkinter.LabelFrame(frame, text="Values", borderwidth=10, relief=Tkinter.GROOVE, padx=10, pady=10)
        self.table_values.grid(row=1, column=0, padx=20, pady=20)

        for i in range(4): #Rows
            for j in range(10): #Columns
                b = Tkinter.Entry(self.table_values, text="", width=10,bg="green")
                b.grid(row=i, column=j)
                b.insert(0, str(round(random.random()*100)))

        frame.grid(row=0, column=0, padx=20, pady=20)

    def dataReadout(self, frame):
        #returns Dict of row and column
        pass


if __name__ == "__main__":
    root = Tkinter.Tk()
    app = App(root)
    root.mainloop()        
