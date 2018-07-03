#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 10:14:52 2018

@author: qpetit
"""

# Python 3
import tkinter as tk
from tkinter import filedialog
 
class App(tk.Tk):
 
    def __init__(self):
        tk.Tk.__init__(self)
        self.initWidgets()
 
    def initWidgets(self):
        self.bt = tk.Button(self, text="Ouvrir fichier", command=self.openFile)
        self.bt.grid(row=0, column=0)
 
        self.text = tk.Text(self, width=80, height=30)
        self.text.grid(row=1, column=0)
 
    def openFile(self):
        filepath = filedialog.askopenfilename(filetypes=[('txt files','.txt')])
 
        with open(filepath, 'r') as FILE:
            content = FILE.read()
 
        self.text.insert("end", content)
 
#------------------------------------------------------------------------------
if __name__ == '__main__':
    app = App()
    app.mainloop()