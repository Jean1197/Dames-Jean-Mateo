'''
Nom    : dame_rules.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 05.12.2024
'''

def bouge_bas_droite(col, ligne, nb_colonnes, nb_lignes):
    if col < nb_colonnes - 1 and ligne < nb_lignes - 1:  # Bas-droite
        col += 1
        ligne += 1
    return col, ligne

def bouge_bas_gauche(col, ligne, nb_colonnes, nb_lignes):
    if col > 0 and ligne < nb_lignes - 1:  # Bas-gauche
        col -= 1
        ligne += 1
    return col, ligne

def bouge_haut_droite(col, ligne, nb_colonnes, nb_lignes):
    if col < nb_colonnes - 1 and ligne > 0:  # Haut-droite
        col += 1
        ligne -= 1
    return col, ligne

def bouge_haut_gauche(col, ligne, nb_colonnes, nb_lignes):
    if col > 0 and ligne > 0:  # Haut-gauche
        col -= 1
        ligne -= 1
    return col, ligne
