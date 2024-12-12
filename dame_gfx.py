'''
Nom    : dame_gfx.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 05.12.2024
'''

import pygame

def dessine_plateau(screen, nb_lignes, nb_colonnes, case_size, cases_blanches, cases_noires):
    """Dessine le plateau de jeu avec alternance des couleurs."""
    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):
            couleur = cases_blanches if (ligne + colonne) % 2 == 0 else cases_noires
            pygame.draw.rect(screen, couleur, (colonne * case_size, ligne * case_size, case_size, case_size))

def charger_images(case_size):
    """Charge et redimensionne les images des pions."""
    pion_noir = pygame.image.load("MA-24_pion_noir.png")
    pion_noir = pygame.transform.scale(pion_noir, (case_size, case_size))

    pion_blanc = pygame.image.load("MA-24_pion.png")
    pion_blanc = pygame.transform.scale(pion_blanc, (case_size, case_size))

    return pion_noir, pion_blanc

def initialiser_pions(nb_lignes, nb_colonnes):
    """Initialise les positions des pions noirs et blancs."""
    pions_noirs = []
    pions_blancs = []

    # Ajouter les pions noirs dans les trois premières lignes sur les cases noires
    for ligne in range(3):
        for colonne in range(nb_colonnes):
            if (ligne + colonne) % 2 == 1:  # Case noire
                pions_noirs.append((ligne, colonne))

    # Ajouter les pions blancs dans les trois dernières lignes sur les cases noires
    for ligne in range(nb_lignes - 3, nb_lignes):
        for colonne in range(nb_colonnes):
            if (ligne + colonne) % 2 == 1:  # Case noire
                pions_blancs.append((ligne, colonne))

    return pions_noirs, pions_blancs

def afficher_pions(screen, pions, pion_image, case_size):
    """Affiche les pions sur le plateau."""
    for ligne, colonne in pions:
        x = colonne * case_size
        y = ligne * case_size
        screen.blit(pion_image, (x, y))
