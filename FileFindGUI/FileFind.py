import loadGUI
import tkinter as tk
from tkinter import *


class ParentWindow(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.minsize(500, 200)
        self.master.maxsize(500, 200)
        self.master.title('File find & replace')

        loadGUI.load_gui(self)


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
