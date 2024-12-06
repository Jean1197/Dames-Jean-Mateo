'''
Nom    : dame_rules.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 05.12.2024
'''

import pygame
import sys

def dessine_case(x, y, couleur):
    global screen, case_size
    pygame.draw.rect(
        screen,
        couleur,
        (x, y, case_size, case_size)
    )

# Fonction pour dessiner le damier
def dessine_plateau():
    global screen, nb_lignes, nb_colonnes, cases_blanches, cases_noires, case_size
    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):
            # Alterne les couleurs
            if (ligne + colonne) % 2 == 0:
                couleur = cases_blanches
            else:
                couleur = cases_noires
            x = colonne * case_size
            y = ligne * case_size
            dessine_case(x, y, couleur)


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
    if pion_col1 > 0 and pion_ligne1 > 0:  # Haut-gaucheq
        pion_col1 -= 1
        pion_ligne1 -= 1


 for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                bouge_bas_droite()
            elif event.key == pygame.K_LEFT:
                bouge_bas_gauche()
            if event.key == pygame.K_UP:
                bouge_haut_droite()
            elif event.key == pygame.K_DOWN:
                bouge_haut_gauche()
            elif event.key == pygame.K_q:
                running = False

 pygame.display.flip()

pygame.quit()
sys.exit()