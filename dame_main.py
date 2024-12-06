'''
Nom    : dame_main.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 22.11.2024
'''

#pygame à installer sur les deux postes

import pygame
import dame_gfx as gfx
import dame_rules

taille_plateau = (10,10)

gfx.plateau(taille_plateau)
print ("Plateau de", taille_plateau[0], "par", taille_plateau[1])
gfx.start()
