'''
Nom    : Jeu_des_Dames.py
Auteur : Jean-Christophe Serrano
Date   : 22.11.2024
'''

#pygame à installer sur les deux postes
import pygame
import sys

from pygame import KEYDOWN


def dessine_case(case_pos):
    global screen, case_size, cases_blanches, cases_noires, marge_gauche, marge_haut
    color = cases_blanches if case_pos % 2 == 0 else cases_noires
    pygame.draw.rect(
        screen,
        color,
        (marge_gauche + case_pos * case_size, marge_haut, case_size, case_size))

def bouge_droite():
    global pion_pos, nb_colonnes, marge_haut, marge_gauche, case_size
    if pion_pos < nb_colonnes-1:
        dessine_case(pion_pos)
        pion_pos += 1
        screen.blit(pion, (marge_gauche + case_size*pion_pos, marge_haut))

def bouge_gauche():
    global pion_pos, nb_colonnes, marge_haut, marge_gauche, case_size
    if pion_pos > 0:
        dessine_case(pion_pos)
        pion_pos -= 1
        screen.blit(pion, (marge_gauche + case_size*pion_pos, marge_haut))

#MAIN

case_size = 50
cases_blanches = (255, 255, 255)
cases_noires = (0, 0, 0)
pions_blancs = (255, 255, 255)
pions_noirs = (0, 0, 0)

# Marges autour du damier
marge_gauche = 0
marge_droite = 0
marge_haut = 0
marge_bas = 0

pion_pos = 0

plateau = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

nb_lignes = len(plateau)
nb_colonnes = len(plateau)

pygame.init()

screen = pygame.display.set_mode((500,500))

pygame.display.set_caption("MA-24 : Bases de pygame")

screen.fill((20, 152, 255))

for i in range(nb_lignes):
    for n in range(nb_colonnes):
        x = i * case_size
        y = n * case_size
        dessine_case(i+n)



running = True

pion = pygame.image.load("MA-24_pion.png")
pion = pygame.transform.scale(pion, (case_size, case_size))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                bouge_droite()
            elif event.key == pygame.K_LEFT:
                bouge_gauche()
            elif event.key == pygame.K_q:
                running = False
        pygame.display.update()



    screen.blit(pion, (marge_gauche + case_size * pion_pos, marge_haut))

    pygame.display.flip()

pygame.quit()
sys.exit()

