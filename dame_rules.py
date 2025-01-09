'''
Nom    : dame_rules.py
Auteur : Jean-Christophe Serrano x Mateo Grgic
Date   : 05.12.2024
'''

import pygame

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

        elif event.type == pygame.KEYDOWN:  # Gérer l'appui sur une touche
            if event.key == pygame.K_q:  # Vérifier si la touche 'Q' est pressée
                return False


        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche

            x, y = pygame.mouse.get_pos()

            colonne, ligne = x // 50, y // 50  # 50 est la taille de la case

            if game_state["pion_selectionne"]:

                if (ligne, colonne) in game_state["mouvements_possibles"]:

                    pion_selectionne = game_state["pion_selectionne"]

                    if pion_selectionne in game_state["pions_noirs"]:

                        game_state["pions_noirs"].remove(pion_selectionne)

                        game_state["pions_noirs"].append((ligne, colonne))

                    elif pion_selectionne in game_state["pions_blancs"]:

                        game_state["pions_blancs"].remove(pion_selectionne)

                        game_state["pions_blancs"].append((ligne, colonne))

                    game_state["pion_selectionne"] = None

                    game_state["mouvements_possibles"] = []


            else:

                mouvements = []

                if (ligne, colonne) in game_state["pions_noirs"]:

                    mouvements = calculer_deplacements(

                        (ligne, colonne), game_state["pions_noirs"], game_state["pions_blancs"], "bas"

                    )

                    if mouvements:  # Seulement sélectionner le pion s'il a des mouvements possibles

                        game_state["pion_selectionne"] = (ligne, colonne)

                        game_state["mouvements_possibles"] = mouvements


                elif (ligne, colonne) in game_state["pions_blancs"]:

                    mouvements = calculer_deplacements(

                        (ligne, colonne), game_state["pions_blancs"], game_state["pions_noirs"], "haut"

                    )

                    if mouvements:  # Seulement sélectionner le pion s'il a des mouvements possibles

                        game_state["pion_selectionne"] = (ligne, colonne)

                        game_state["mouvements_possibles"] = mouvements
    return True