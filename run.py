import tkinter as tk
import tkinter.ttk as ttk

class MainWindow:

    def __init__(self,master):

        self.master = master

        self.ipLabel = tk.Label(root, text="IP Range: ")
        self.ipEntry1 = tk.Entry(root, width=15)
        self.toLabel = tk.Label(root, text="to")
        self.ipEntry2 = tk.Entry(root, width=15)
        self.startButton = tk.Button(root, text="start", width=7)

        self.sheet = ttk.Treeview(root)
        self.sheet["columns"] = ("one", "two")
        self.sheet.column("one", width=100)
        self.sheet.column("two", width=100)
        self.sheet.heading("one", text="column A")
        self.sheet.heading("two", text="column B")

        self.ipLabel.grid(column=0, row=0, padx=2, pady=2)
        self.ipEntry1.grid(column=1, row=0, padx=2, pady=2)
        self.toLabel.grid(column=2, row=0, padx=2, pady=2)
        self.ipEntry2.grid(column=3, row=0, padx=2, pady=2)
        self.startButton.grid(column=4, row =0, padx=2, pady=2)
        self.sheet.grid(column=0, row=1, padx=5, pady=5)


root = tk.Tk()
GUI = MainWindow(root)
root.mainloop()