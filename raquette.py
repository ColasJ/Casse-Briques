import pygame
import math
from bordure import Bordure

ANGLE_MAX = 45

class Raquette(pygame.sprite.Sprite):
    def __init__(self, x : int, y : int, largeur : int, epaisseur, couleur):
        super().__init__()
        self.largeur = largeur
        self.raquette = pygame.Rect(x, y, largeur, epaisseur)
        self.couleur = couleur
        self.vitesse = 10

    def setTaille (self, largeur):
        self.size = largeur

    def setVitesse (self, vitesse):
        self.vitesse = vitesse

    def rebondRaquette(self, balle):
        x_relatif = (balle.rect.centerx - self.raquette.left) - self.raquette.width / 2
        ratio = x_relatif / (self.raquette.width / 2)
        bounce_angle = ratio * ANGLE_MAX
        if bounce_angle < 20:
            bounce_angle = 20

        # Calculer la nouvelle direction de la ballee
        return pygame.math.Vector2(math.cos(math.radians(bounce_angle)), -math.sin(math.radians(bounce_angle))).normalize()
    
    # Deplacement de la raquette du joueur
    def bougerRaquette (self, gauche, droite, largeur_ecran) :
        if gauche:
            if not self.raquette.left <= 0:
                self.raquette.x -= self.vitesse
        elif droite:
            if not self.raquette.left >= largeur_ecran:
                self.raquette.x += self.vitesse
        return self

    def afficher(self, fenetre):
        pygame.draw.rect(fenetre, self.couleur, self.raquette)