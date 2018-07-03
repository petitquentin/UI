#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:42:00 2018

@author: qpetit
"""

import re
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def alert():
    messagebox.showinfo("Say Hello", "Hello World")

def mise_a_jour_interface():
    can.delete(ALL)
    if fichier1 != "":
        text_1=can.create_text(250,10,text=fichier1,fill="red")
    else:
        text_1=can.create_text(250,10,text="Pas de fichier 1",fill="red")
    if fichier2 != "":
        text_2=can.create_text(250,30,text=fichier2,fill="red")
    else: 
        text_2=can.create_text(250,30,text="Pas de fichier 2",fill="red")
    fenetre.update_idletasks()
        

    

def ouvrir_fichier1():
    global fichier1 
    fichier1 = filedialog.askopenfilename(filetypes=[('Fichier Texte','.txt')])
    if fichier2 == "" and fichier1 != "":
        answer = messagebox.askyesno("Ouvrir fichier Final","Voulez-vous ouvrir le fichier Final maintenant ?")
        if answer == True:
            ouvrir_fichier2()
    mise_a_jour_interface()
    
    
def ouvrir_fichier2():
    global fichier2 
    fichier2 = filedialog.askopenfilename(filetypes=[('Fichier Texte','.txt')])
    if fichier1 == "" and fichier2 != "":
        answer = messagebox.askyesno("Ouvrir fichier Initial","Voulez-vous ouvrir le fichier Initial maintenant ?")
        if answer == True:
            ouvrir_fichier1
    mise_a_jour_interface()
    
def reinitialisation():
    global fichier1, fichier2
    fichier1 = ""
    fichier2 = ""
    can.delete(ALL)
    text_1=can.create_text(250,10,text="Réinitialisation réussite : Pas de fichier 1",fill="red")
    text_2=can.create_text(250,30,text="Réinitialisation réussite : Pas de fichier 2",fill="red")

def ouverture_menu(fenetre):
    menubar = Menu(fenetre)
    #On créé le menu déroulant 1 : Fichier
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Ouvrir Initial", command=ouvrir_fichier1)
    menu1.add_command(label="Ouvrir Final", command=ouvrir_fichier2)
    menu1.add_separator()
    menu1.add_command(label="Réinitialiser", command=reinitialisation)
    menu1.add_command(label="Quitter", command=fenetre.quit)
    menubar.add_cascade(label="Fichier", menu=menu1)
    
    #On créé le menu déroulant 2 : paramètres
    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="Taille de canvas", command=parametre_canvas)
    menubar.add_cascade(label="Paramètres", menu=menu2)
    
    #On créé le menu déroulant 3 : Aide
    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="A propos", command=alert)
    menubar.add_cascade(label="Aide", menu=menu3)
    
    fenetre.config(menu=menubar)
    
    

#On ouvre la fenetre graphique de TKinter
fenetre = Tk()

fichier1 = ""
fichier2 = ""

can=Canvas(fenetre,width=500,height=50,background='white')
can.pack()
text_1=can.create_text(250,10,text="Début : Pas de fichier 1",fill="red")
text_2=can.create_text(250,30,text="Début : Pas de fichier 2",fill="red")

ouverture_menu(fenetre)

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()

