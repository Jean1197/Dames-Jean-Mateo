'''
Nom    : Jeu_des_Dames.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
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

# Paramètres du plateau et des cases
case_size = 50
cases_blanches = (200 , 173 , 127)
cases_noires = (91 , 60 , 17)

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

# Initialisation de pygame
pygame.init()

screen = pygame.display.set_mode((nb_colonnes * case_size, nb_lignes * case_size))
pygame.display.set_caption("Jeu de dames")

# Charger l'image du pion
pion = pygame.image.load("MA-24_pion_noir.png")
pion = pygame.transform.scale(pion, (case_size, case_size))

# Charger l'image du pion1
pion1 = pygame.image.load("MA-24_pion.png")
pion1 = pygame.transform.scale(pion1, (case_size, case_size))


# Boucle principale
running = True
while running:
    # Dessiner le plateau
    dessine_plateau()

    # Afficher le pion
    x_pion = pion_col * case_size
    y_pion = pion_ligne * case_size
    screen.blit(pion, (x_pion, y_pion))

    x_pion1 = pion_col1 * case_size
    y_pion1 = pion_ligne1 * case_size
    screen.blit(pion1, (x_pion1, y_pion1))



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
