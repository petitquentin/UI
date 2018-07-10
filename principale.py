#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:42:00 2018

@author: qpetit
"""

import PIL.Image
import PIL.ImageTk
import os
import re
import random
import numpy as np
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from decimal import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg


#Importation des fichiers .py présent dans le dossier 
from get_path import read_file_path
from files import read_files, open_file, save_file
from reset import reset_window
from graph import generate_graph
from settings import setting_canvas


def alert():
    messagebox.showinfo("Say Hello", "Hello World")
    
    
def mise_a_jour_interface():
    fichier1 = read_file_path(1)
    fichier2 = read_file_path(2)
   
    
    #Nettoyage du canves affichant les adresses
    can.delete(ALL)
    
    #Ici, on regarde si le chemin du fichier est vide, si c'est le cas, on affiche un message d'attention, sinon on affiche le chemin du fichier.
    if fichier1 != "":
        text_1=can.create_text(400,10,text=fichier1,fill="black")
    else:
        text_1=can.create_text(400,10,text="Warning : No original file selected",fill="red")
    if fichier2 != "":
        text_2=can.create_text(400,30,text=fichier2,fill="black")
    else: 
        text_2=can.create_text(400,30,text="Warning : No final file selected",fill="red")
    fenetre.update_idletasks()


    
    
def affichage_fichier():
    
    
    dimension = read_files()
    if dimension < 1 :
        return
    graphique = generate_graph(dimension)
    try:
        i = 0
        with open("sys/window.reso", "r") as f:
            for line in f.readlines():
                donnees = line.split()
                donnees[0] = int(donnees[0])
                if i == 0 :
                    h = donnees[0]
                else:
                    l = donnees[0]  
                i = i + 1
                
    except FileNotFoundError:
        messagebox.showerror("Error","Can not find windows.reso file")
        return
    
    
    

    
    if graphique == True :
        can_plot.delete(ALL)
        graph_origin = PIL.Image.open('data/graphic_brut.png')
        graph_reduit = graph_origin.resize((h,l))        
        img = PIL.ImageTk.PhotoImage(graph_reduit)
        dic['image']= img
        item = can_plot.create_image(h/2, l/2, image=img)
#        mon_image=PhotoImage(file=r"smiley.gif")
#        dic['image']= mon_image
#        img=can_plot.create_image(250,250,image=mon_image)
        
        fenetre.update_idletasks()
        fenetre.update()
        menubar.entryconfigure(2, state=NORMAL)
        
    else:
        messagebox.showerror("Error","Can not display the graphic")

        


                        
                        
    
    

def ouvrir_fichier1():
    open_file(1)
    mise_a_jour_interface()
    
    
    
def ouvrir_fichier2():
   open_file(2)
   mise_a_jour_interface()

def reset_window_launcher():
    reset_window(can, can_plot, menubar)
    
    
def about():
    messagebox.showinfo("About...", "Implementation of a user interface for the SMG2S project: https://github.com/brunowu/SMG2S")
    return


#On ouvre la fenetre graphique de TKinter
fenetre = Tk()
fenetre.title("UI SMG2S")
fenetre.configure(bg = "white")
dimension = 0
dic={}

def set_canvas_launcher():
    setting_canvas(fenetre)




menubar = Menu(fenetre)
#On créé le menu déroulant 1 : Fichier
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Open original file", command=ouvrir_fichier1)
menu1.add_command(label="Open final file", command=ouvrir_fichier2)
menu1.add_separator()
menu1.add_command(label="Run & display", command=affichage_fichier)
menu1.add_separator()
menu1.add_command(label="Reset", command=reset_window_launcher)
menu1.add_command(label="Exit", command=fenetre.quit)
menubar.add_cascade(label="File", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Save", command=save_file)
menubar.add_cascade(label="Save", menu=menu2)

#On créé le menu déroulant 3 : paramètres
menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Canvas", command=set_canvas_launcher)
menubar.add_cascade(label="Settings", menu=menu3)

#On créé le menu déroulant 4 : Aide
menu4 = Menu(menubar, tearoff=0)
menu4.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=menu4)

fenetre.config(menu=menubar)

can=Canvas(fenetre,width=800,height=40,background='white')
can.pack()
can_plot=Canvas(fenetre,width=800,height=600,background='white')
can_plot.pack()
reset_window_launcher()

#ouverture_menu(fenetre)

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()

