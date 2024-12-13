'''
Nom    : dame_main.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 22.11.2024
'''

import pygame
import sys
from dame_gfx import dessine_plateau, charger_images, initialiser_pions, afficher_pions

# Paramètres du plateau
case_size = 50
cases_blanches = (0,0,139)
cases_noires = (255,0,0)
nb_lignes, nb_colonnes = 10, 10

# Initialisation de pygame
pygame.init()
screen = pygame.display.set_mode((nb_colonnes * case_size, nb_lignes * case_size))
pygame.display.set_caption("Jeu de dames")

# Charger les images des pions
pion_noir, pion_blanc = charger_images(case_size)

# Initialiser les positions des pions
pions_noirs, pions_blancs = initialiser_pions(nb_lignes, nb_colonnes)

# Boucle principale
def main():
    running = True
    while running:
        # Dessiner le plateau
        dessine_plateau(screen, nb_lignes, nb_colonnes, case_size, cases_blanches, cases_noires)

        # Afficher les pions noirs et blancs
        afficher_pions(screen, pions_noirs, pion_noir, case_size)
        afficher_pions(screen, pions_blancs, pion_blanc, case_size)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
