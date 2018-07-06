#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:42:00 2018

@author: qpetit
"""

import PIL.Image
import PIL.ImageTk
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

def alert():
    messagebox.showinfo("Say Hello", "Hello World")

def mise_a_jour_interface():
    can.delete(ALL)
    if fichier1 != "":
        text_1=can.create_text(400,10,text=fichier1,fill="black")
    else:
        text_1=can.create_text(400,10,text="No original file selected",fill="red")
    if fichier2 != "":
        text_2=can.create_text(400,30,text=fichier2,fill="black")
    else: 
        text_2=can.create_text(400,30,text="No final file selected",fill="red")
    fenetre.update_idletasks()

def generation_graphe():
    global fichier1
    global fichier2
    global reel1
    global imaginaire1
    global reel2
    global imaginaire2
    global dimension
    global graphique
    
    plt.figure(1, figsize=(8, 6))
    plt.subplot(1, 1, 1)
    if dimension == 2:
        if fichier1 != "":
            plt.scatter(reel1, imaginaire1, c = 'black', marker = 'o')
            graphique = True
        if fichier2 != "":
            plt.scatter(reel2, imaginaire2, c = 'red', marker = '+')
            graphique = True
        
    else:
        if dimension == 1:
            
            if fichier1 != "":
                plt.scatter(reel1, imaginaire1, c = 'black', marker = 'o')
                graphique = True
            if fichier2 != "":
                plt.scatter(reel2, imaginaire2, c = 'red', marker = '+')
                graphique = True
    if graphique == True :
        plt.savefig('data/graphic_brut.png', dpi=1000)
        plt.show()
    
    
def affichage_fichier():
    global graphique
    
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
        messagebox.showwarning("Error","Can not find windows.reso file")
        return
    
    
    if graphique == True :
        can_plot.delete(ALL)
        graph_origin = PIL.Image.open('data/graphic_brut.png')
        graph_reduit = graph_origin.resize((h,l))
        
        img = PIL.ImageTk.PhotoImage(graph_reduit)
        item = can_plot.create_image(0, 0, image=img)
        can_plot.pack()
        fenetre.update_idletasks()
        fenetre.update()
        
    else:
        messagebox.showwarning("Error","Can not display the graphic")

        
def lecture_fichier():
    global fichier1
    global fichier2
    global reel1
    global imaginaire1
    global reel2
    global imaginaire2
    global dimension
    exp = r"[0-9]+(\.)?[0-9]*"
    # Booléen qui permet de stocker si on a déjà rencontré la ligne de la dimension.
    premiere_ligne = False
    if fichier1 == "" and fichier2 == "" :
        messagebox.showwarning("Erreur","Aucun fichier n'a été ouvert")
    else:
        if fichier1 != "":
            with open(fichier1, "r") as f:
                for line in f.readlines():
                    donnees = line.split()
                    
                    #On regarde si le premier caractère n'est pas un espace est un chiffre
                    print(re.match(exp, donnees[0]))
                    if re.match(exp, donnees[0]) is not None:
                        if premiere_ligne == False:
                            premiere_ligne = True
                            dimension = 0
                            for x in line.split(" "):
                                if re.match(exp, x):
                                    dimension += 1
                            dimension = dimension - 1
                            print("Dimension : ", dimension, "premiere_ ligne : ", premiere_ligne)
                            #On créé les vecteurs qui stockera les informations a afficher
                            reel1 = []
                            imaginaire1 = []
                            
                        else:
                            reel1.append(Decimal(donnees[1]))
                            if dimension == 2:
                                imaginaire1.append(Decimal(donnees[2]))
                            else:
                                imaginaire1.append(0)
                                
            np.savetxt(r'data/r1.vec', reel1)
            np.savetxt(r'data/i1.vec', imaginaire1)
            messagebox.showinfo("Information","Chargement fichier 1 semble ok!")
        else:                
            messagebox.showwarning("Erreur","Le fichier 1 n'est pas chargé")   
        
        
        premiere_ligne = False
        if fichier2 != "":
            with open(fichier2, "r") as f:
                for line in f.readlines():
                    donnees = line.split()
                    
                    #On regarde si le premier caractère n'est pas un espace est un chiffre
                    print(re.match(exp, donnees[0]))
                    if re.match(exp, donnees[0]) is not None:
                        if premiere_ligne == False:
                            premiere_ligne = True
                            dimension = 0
                            for x in line.split(" "):
                                if re.match(exp, x):
                                    dimension += 1
                            dimension = dimension - 1
                            print("Dimension : ", dimension, "premiere_ ligne : ", premiere_ligne)
                            #On créé les vecteurs qui stockera les informations a afficher
                            reel2 = []
                            imaginaire2 = []
                            
                        else:
                            reel2.append(Decimal(donnees[1]))
                            print("tableau reel : ",reel2)
                            if dimension == 2:
                                imaginaire2.append(Decimal(donnees[2]))
                                print("tableau imaginaire : ",imaginaire2)
                            else:
                                imaginaire1.append(0)
                                
            np.savetxt(r'data/r2.vec', reel2)
            np.savetxt(r'data/i2.vec', imaginaire2)
            messagebox.showinfo("Information","Chargement fichier 2 semble ok!")
        else:                
            messagebox.showwarning("Erreur","Le fichier 2 n'est pas chargé")
        generation_graphe()
        affichage_fichier()


                        
                        
    
    

def ouvrir_fichier1():
    global graphique
    global fichier1 
    fichier_precedent = fichier1
    fichier1 = filedialog.askopenfilename(filetypes=[('Fichier Texte','.txt')])
    if fichier_precedent != fichier2 :
        graphique = False
    if fichier2 == "" and fichier1 != "":
        answer = messagebox.askyesno("Ouvrir fichier Final","Voulez-vous ouvrir le fichier Final maintenant ?")
        if answer == True:
            ouvrir_fichier2()
    mise_a_jour_interface()
    
    
def ouvrir_fichier2():
    global graphique
    global fichier2
    fichier_precedent = fichier2
    fichier2 = filedialog.askopenfilename(filetypes=[('Fichier Texte','.txt')])
    if fichier_precedent != fichier2 :
        graphique = False
    if fichier1 == "" and fichier2 != "":
        answer = messagebox.askyesno("Ouvrir fichier Initial","Voulez-vous ouvrir le fichier Initial maintenant ?")
        if answer == True:
            ouvrir_fichier1
    mise_a_jour_interface()
    
def reinitialisation():
    global graphique
    global fichier1, fichier2
    fichier1 = ""
    fichier2 = ""
    can.delete(ALL)
    graphique = False
    text_1=can.create_text(250,10,text="Warning : No original file selected",fill="red")
    text_2=can.create_text(250,30,text="Warning : No final file selected",fill="red")

def ouverture_menu(fenetre):
    menubar = Menu(fenetre)
    #On créé le menu déroulant 1 : Fichier
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Open original file", command=ouvrir_fichier1)
    menu1.add_command(label="Open final file", command=ouvrir_fichier2)
    menu1.add_separator()
    menu1.add_command(label="Run & display", command=lecture_fichier)
    menu1.add_separator()
    menu1.add_command(label="Reset", command=reinitialisation)
    menu1.add_command(label="Exit", command=fenetre.quit)
    menubar.add_cascade(label="File", menu=menu1)
    
    #On créé le menu déroulant 2 : paramètres
    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="Canvas", command=alert)
    menubar.add_cascade(label="Settings", menu=menu2)
    
    #On créé le menu déroulant 3 : Aide
    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="About...", command=alert)
    menubar.add_cascade(label="Help", menu=menu3)
    
    fenetre.config(menu=menubar)
    
    

#On ouvre la fenetre graphique de TKinter
fenetre = Tk()
fenetre.title("UI SMG2S")
fenetre.configure(bg = "white")
fichier1 = ""
fichier2 = ""
dimension = 0

graphique = False
reel1 = []
imaginaire1 = []
reel2 = []
imaginaire2 = []

can=Canvas(fenetre,width=800,height=40,background='white')
can.pack()
text_1=can.create_text(400,10,text="Warning : No original file selected",fill="red")
text_2=can.create_text(400,30,text="Warning : No final file selected",fill="red")

can_plot=Canvas(fenetre,width=800,height=600,background='white')
can_plot.pack()
text_image =can_plot.create_text(400, 300, text="please select a file then click on Run (File->Run)")

ouverture_menu(fenetre)

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()

