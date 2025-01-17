'''
Nom    : dame_gfx.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 05.12.2024
'''

import pygame

# A l'aide de Chat GPT : lignes 19-27, 42-126

# Paramètres
case_size = 70
nb_lignes, nb_colonnes = 10, 10
cases_blanches = (255, 255, 255) # Couleur blanche
cases_noires = (47,79,79) # Couleur gris foncé
marge = 70  # Taille de la marge en pixels

# Dessine le plateau
def dessine_plateau(screen):
    # Dessine le plateau de jeu avec les couleurs et une marge
    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):
            couleur = cases_blanches if (ligne + colonne) % 2 == 0 else cases_noires
            # Ajuste les coordonnées pour inclure la marge
            x = colonne * case_size + marge
            y = ligne * case_size + marge
            pygame.draw.rect(screen, couleur, (x, y, case_size, case_size))

def charger_images():
    # Charge et redimensionne les images des pions et des dames
    pion_noir = pygame.image.load("MA-24_pion_noir.png")
    pion_blanc = pygame.image.load("MA-24_pion.png")
    pion_dame_noir = pygame.image.load("MA-24_dame_noire.png")
    pion_dame_blanc = pygame.image.load("MA-24_dame_blanche.png")
    pion_noir = pygame.transform.scale(pion_noir, (case_size, case_size))
    pion_blanc = pygame.transform.scale(pion_blanc, (case_size, case_size))
    pion_dame_noir = pygame.transform.scale(pion_dame_noir, (case_size, case_size))
    pion_dame_blanc = pygame.transform.scale(pion_dame_blanc, (case_size, case_size))
    return pion_noir, pion_blanc, pion_dame_noir, pion_dame_blanc


def initialiser_pions():
    # Initialise les positions des pions noirs et blancs
    pions_noirs = [(ligne, colonne) for ligne in range(4) for colonne in range(nb_colonnes) if (ligne + colonne) % 2 == 1]
    pions_blancs = [(ligne, colonne) for ligne in range(nb_lignes - 4, nb_lignes) for colonne in range(nb_colonnes) if (ligne + colonne) % 2 == 1]
    return pions_noirs, pions_blancs

def afficher_pions(screen, pions, assets, game_state):
    # Affiche les pions et les dames sur le plateau
    for piece in pions:
        # Vérifie si c'est un pion (2 éléments) ou une dame (3 éléments)
        if len(piece) == 2:  # Pion normal
            ligne, colonne = piece
            x = colonne * case_size + marge
            y = ligne * case_size + marge
            if piece in game_state["pions_noirs"]:  # Si c'est un pion noir
                screen.blit(assets["pion_noir"], (x, y))
            else:  # Si c'est un pion blanc
                screen.blit(assets["pion_blanc"], (x, y))
        elif len(piece) == 3:  # Dame (3 éléments : ligne, colonne, type)
            ligne, colonne, type_dame = piece
            x = colonne * case_size + marge
            y = ligne * case_size + marge
            if type_dame == "noir":  # Dame noire
                screen.blit(assets["pion_dame_noir"], (x, y))
            else:  # Dame blanche
                screen.blit(assets["pion_dame_blanc"], (x, y))


def init_graphics():
    # Initialise les graphiques
    pygame.init()
    screen = pygame.display.set_mode((nb_colonnes * case_size + 2 * marge, nb_lignes * case_size + 2 * marge))
    pygame.display.set_caption("Jeu de dames")

    pion_noir, pion_blanc, pion_dame_noir, pion_dame_blanc = charger_images()  # Récupérer toutes les images
    assets = {
        "pion_noir": pion_noir,
        "pion_blanc": pion_blanc,
        "pion_dame_noir": pion_dame_noir,
        "pion_dame_blanc": pion_dame_blanc
    }

    # Appel à la fonction pour initialiser les positions des pions
    pions_noirs, pions_blancs = initialiser_pions()

    # Initialisation de l'état du jeu
    game_state = {
        "pions_noirs": pions_noirs,
        "pions_blancs": pions_blancs,
        "pion_selectionne": None,
        "mouvements_possibles": [],
        "tour_actif": "Noir"  # Noir commence
    }

    return screen, assets, game_state


def effacer_zone_texte(screen):
    # Efface une zone spécifique où le texte est affiché
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen.get_width(), 50))  # Efface le haut de l'écran

def afficher_tour(screen, tour_actif):
    # Affiche le texte indiquant le tour actuel
    effacer_zone_texte(screen)  # Efface la zone précédente
    font = pygame.font.Font(None, 50)
    couleur = (255, 255, 255) if tour_actif == "Noir" else (255, 255, 255)  # Même couleur, mais vous pouvez choisir une couleur différente pour chaque équipe
    text = font.render(f"Tour : {tour_actif.capitalize()}", True, couleur)
    screen.blit(text, (10, 10))

def update_graphics(screen, assets, game_state):
    # Met à jour l'écran avec les nouveaux graphismes
    # Efface tout l'écran avant de redessiner
    screen.fill((0, 0, 0))

    # Dessine le plateau et les pions
    dessine_plateau(screen)
    afficher_pions(screen, game_state["pions_noirs"], assets, game_state)
    afficher_pions(screen, game_state["pions_blancs"], assets, game_state)

    # Dessine les mouvements possibles
    for ligne, colonne in game_state["mouvements_possibles"]:
        pygame.draw.rect(screen, (0, 255, 0), (colonne * case_size + marge, ligne * case_size + marge, case_size, case_size), 5)

    # Affiche le tour actif
    afficher_tour(screen, game_state["tour_actif"])

    # Met à jour l'affichage
    pygame.display.flip()