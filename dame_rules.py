'''
Nom    : dame_rules.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 05.12.2024
'''

import pygame

case_size = 70
marge = 70  # Taille de la marge en pixels
nb_lignes, nb_colonnes = 10, 10

def calculer_deplacements(pion, pions_amis, pions_adverses, direction):
    """Calcule les mouvements possibles pour un pion donné, priorisant les captures."""
    ligne, colonne = pion
    mouvements = []
    captures = []
    directions = [(1, -1), (1, 1)] if direction == "bas" else [(-1, -1), (-1, 1)]

    for d_ligne, d_colonne in directions:
        # Déplacement simple
        new_ligne, new_colonne = ligne + d_ligne, colonne + d_colonne
        if 0 <= new_ligne < nb_lignes and 0 <= new_colonne < nb_colonnes:
            if (new_ligne, new_colonne) not in pions_amis and (new_ligne, new_colonne) not in pions_adverses:
                mouvements.append((new_ligne, new_colonne))

        # Déplacement pour manger
        saut_ligne, saut_colonne = ligne + 2 * d_ligne, colonne + 2 * d_colonne
        if (
            0 <= saut_ligne < nb_lignes and 0 <= saut_colonne < nb_colonnes
            and (new_ligne, new_colonne) in pions_adverses
            and (saut_ligne, saut_colonne) not in pions_amis
            and (saut_ligne, saut_colonne) not in pions_adverses
        ):
            captures.append((saut_ligne, saut_colonne))

    return captures if captures else mouvements


def handle_events(game_state):
    """Gère les événements utilisateur et met à jour l'état du jeu."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False  # Quitter la fenêtre si l'utilisateur clique sur la croix

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False  # Quitter si 'q' est pressée

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            colonne = (x - marge) // case_size
            ligne = (y - marge) // case_size

            # Si un pion est déjà sélectionné
            if game_state["pion_selectionne"]:
                pion_selectionne = game_state["pion_selectionne"]
                if (ligne, colonne) in game_state["mouvements_possibles"]:
                    # Récupération des pions actuels et adverses
                    pions_actuels = game_state["pions_noirs"] if game_state["tour_actif"] == "Noir" else game_state[
                        "pions_blancs"]
                    pions_adverses = game_state["pions_blancs"] if game_state["tour_actif"] == "Noir" else game_state[
                        "pions_noirs"]

                    # Déplacement du pion
                    pions_actuels.remove(pion_selectionne)
                    pions_actuels.append((ligne, colonne))

                    # Vérifier si un pion a été capturé
                    capturable = ((pion_selectionne[0] + ligne) // 2, (pion_selectionne[1] + colonne) // 2)
                    capture_effectuee = capturable in pions_adverses
                    if capture_effectuee:
                        pions_adverses.remove(capturable)

                        # Vérifier si une autre capture est possible
                        direction = "bas" if game_state["tour_actif"] == "Noir" else "haut"
                        mouvements_suivants = calculer_deplacements((ligne, colonne), pions_actuels, pions_adverses,
                                                                    direction)

                        if mouvements_suivants and any(
                                m in mouvements_suivants for m in game_state["mouvements_possibles"]):
                            # S'il y a encore une capture possible, on reste sur le même tour
                            game_state["pion_selectionne"] = (ligne, colonne)
                            game_state["mouvements_possibles"] = mouvements_suivants
                            return True  # Tour non fini

                    # Si pas de capture enchaînée possible, on change de joueur
                    game_state["tour_actif"] = "Blanc" if game_state["tour_actif"] == "Noir" else "Noir"
                    game_state["pion_selectionne"] = None
                    game_state["mouvements_possibles"] = []

                else:
                    game_state["pion_selectionne"] = None
                    game_state["mouvements_possibles"] = []

            else:
                # Sélection d'un pion valide
                pions_actuels = game_state["pions_noirs"] if game_state["tour_actif"] == "Noir" else game_state[
                    "pions_blancs"]
                pions_adverses = game_state["pions_blancs"] if game_state["tour_actif"] == "Noir" else game_state[
                    "pions_noirs"]
                direction = "bas" if game_state["tour_actif"] == "Noir" else "haut"

                if (ligne, colonne) in pions_actuels:
                    mouvements = calculer_deplacements((ligne, colonne), pions_actuels, pions_adverses, direction)
                    if mouvements:
                        game_state["pion_selectionne"] = (ligne, colonne)
                        game_state["mouvements_possibles"] = mouvements
    return True




