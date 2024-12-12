'''
Nom    : dame_gfx.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 05.12.2024
'''

import pygame


def dessine_plateau(screen, nb_lignes, nb_colonnes, case_size, cases_blanches, cases_noires):
    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):
            couleur = cases_blanches if (ligne + colonne) % 2 == 0 else cases_noires
            pygame.draw.rect(screen, couleur, (colonne * case_size, ligne * case_size, case_size, case_size))


def charger_images(case_size):
    pion = pygame.image.load("MA-24_pion_noir.png")
    pion = pygame.transform.scale(pion, (case_size, case_size))

    pion1 = pygame.image.load("MA-24_pion.png")
    pion1 = pygame.transform.scale(pion1, (case_size, case_size))

    return pion, pion1
