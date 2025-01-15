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
marge = 50  # Taille de la marge en pixels

#dessine le tableau
def dessine_plateau(screen):
    """Dessine le plateau de jeu avec alternance des couleurs et une marge."""
    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):
            couleur = cases_blanches if (ligne + colonne) % 2 == 0 else cases_noires
            # Ajuste les coordonnées pour inclure la marge
            x = colonne * case_size + marge
            y = ligne * case_size + marge
            pygame.draw.rect(screen, couleur, (x, y, case_size, case_size))

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
    """Affiche les pions sur le plateau avec une marge."""
    for ligne, colonne in pions:
        x = colonne * case_size + marge
        y = ligne * case_size + marge
        screen.blit(pion_image, (x, y))


def init_graphics():
    """Initialise les graphiques et retourne les objets nécessaires."""
    pygame.init()
    screen = pygame.display.set_mode((nb_colonnes * case_size + 2 * marge, nb_lignes * case_size + 2 * marge))
    pygame.display.set_caption("Jeu de dames")
    pion_noir, pion_blanc = charger_images()
    pions_noirs, pions_blancs = initialiser_pions()
    assets = {"pion_noir": pion_noir, "pion_blanc": pion_blanc}

    # Initialisez correctement "tour_actif"
    game_state = {
        "pions_noirs": pions_noirs,
        "pions_blancs": pions_blancs,
        "pion_selectionne": None,
        "mouvements_possibles": [],
        "tour_actif": "noir"  # Le joueur noir commence
    }
    return screen, assets, game_state


def afficher_tour(screen, tour_actif):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Tour : {tour_actif.capitalize()}", True, (255, 255, 255))
    screen.blit(text, (10, 10))


def update_graphics(screen, assets, game_state):
    """Met à jour l'écran avec les nouveaux graphismes."""
    dessine_plateau(screen)
    afficher_pions(screen, game_state["pions_noirs"], assets["pion_noir"])
    afficher_pions(screen, game_state["pions_blancs"], assets["pion_blanc"])

    # Dessine les mouvements possibles
    for ligne, colonne in game_state["mouvements_possibles"]:
        pygame.draw.rect(screen, (0, 255, 0), (colonne * case_size + marge, ligne * case_size + marge, case_size, case_size), 5)

    # Affiche le tour si "tour_actif" existe
    if "tour_actif" in game_state:
        afficher_tour(screen, game_state["tour_actif"])
    else:
        print("Erreur : 'tour_actif' manquant dans game_state !")

    # Met à jour l'affichage
    pygame.display.flip()

