#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 12:26:49 2018

@author: qpetit
"""

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def setting_canvas(fenetre):
    fenetreParametre=Toplevel(fenetre)
    taille = ""
    titre_parametre = Label(fenetreParametre, text="Résolution du graphique")
    choix_1920 = Radiobutton(fenetreParametre, text="1920x1080", variable=taille, value="1920x1080")
    choix_1366 = Radiobutton(fenetreParametre, text="1366x768", variable=taille, value="1366x768")
    choix_800 = Radiobutton(fenetreParametre, text="800x600", variable=taille, value="800x600")
    choix_400 = Radiobutton(fenetreParametre, text="400x300", variable=taille, value="400x300")
    choix_perso = Radiobutton(fenetreParametre, text="Personnalisée", variable=taille, value="perso")
    var_abs = StringVar()
    ligne_abs = Entry(fenetreParametre, textvariable=var_abs, width=5)
    var_ord = StringVar()
    ligne_ord = Entry(fenetreParametre, textvariable=var_ord, width=5)
    titre_parametre.pack(side=LEFT)
    choix_1920.pack(side=LEFT)
    choix_1366.pack(side=LEFT)
    choix_800.pack(side=LEFT)
    choix_400.pack(side=LEFT)
    choix_perso.pack(side=LEFT)
    ligne_abs.pack(side=LEFT)
    ligne_ord.pack(side=LEFT)
    
#------------------------------------------------------------------------------
if __name__ == '__main__':
    fenetre = Tk()
    parametre_canvas()
    fenetreParametre.mainloop()