# Python Version: 3.7.3
#
# Author: Michael Tabor
#
# Purpose: Phonebook App. Demonstrating OOP, Tkinter GUI module,
#          using Tkinter Parent and Child relationships. Utilizes sqlite3 for dB.


from tkinter import *
import tkinter as tk
import phonebook_gui
import phonebook_functions


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # DEFINE OUR MASTER FRAME CONFIGURATION
        self.master = master
        self.master.minsize(500, 300)
        self.master.maxsize(500, 300)
        # CenterWindow METHOD WILL CENTER OUR APP ON THE USER'S SCREEN
        phonebook_functions.center_window(self, 500, 300)
        self.master.title("The Tkinter Phonebook App")
        self.master.configure(bg='#F0F0F0')
        # THIS protocol() METHOD IS A TKINTER METHOD TO CATCH IF THE USER
        # CLICKS THE UPPER CORNER, 'X' ON WINDOWS OS
        self.master.protocol('WM_DELETE_WINDOW', lambda: phonebook_functions.ask_quit(self))
        arg = self.master

        # LOAD IN THE GUI WIDGETS FROM A SEPARATE MODULE, KEEPING YOUR CODE
        # COMPARTMENTALIZED AND CLUTTER FREE
        phonebook_gui.load_gui(self)


if __name__=='__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

