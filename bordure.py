from typing import Any
import pygame

class Bordure :
    def __init__ (self, largeur : int, hauteur : int, epaisseur : int, couleur):
        self.haut = pygame.Rect(0, 0, largeur, epaisseur)
        self.gauche = pygame.Rect(0, 0, epaisseur, hauteur)
        self.droite = pygame.Rect(largeur-epaisseur, 0, epaisseur, hauteur)
        self.couleur = couleur

    def afficher(self, fenetre):
        pygame.draw.rect(fenetre, self.couleur, self.haut)
        pygame.draw.rect(fenetre, self.couleur, self.gauche)
        pygame.draw.rect(fenetre, self.couleur, self.droite)