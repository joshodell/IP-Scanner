import tkinter as tk


class MainWindow():

    def __init__(self,master):

        self.master = master

        self.ipLabel = tk.Label(self, text="IP Range: ")
        self.ipEntry1 = tk.Entry(self)
        self.toLabel = tk.Label(self, text="to")
        self.ipEntry2 = tk.Entry(self)

        self.ipLabel.grid(column=0, row=0, padx=2, pady=2)
        self.ipEntry1.grid(column=1, row=0, padx=2, pady=2)
        self.toLabel.grid(column=2, row=0, padx=2, pady=2)
        self.ipEntry2.grid(column=3, row=0, padx=2, pady=2)


def main():
    root = tk.Tk()
    GUI = MainWindow(root)
    root.mainloop()