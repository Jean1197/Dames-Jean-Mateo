'''
Nom    : dame_main.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 22.11.2024
'''

import pygame
from dame_gfx import init_graphics, update_graphics
from dame_rules import handle_events

# A l'aide de Chat GPT : lignes 13-28

def main():
        # Initialiser les graphiques
        screen, assets, game_state = init_graphics()

        # Boucle principale
        running = True
        while running:
            running = handle_events(game_state)  # Gérer les événements et vérifier si le jeu continue
            update_graphics(screen, assets, game_state)  # Mettre à jour l'affichage

        # Quitter pygame
        pygame.quit()


if __name__ == "__main__":
    main()