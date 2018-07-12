import tkinter as tk


class MainWindow:

    def __init__(self,master):

        self.master = master

        self.ipLabel = tk.Label(root, text="IP Range: ")
        self.ipEntry1 = tk.Entry(root, width=15)
        self.toLabel = tk.Label(root, text="to")
        self.ipEntry2 = tk.Entry(root, width=15)
        self.startButton = tk.Button(root, text="start", width=7)
        self.T = tk.Text(root, height=10, width=45)

        self.ipLabel.grid(column=0, row=0, padx=2, pady=2)
        self.ipEntry1.grid(column=1, row=0, padx=2, pady=2)
        self.toLabel.grid(column=2, row=0, padx=2, pady=2)
        self.ipEntry2.grid(column=3, row=0, padx=2, pady=2)
        self.startButton.grid(column=4, row =0, padx=2, pady=2)
        self.T.grid(column=0, row=1, columnspan=5, padx=5, pady=5)


root = tk.Tk()
GUI = MainWindow(root)
root.mainloop()