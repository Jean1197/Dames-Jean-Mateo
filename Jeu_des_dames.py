'''
Nom    : Jeu_des_Dames.py
Auteur : Jean-Christophe Serrano
Date   : 22.11.2024
'''

#pygame à installer sur les deux postes
import pygame
import sys

from pygame import KEYDOWN


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


# Paramètres du plateau et des cases
case_size = 50
cases_blanches = (255, 255, 255)
cases_noires = (0, 0, 0)

# Taille du plateau
nb_lignes = 10
nb_colonnes = 10

# Position initiale du pion
pion_pos = 0

# Pion position horizontale
pion_col = 0

# Pion position verticale
pion_ligne = 0

# Initialisation de pygame
pygame.init()

screen = pygame.display.set_mode((nb_colonnes * case_size, nb_lignes * case_size))
pygame.display.set_caption("Jeu de dames")

# Charger l'image du pion
pion = pygame.image.load("MA-24_pion.png")
pion = pygame.transform.scale(pion, (case_size, case_size))

# Boucle principale
running = True
while running:
    # Dessiner le plateau
    dessine_plateau()

    # Afficher le pion
    x_pion = pion_col * case_size
    y_pion = pion_ligne * case_size
    screen.blit(pion, (x_pion, y_pion))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                bouge_bas_droite()
            elif event.key == pygame.K_LEFT:
                bouge_bas_gauche()
            elif event.key == pygame.K_q:
                running = False



    pygame.display.flip()

pygame.quit()
sys.exit()
