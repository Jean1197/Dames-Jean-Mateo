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
cases_blanches = (0, 0, 139)
cases_noires = (255, 0, 0)
nb_lignes, nb_colonnes = 10, 10

# Initialisation de pygame
pygame.init()
screen = pygame.display.set_mode((nb_colonnes * case_size, nb_lignes * case_size))
pygame.display.set_caption("Jeu de dames")

# Charger les images des pions
pion_noir, pion_blanc = charger_images(case_size)

# Initialiser les positions des pions
pions_noirs, pions_blancs = initialiser_pions(nb_lignes, nb_colonnes)

# Variables pour gérer la sélection et les déplacements
pion_selectionne = None
mouvements_possibles = []

# Fonction pour calculer les déplacements possibles
def calculer_deplacements(pion, pions_amis, pions_adverses, direction):
    """Calcule les mouvements possibles pour un pion donné en diagonale et dans une direction donnée."""
    ligne, colonne = pion
    mouvements = []

    # Directions en fonction de l'avant (haut ou bas)
    if direction == "bas":
        directions = [(1, -1), (1, 1)]  # Diagonales vers le bas
    elif direction == "haut":
        directions = [(-1, -1), (-1, 1)]  # Diagonales vers le haut

    for d_ligne, d_colonne in directions:
        new_ligne = ligne + d_ligne
        new_colonne = colonne + d_colonne

        if 0 <= new_ligne < nb_lignes and 0 <= new_colonne < nb_colonnes:
            if (new_ligne, new_colonne) not in pions_amis and (new_ligne, new_colonne) not in pions_adverses:
                mouvements.append((new_ligne, new_colonne))

    return mouvements

# Boucle principale
def main():
    global pion_selectionne, mouvements_possibles

    running = True
    while running:
        # Dessiner le plateau
        dessine_plateau(screen, nb_lignes, nb_colonnes, case_size, cases_blanches, cases_noires)

        # Afficher les pions noirs et blancs
        afficher_pions(screen, pions_noirs, pion_noir, case_size)
        afficher_pions(screen, pions_blancs, pion_blanc, case_size)

        # Afficher les déplacements possibles
        for ligne, colonne in mouvements_possibles:
            pygame.draw.rect(
                screen, (0, 255, 0), (colonne * case_size, ligne * case_size, case_size, case_size), 5
            )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
                x, y = pygame.mouse.get_pos()
                colonne, ligne = x // case_size, y // case_size

                if pion_selectionne:
                    # Déplacer le pion si la case est valide
                    if (ligne, colonne) in mouvements_possibles:
                        if pion_selectionne in pions_noirs:
                            pions_noirs.remove(pion_selectionne)
                            pions_noirs.append((ligne, colonne))
                        elif pion_selectionne in pions_blancs:
                            pions_blancs.remove(pion_selectionne)
                            pions_blancs.append((ligne, colonne))

                        pion_selectionne = None
                        mouvements_possibles = []

                else:
                    # Vérifier si un pion est sélectionné
                    if (ligne, colonne) in pions_noirs:
                        pion_selectionne = (ligne, colonne)
                        mouvements_possibles = calculer_deplacements(
                            pion_selectionne, pions_noirs, pions_blancs, "bas"
                        )
                    elif (ligne, colonne) in pions_blancs:
                        pion_selectionne = (ligne, colonne)
                        mouvements_possibles = calculer_deplacements(
                            pion_selectionne, pions_blancs, pions_noirs, "haut"
                        )

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
