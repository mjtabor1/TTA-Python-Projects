from tkinter import *
import tkinter as tk
import phonebook_main
import phonebook_functions


def load_gui(self):  # passing in self give us access to the class ParentWindow
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
    """
    # CREATE AND PLACE ALL OF OUR LABELS IN THE GUI
    self.lbl_fname = tk.Label(self.master, text='First Name:')  # access the tkinter module(Label())
    self.lbl_fname.grid(row=0, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)  # places the label on the grid
    self.lbl_lname = tk.Label(self.master, text='Last Name:')
    self.lbl_lname.grid(row=2, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lbl_phone = tk.Label(self.master, text='Phone Number:')
    self.lbl_phone.grid(row=4, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lbl_email = tk.Label(self.master, text='Email Address:')
    self.lbl_email.grid(row=6, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lbl_info = tk.Label(self.master, text='Information:')
    self.lbl_info.grid(row=0, column=2, padx=(0, 0), pady=(10, 0), sticky=N + W)

    # CREATE AND PLACE ALL OF OUR TEXT-BOXES IN THE GUI
    self.txt_fname = tk.Entry(self.master, text='')
    self.txt_fname.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N + E + W)
    self.txt_lname = tk.Entry(self.master, text='')
    self.txt_lname.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N + E + W)
    self.txt_phone = tk.Entry(self.master, text='')
    self.txt_phone.grid(row=5, column=0, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N + E + W)
    self.txt_email = tk.Entry(self.master, text='')
    self.txt_email.grid(row=7, column=0, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N + E + W)

    # CREATE THE LISTBOX AND SCROLLBAR AND PLACE THEM IN THE GUI
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.lstList1 = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar1.set)
    # function that gets called upon a click within the list bos(ListboxSelect), using the bind() method
    self.lstList1.bind('<<ListboxSelect>>', lambda event: phonebook_functions.onSelect(self, event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1, column=5, rowspan=7, columnspan=1, padx=(0, 0), pady=(0, 0), sticky=N + E + S)
    self.lstList1.grid(row=1, column=2, rowspan=7, columnspan=3, padx=(0, 0), pady=(0, 0), sticky=N + E + S + W)

    # CREATE AND PLACE ALL OF OUR BUTTONS IN THE GUI
    # EACH BUTTON CALLS UPON A FUNCTION(command=lambda: functionName)
    self.btn_add = tk.Button(self.master, width=12, height=2, text='Add',
                             command=lambda: phonebook_functions.addToList(self))
    self.btn_add.grid(row=8, column=0, padx=(25, 0), pady=(45, 10), sticky=W)
    self.btn_update = tk.Button(self.master, width=12, height=2, text='Update',
                                command=lambda: phonebook_functions.onUpdate(self))
    self.btn_update.grid(row=8, column=1, padx=(15, 0), pady=(45, 10), sticky=W)
    self.btn_delete = tk.Button(self.master, width=12, height=2, text='Delete',
                                command=lambda: phonebook_functions.onDelete(self))
    self.btn_delete.grid(row=8, column=2, padx=(15, 0), pady=(45, 10), sticky=W)
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close',
                               command=lambda: phonebook_functions.ask_quit(self))
    self.btn_close.grid(row=8, column=4, columnspan=1, padx=(15, 0), pady=(45, 10), sticky=E)

    # CALLING SOME FUNCTIONS(create_db & onRefresh) FROM(phonebook_functions)
    phonebook_functions.create_db(self)
    phonebook_functions.onRefresh(self)


if __name__ == "__main__":
    pass
