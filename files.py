#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 16:22:11 2018

@author: qpetit
"""

import re
from tkinter import messagebox
from tkinter import filedialog
from decimal import Decimal
import numpy as np
import shutil


from get_path import read_file_path

def save_file():
    try:
        fichier = filedialog.asksaveasfilename(filetypes=[('PNG file','.png')])
        print(fichier)
        shutil.copy("data/graphic_brut.png", fichier)
    except FileNotFoundError:
        messagebox.showerror("eroor", "problem with file path, the image has not been saved")

def read_files():
    #On ouvre le fichier 1
    fichier1 = read_file_path(1)
    #On ouvre le fichier 2
    fichier2 = read_file_path(2)
    
    exp = r"[0-9]+(\.)?[0-9]*"
    # Booléen qui permet de stocker si on a déjà rencontré la ligne de la dimension.
    premiere_ligne = False
    dimension = 0
    if fichier1 == "" and fichier2 == "" :
        messagebox.showerror("Error","No files were opened")
        return -1
    else:
        if fichier1 != "":
            presence_fichier1 = True
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
                                
            np.savetxt(r'data/matrix/r1.vec', reel1)
            np.savetxt(r'data/matrix/i1.vec', imaginaire1)
        else:      
            presence_fichier1 = False
            messagebox.showwarning("Warning","The original file is not loaded")   
        
        
        premiere_ligne = False
        if fichier2 != "":
            presence_fichier2 = True
            with open(fichier2, "r") as f:
                for line in f.readlines():
                    donnees = line.split()
                    
                    #On regarde si le premier caractère n'est pas un espace est un chiffre
                    print(re.match(exp, donnees[0]))
                    if re.match(exp, donnees[0]) is not None:
                        if premiere_ligne == False:
                            premiere_ligne = True
                            ancienne_dimension = dimension
                            dimension = 0
                            for x in line.split(" "):
                                if re.match(exp, x):
                                    dimension += 1
                            dimension = dimension - 1
                            #On créé les vecteurs qui stockera les informations a afficher
                            reel2 = []
                            imaginaire2 = []
                            
                        else:
                            reel2.append(Decimal(donnees[1]))
                            if dimension == 2:
                                imaginaire2.append(Decimal(donnees[2]))
                            else:
                                imaginaire2.append(0)
            f.close                    
            np.savetxt(r'data/matrix/r2.vec', reel2)
            np.savetxt(r'data/matrix/i2.vec', imaginaire2)
        else:  
            presence_fichier2 = False              
            messagebox.showwarning("Warning","The final file is not loaded")
        if presence_fichier1 == presence_fichier2 == True :
            if ancienne_dimension != dimension :
                messagebox.showwarning("Error","The selected files are not the same size. Please check the files") 
                return -1
            else:
                return dimension
        else:
            return dimension


def open_file(number):
    
    if number == 1 :
        fichier = read_file_path(1)
        autre_fichier = read_file_path(2)
    else:
        fichier = read_file_path(2)
        autre_fichier = read_file_path(1)
    print(fichier, "Autre :", autre_fichier)
    #On enregistre ce que contient l'adresse du fichier précédente
    fichier_precedent = fichier
    
    #On demande à l'utilisateur de choisir son fichier texte
    fichier = filedialog.askopenfilename(filetypes=[('Text file','.txt')])
    #Si le fichier choisi est différent du fichier précédent alors le graphique n'est plus valable, on va donc pouvoir en refaire un et mettre à jour l'affichage.
    if fichier_precedent != fichier :
        file = open("data/files/file"+str(number)+".txt", "w")
        file.write(fichier)
#    if autre_fichier == "" and fichier != "" and number == 1:
#        answer = messagebox.askyesno("Open final file","Do you want to open the final file now?")
#        if answer == True:
#            open_file(2)
#    elif autre_fichier == "" and fichier != "" and number == 2:
#        print("autrefichier : ", autre_fichier, " fichier : ", fichier, "number : ", number)
#        answer = messagebox.askyesno("Open original file","Do you want to open the original file now?")
#        if answer == True:
#            open_file(1)
    