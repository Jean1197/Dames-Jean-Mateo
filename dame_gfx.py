'''
Nom    : dame_gfx.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 05.12.2024
'''

import pygame

# Paramètres globaux
case_size = 50
nb_lignes, nb_colonnes = 10, 10
cases_blanches = (0, 0, 139)
cases_noires = (255, 0, 0)

#dessine le tableau
def dessine_plateau(screen):
    """Dessine le plateau de jeu avec alternance des couleurs."""
    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):
            couleur = cases_blanches if (ligne + colonne) % 2 == 0 else cases_noires
            pygame.draw.rect(screen, couleur, (colonne * case_size, ligne * case_size, case_size, case_size))

def charger_images():
    """Charge et redimensionne les images des pions."""
    pion_noir = pygame.image.load("psg.png")
    pion_blanc = pygame.image.load("barca.png")
    pion_noir = pygame.transform.scale(pion_noir, (case_size, case_size))
    pion_blanc = pygame.transform.scale(pion_blanc, (case_size, case_size))
    return pion_noir, pion_blanc

def initialiser_pions():
    """Initialise les positions des pions noirs et blancs."""
    pions_noirs = [(ligne, colonne) for ligne in range(4) for colonne in range(nb_colonnes) if (ligne + colonne) % 2 == 1]
    pions_blancs = [(ligne, colonne) for ligne in range(nb_lignes - 4, nb_lignes) for colonne in range(nb_colonnes) if (ligne + colonne) % 2 == 1]
    return pions_noirs, pions_blancs

def afficher_pions(screen, pions, pion_image):
    """Affiche les pions sur le plateau."""
    for ligne, colonne in pions:
        x, y = colonne * case_size, ligne * case_size
        screen.blit(pion_image, (x, y))

def init_graphics():
    """Initialise les graphiques et retourne les objets nécessaires."""
    pygame.init()
    screen = pygame.display.set_mode((nb_colonnes * case_size, nb_lignes * case_size))
    pygame.display.set_caption("Jeu de dames")
    pion_noir, pion_blanc = charger_images()
    pions_noirs, pions_blancs = initialiser_pions()
    assets = {"pion_noir": pion_noir, "pion_blanc": pion_blanc}
    game_state = {"pions_noirs": pions_noirs, "pions_blancs": pions_blancs, "pion_selectionne": None, "mouvements_possibles": []}
    return screen, assets, game_state

def update_graphics(screen, assets, game_state):
    """Met à jour l'écran avec les nouveaux graphismes."""
    dessine_plateau(screen)
    afficher_pions(screen, game_state["pions_noirs"], assets["pion_noir"])
    afficher_pions(screen, game_state["pions_blancs"], assets["pion_blanc"])
    for ligne, colonne in game_state["mouvements_possibles"]:
        pygame.draw.rect(screen, (0, 255, 0), (colonne * case_size, ligne * case_size, case_size, case_size), 5)
    pygame.display.flip()
