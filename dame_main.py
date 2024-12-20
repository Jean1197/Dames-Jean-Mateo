'''
Nom    : dame_main.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 22.11.2024
'''

import pygame
from dame_gfx import init_graphics, update_graphics
from dame_rules import handle_events

def main():
    # Initialiser pygame et les graphiques
    screen, assets, game_state = init_graphics()

    # Boucle principale
    running = True
    while running:
        running = handle_events(game_state)  # Gérer les événements
        update_graphics(screen, assets, game_state)  # Mettre à jour l'affichage

    # Quitter pygame
    pygame.quit()

if __name__ == "__main__":
    main()
