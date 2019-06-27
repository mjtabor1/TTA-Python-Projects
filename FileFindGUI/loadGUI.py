from tkinter import *
import tkinter as tk
import functions


def load_gui(self):

    self.txtSource = tk.Entry(self.master, text='', width=52)
    source = self.txtSource
    self.txtSource.grid(row=0, column=1, padx=(30, 0), pady=(50, 0), sticky=NW)

    self.txtDest = tk.Entry(self.master, text='', width=52)
    destination = self.txtDest
    self.txtDest.grid(row=1, column=1, padx=(30, 0), pady=(10, 0), sticky=NW)

    self.btnSource = tk.Button(self.master, text='Source Directory', width=15, height=1,
                               command=lambda: functions.openDirectory(self, source))
    self.btnSource.grid(row=0, column=0, padx=(20, 0), pady=(50, 0))

    self.btnDest = tk.Button(self.master, text='Destination Directory', width=15, height=1,
                             command=lambda: functions.openDirectory(self, destination))
    self.btnDest.grid(row=1, column=0, padx=(20, 0), pady=(10, 0))

    self.btnCheck = tk.Button(self.master, text='Check for files...', width=15, height=3,
                              command=lambda: functions.move_file(self, source, destination))
    self.btnCheck.grid(row=2, column=0, padx=(20, 0), pady=(10, 0))

    self.btnClose = tk.Button(self.master, text='Close Program', width=15, height=3,
                              command=lambda: functions.ask_quit(self))
    self.btnClose.grid(row=2, column=1, padx=(20, 0), pady=(10, 0), sticky=E)

    functions.create_db(self)


if __name__ == "__main__":
    pass
