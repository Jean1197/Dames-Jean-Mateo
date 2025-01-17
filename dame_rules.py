'''
Nom    : dame_rules.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 05.12.2024
'''

import pygame

# A l'aide de Chat GPT : lignes 15-159

case_size = 70  # Taille de la case
marge = 70  # Taille de la marge
nb_lignes, nb_colonnes = 10, 10

def calculer_deplacements_pion(pion, pions_amis, pions_adverses, direction):
    # Calcule les mouvements possibles pour un pion
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


def calculer_deplacements_dame(pion, pions_amis, pions_adverses):
    # Calcule les déplacements possibles pour une dame dans toutes les directions diagonales
    ligne, colonne = pion
    mouvements = []
    captures = []

    # Directions possibles pour la dame (haut/gauche, haut/droite, bas/gauche, bas/droite)
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    # Explore chaque direction
    for d_ligne, d_colonne in directions:
        for i in range(1, nb_lignes):  # Exploration sur plusieurs cases
            new_ligne = ligne + d_ligne * i
            new_colonne = colonne + d_colonne * i
            if 0 <= new_ligne < nb_lignes and 0 <= new_colonne < nb_colonnes:
                # Si la case est vide, le déplacement est possible
                if (new_ligne, new_colonne) not in pions_amis and (new_ligne, new_colonne) not in pions_adverses:
                    mouvements.append((new_ligne, new_colonne))

                # Si la case contient un pion adverse, vérifier la possibilité de capture
                elif (new_ligne, new_colonne) in pions_adverses:
                    saut_ligne = new_ligne + d_ligne
                    saut_colonne = new_colonne + d_colonne
                    if 0 <= saut_ligne < nb_lignes and 0 <= saut_colonne < nb_colonnes:
                        # Si la case de capture est libre, on peut capturer
                        if (saut_ligne, saut_colonne) not in pions_amis and (saut_ligne, saut_colonne) not in pions_adverses:
                            captures.append((saut_ligne, saut_colonne))
            else:
                break  # Si on sort du plateau, on arrête d'explorer dans cette direction

    return captures if captures else mouvements




def handle_events(game_state):
    # Gère les événements utilisateur et met à jour l'état du jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False  # Quitter la fenêtre si l'utilisateur clique sur la croix

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False  # Quitter si 'q' est pressé

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

                    # Vérification si le pion a atteint la dernière ligne (et devient une dame)
                    if (game_state["tour_actif"] == "Noir" and ligne == nb_lignes - 1):
                        pions_actuels.remove((ligne, colonne))
                        pions_actuels.append((ligne, colonne, "noir"))  # Transforme en dame noire
                    elif (game_state["tour_actif"] == "Blanc" and ligne == 0):
                        pions_actuels.remove((ligne, colonne))
                        pions_actuels.append((ligne, colonne, "blanc"))  # Transforme en dame blanche

                    # Vérifier si une autre capture est possible
                    capturable = ((pion_selectionne[0] + ligne) // 2, (pion_selectionne[1] + colonne) // 2)
                    capture_effectuee = capturable in pions_adverses
                    if capture_effectuee:
                        pions_adverses.remove(capturable)

                        # Vérifier si une autre capture est possible
                        if len((ligne, colonne)) == 3:  # Si c'est une dame
                            mouvements_suivants = calculer_deplacements_dame((ligne, colonne), pions_actuels, pions_adverses)
                        else:
                            direction = "bas" if game_state["tour_actif"] == "Noir" else "haut"
                            mouvements_suivants = calculer_deplacements_pion((ligne, colonne), pions_actuels, pions_adverses, direction)

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
                pions_actuels = game_state["pions_noirs"] if game_state["tour_actif"] == "Noir" else game_state["pions_blancs"]
                pions_adverses = game_state["pions_blancs"] if game_state["tour_actif"] == "Noir" else game_state["pions_noirs"]
                direction = "bas" if game_state["tour_actif"] == "Noir" else "haut"

                if (ligne, colonne) in pions_actuels:
                    # Si c'est une dame
                    if len((ligne, colonne)) == 3:  # Si c'est une dame (3 éléments)
                        mouvements = calculer_deplacements_dame((ligne, colonne), pions_actuels, pions_adverses)
                    else:
                        mouvements = calculer_deplacements_pion((ligne, colonne), pions_actuels, pions_adverses, direction)
                    if mouvements:
                        game_state["pion_selectionne"] = (ligne, colonne)
                        game_state["mouvements_possibles"] = mouvements
    return True



