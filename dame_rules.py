'''
Nom    : dame_rules.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 05.12.2024
'''

import pygame

# Fonction pour déplacer le pion vers la droite
def bouge_bas_droite():
    global pion_col, pion_ligne
    if pion_col < nb_colonnes - 1 and pion_ligne < nb_lignes - 1:  # Bas-droite
        pion_col += 1
        pion_ligne += 1

def bouge_bas_gauche():
    global pion_col, pion_ligne
    if pion_col > 0 and pion_ligne < nb_lignes - 1:  # Bas-gauche
        pion_col -= 1
        pion_ligne += 1

def bouge_haut_droite():
    global pion_col1, pion_ligne1
    if pion_col1 < nb_colonnes - 1 and pion_ligne1 > 0:  # Haut-droite
        pion_col1 += 1
        pion_ligne1 -= 1

def bouge_haut_gauche():
    global pion_col1, pion_ligne1
    if pion_col1 > 0 and pion_ligne1 > 0:  # Haut-gauche
        pion_col1 -= 1
        pion_ligne1 -= 1

pygame.init()

# Taille du plateau
nb_lignes = 10
nb_colonnes = 10

# Position initiale du pion
pion_pos = 0

# Pion position horizontale
pion_col = 1

# Pion position verticale
pion_ligne = 0

# Pion1 position horizontale
pion_col1 = 2

# Pion1 position verticale
pion_ligne1 = 9

pygame.quit()