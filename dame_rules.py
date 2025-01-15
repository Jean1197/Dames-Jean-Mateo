'''
Nom    : dame_rules.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 05.12.2024
'''

import pygame

case_size = 50
marge = 50  # Taille de la marge en pixels
nb_lignes, nb_colonnes = 10, 10

def calculer_deplacements(pion, pions_amis, pions_adverses, direction):
    """Calcule les mouvements possibles pour un pion donné."""
    ligne, colonne = pion
    mouvements = []
    directions = [(1, -1), (1, 1)] if direction == "bas" else [(-1, -1), (-1, 1)]

    for d_ligne, d_colonne in directions:
        new_ligne, new_colonne = ligne + d_ligne, colonne + d_colonne
        if 0 <= new_ligne < nb_lignes and 0 <= new_colonne < nb_colonnes:
            if (new_ligne, new_colonne) not in pions_amis and (new_ligne, new_colonne) not in pions_adverses:
                mouvements.append((new_ligne, new_colonne))

    return mouvements

def handle_events(game_state):
    """Gère les événements utilisateur et met à jour l'état du jeu."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            colonne = (x - marge) // case_size
            ligne = (y - marge) // case_size

            # Si un pion est déjà sélectionné
            if game_state["pion_selectionne"]:
                # Vérifiez si le mouvement est valide
                if (ligne, colonne) in game_state["mouvements_possibles"]:
                    pion_selectionne = game_state["pion_selectionne"]

                    if pion_selectionne in game_state["pions_noirs"] and game_state["tour_actif"] == "noir":
                        game_state["pions_noirs"].remove(pion_selectionne)
                        game_state["pions_noirs"].append((ligne, colonne))
                        game_state["tour_actif"] = "blanc"  # Passe au joueur blanc

                    elif pion_selectionne in game_state["pions_blancs"] and game_state["tour_actif"] == "blanc":
                        game_state["pions_blancs"].remove(pion_selectionne)
                        game_state["pions_blancs"].append((ligne, colonne))
                        game_state["tour_actif"] = "noir"  # Passe au joueur noir

                    # Réinitialisez la sélection
                    game_state["pion_selectionne"] = None
                    game_state["mouvements_possibles"] = []

                else:
                    # Si la case cliquée n'est pas un mouvement valide, désélectionner le pion
                    game_state["pion_selectionne"] = None
                    game_state["mouvements_possibles"] = []

            else:
                # Sélectionnez un pion valide pour le joueur actif
                if game_state["tour_actif"] == "noir" and (ligne, colonne) in game_state["pions_noirs"]:
                    game_state["pion_selectionne"] = (ligne, colonne)
                    direction = "bas"  # Les noirs se déplacent vers le bas
                    game_state["mouvements_possibles"] = calculer_deplacements(
                        (ligne, colonne),
                        game_state["pions_noirs"],
                        game_state["pions_blancs"],
                        direction
                    )
                elif game_state["tour_actif"] == "blanc" and (ligne, colonne) in game_state["pions_blancs"]:
                    game_state["pion_selectionne"] = (ligne, colonne)
                    direction = "haut"  # Les blancs se déplacent vers le haut
                    game_state["mouvements_possibles"] = calculer_deplacements(
                        (ligne, colonne),
                        game_state["pions_blancs"],
                        game_state["pions_noirs"],
                        direction
                    )

    return True
