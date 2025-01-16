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
    """Calcule les mouvements possibles pour un pion donné, priorisant les captures."""
    ligne, colonne = pion
    mouvements = []
    captures = []
    directions = [(1, -1), (1, 1)] if direction == "bas" else [(-1, -1), (-1, 1)]

    print(f"Calcul des déplacements pour {pion}, direction: {direction}")  # Log de la direction et du pion

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

    # Si des captures sont disponibles, elles deviennent obligatoires
    print(f"Mouvements possibles: {mouvements}, Captures possibles: {captures}")  # Log des résultats
    return captures if captures else mouvements

def verifier_captures_obligatoires(pions_actifs, pions_adverses, direction):
    """Vérifie si des captures sont obligatoires pour le joueur actif."""
    for pion in pions_actifs:
        if calculer_deplacements(pion, pions_actifs, pions_adverses, direction):
            return True
    return False

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

            print(f"Click détecté en ({ligne}, {colonne})")  # Log pour afficher où l'utilisateur clique

            # Si un pion est déjà sélectionné
            if game_state["pion_selectionne"]:
                pion_selectionne = game_state["pion_selectionne"]
                print(f"Pion sélectionné : {pion_selectionne}")  # Log de la sélection du pion

                # Vérifiez si le mouvement est valide
                if (ligne, colonne) in game_state["mouvements_possibles"]:
                    print(f"Mouvement valide vers ({ligne}, {colonne})")  # Log de mouvement valide
                    # Déplacez le pion et gérez les captures
                    if pion_selectionne in game_state["pions_noirs"] and game_state["tour_actif"] == "PSG":
                        # Déplacez le pion noir
                        game_state["pions_noirs"].remove(pion_selectionne)
                        game_state["pions_noirs"].append((ligne, colonne))

                        # Gérer les captures
                        capturable = ((pion_selectionne[0] + ligne) // 2, (pion_selectionne[1] + colonne) // 2)
                        if capturable in game_state["pions_blancs"]:
                            print(f"Capture détectée sur {capturable}")  # Log de la capture
                            game_state["pions_blancs"].remove(capturable)

                        # Passe au tour suivant, peu importe s'il y a des captures
                        game_state["tour_actif"] = "Barca"
                        game_state["pion_selectionne"] = None
                        game_state["mouvements_possibles"] = []

                    elif pion_selectionne in game_state["pions_blancs"] and game_state["tour_actif"] == "Barca":
                        # Déplacez le pion blanc
                        game_state["pions_blancs"].remove(pion_selectionne)
                        game_state["pions_blancs"].append((ligne, colonne))

                        # Gérer les captures
                        capturable = ((pion_selectionne[0] + ligne) // 2, (pion_selectionne[1] + colonne) // 2)
                        if capturable in game_state["pions_noirs"]:
                            print(f"Capture détectée sur {capturable}")  # Log de la capture
                            game_state["pions_noirs"].remove(capturable)

                        # Passe au tour suivant, peu importe s'il y a des captures
                        game_state["tour_actif"] = "PSG"
                        game_state["pion_selectionne"] = None
                        game_state["mouvements_possibles"] = []

                else:
                    # Si le mouvement n'est pas valide, désélectionner le pion
                    print("Mouvement invalide, désélection du pion.")
                    game_state["pion_selectionne"] = None
                    game_state["mouvements_possibles"] = []

            else:
                # Sélectionnez un pion valide pour le joueur actif (PSG ou Barca)
                if game_state["tour_actif"] == "PSG" and (ligne, colonne) in game_state["pions_noirs"]:
                    game_state["pion_selectionne"] = (ligne, colonne)
                    direction = "bas"  # Les noirs se déplacent vers le bas
                    print(f"Pion sélectionné : {game_state['pion_selectionne']}")  # Log de la sélection
                    game_state["mouvements_possibles"] = calculer_deplacements(
                        (ligne, colonne),
                        game_state["pions_noirs"],
                        game_state["pions_blancs"],
                        direction
                    )
                elif game_state["tour_actif"] == "Barca" and (ligne, colonne) in game_state["pions_blancs"]:
                    game_state["pion_selectionne"] = (ligne, colonne)
                    direction = "haut"  # Les blancs se déplacent vers le haut
                    print(f"Pion sélectionné : {game_state['pion_selectionne']}")  # Log de la sélection
                    game_state["mouvements_possibles"] = calculer_deplacements(
                        (ligne, colonne),
                        game_state["pions_blancs"],
                        game_state["pions_noirs"],
                        direction
                    )

    return True  # Retourner True tant que l'utilisateur ne ferme pas la fenêtre



