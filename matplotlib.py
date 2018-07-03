#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 09:04:23 2018

@author: qpetit
"""

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
 
app = tk.Tk()
app.wm_title("Graphe Matplotlib dans Tkinter")
 
fig = Figure(figsize=(6, 4), dpi=96)
ax = fig.add_subplot(111)
ax.plot(range(10), [5, 4, 2, 6, 9, 8, 7, 1, 2, 3])
 
graph = FigureCanvasTkAgg(fig, master=app)
canvas = graph.get_tk_widget()
canvas.grid(row=0, column=0)
 
app.mainloop()
        