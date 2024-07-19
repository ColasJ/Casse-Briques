import pygame
import math
from bordure import Bordure

ANGLE_MAX = 40

class Raquette(pygame.sprite.Sprite):
    def __init__(self, x : int, y : int, largeur : int, epaisseur, couleur):
        super().__init__()
        self.largeur = largeur
        self.surface = pygame.surface
        self.raquette = pygame.Rect(x, y, largeur, epaisseur)
        self.couleur = couleur
        self.vitesse = 10

    def set_taille (self, largeur):
        self.size = largeur

    def set_vitesse (self, vitesse):
        self.vitesse = vitesse

    def rebond_raquette(self, balle):
        
        # Calcul du centre de la raquette
        x_relatif = (balle.rect.centerx - self.raquette.left) - self.raquette.width / 2
        ratio = x_relatif / (self.raquette.width / 2)
        angle_rebond = ratio * ANGLE_MAX

        print(f"Xrelatif : {x_relatif} / ratio : {ratio} / rebond : {angle_rebond}" )

        # Restreint l'angle possible du rebond
        angle_rebond = max(min(angle_rebond, ANGLE_MAX), -ANGLE_MAX)

        # Calculate the new direction of the ball
        nouvelle_direction = pygame.math.Vector2(math.cos(math.radians(angle_rebond)), -math.sin(math.radians(angle_rebond))).normalize()
        return nouvelle_direction
    
    # Deplacement de la raquette du joueur
    def bouger_raquette (self, gauche, droite, largeur_ecran) :
        if gauche:
            if not self.raquette.left <= 0:
                self.raquette.x -= self.vitesse
        elif droite:
            if not self.raquette.right >= largeur_ecran:
                self.raquette.x += self.vitesse
        return self

    def afficher(self, fenetre):
        pygame.draw.rect(fenetre, self.couleur, self.raquette)