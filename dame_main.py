'''
Nom    : dame_main.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 22.11.2024
'''

import pygame
import sys
from dame_gfx import dessine_plateau, charger_images
from dame_rules import bouge_bas_droite, bouge_bas_gauche, bouge_haut_droite, bouge_haut_gauche

# Paramètres du plateau
case_size = 50
cases_blanches = (200, 173, 127)
cases_noires = (91, 60, 17)
nb_lignes, nb_colonnes = 10, 10

# Position initiale des pions
pion_col, pion_ligne = 1, 0
pion_col1, pion_ligne1 = 2, 9

# Initialisation de pygame
pygame.init()
screen = pygame.display.set_mode((nb_colonnes * case_size, nb_lignes * case_size))
pygame.display.set_caption("Jeu de dames")

# Charger les images des pions
pion, pion1 = charger_images(case_size)

# Boucle principale
def main():
    global pion_col, pion_ligne, pion_col1, pion_ligne1
    running = True
    while running:
        # Dessiner le plateau
        dessine_plateau(screen, nb_lignes, nb_colonnes, case_size, cases_blanches, cases_noires)

        # Afficher les pions
        screen.blit(pion, (pion_col * case_size, pion_ligne * case_size))
        screen.blit(pion1, (pion_col1 * case_size, pion_ligne1 * case_size))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pion_col, pion_ligne = bouge_bas_droite(pion_col, pion_ligne, nb_colonnes, nb_lignes)
                elif event.key == pygame.K_LEFT:
                    pion_col, pion_ligne = bouge_bas_gauche(pion_col, pion_ligne, nb_colonnes, nb_lignes)
                elif event.key == pygame.K_UP:
                    pion_col1, pion_ligne1 = bouge_haut_droite(pion_col1, pion_ligne1, nb_colonnes, nb_lignes)
                elif event.key == pygame.K_DOWN:
                    pion_col1, pion_ligne1 = bouge_haut_gauche(pion_col1, pion_ligne1, nb_colonnes, nb_lignes)
                elif event.key == pygame.K_q:
                    running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
