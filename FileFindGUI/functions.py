import os
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import tkinter as tk
import sqlite3
import shutil


def openDirectory(self, source):
    if source.get() != '':
        source.delete(0, END)
    directory = tk.filedialog.askdirectory()
    source.insert(0, directory)


def move_file(self, source, destination):
    count = 0
    source = source.get()
    dest = destination.get()
    if (source == '') or (dest == ''):
        tk.messagebox.showerror('Folder Error', 'Please select a path for both folders')
    elif source == dest:
        tk.messagebox.showerror('Folder Error', "Source and destination can't be the same.")
    else:
        list_files = os.listdir(source)
        for i in list_files:
            pair = []
            currentFile = i

            if currentFile.endswith('.txt'):
                pair.append(currentFile)
                filepath = os.path.join(source, currentFile)
                pair.append(os.path.getmtime(filepath))
                shutil.move(filepath, dest)
                fileName = pair[0]
                time = pair[1]
                print(pair)
                addToDB(self, fileName, time)
                destination.delete(0, END)
                count += 1

        if count == 0:
            tk.messagebox.showinfo('File info', 'There were no text files to move in the directory')


def create_db(self):
    conn = sqlite3.connect("db_textfiles.db")
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_fileName TEXT, \
                    col_time REAL \
                    );")
        conn.commit()
    conn.close()


def addToDB(self, fileName, time):
    conn = sqlite3.connect("db_textfiles.db")
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_files (col_fileName, col_time) VALUES(?,?)", (fileName, time))
        conn.commit()
    conn.close()


def ask_quit(self):
    self.master.destroy()
    os._exit(0)
