#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 14:41:46 2018

@author: qpetit
"""


from tkinter import *

def reset_window(can, can_plot, menubar):
    global graphique
    
    menubar.entryconfigure(2, state=DISABLED)
    #On écrase le chemin préalablement inscrit dans le fichier 1
    mon_fichier = open("data/files/file1.txt", "w") 
    mon_fichier.write("")
    mon_fichier.close()
    
    #De même pour le fichier 2
    mon_fichier = open("data/files/file2.txt", "w")
    mon_fichier.write("")
    mon_fichier.close()
    
    #On efface les inscriptions potentiellement présentes dans les canvas de la fenêtre
    can.delete(ALL)
    can_plot.delete(ALL)
    text_1=can.create_text(400,10,text="Warning : No original file selected",fill="red")
    text_2=can.create_text(400,30,text="Warning : No final file selected",fill="red")
    text_image1 = can_plot.create_text(400, 290, text="The graphic will be generate here")
    text_image2 = can_plot.create_text(400, 310, text="please select files then click on Run (File->Run)")

