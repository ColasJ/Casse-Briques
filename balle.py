from typing import Any
import pygame
import math
import os

DIRECTION_INITIALE = pygame.math.Vector2(1, -1).normalize()
ANGLE_MAX = 45

class Balle (pygame.sprite.Sprite):
    def __init__(self, rayon, image, vitesse, limite_hauteur, limite_largeur):
        super().__init__()
        self.surface = pygame.Surface((rayon*2, rayon*2))
        self.rectangle = self.surface.get_rect()
        self.rayon = rayon
        self.image = image
        self.direction = DIRECTION_INITIALE
        self.vitesse = vitesse
        self.limite_hauteur = limite_hauteur
        self.limite_largeur = limite_largeur


    # On positionne la balle au centre de la raquette
    def init_position(self, raquette):
        self.rectangle.x = raquette.rectangle.x + raquette.rectangle.width / 2 - self.rayon
        self.rectangle.y = raquette.rectangle.y - raquette.rectangle.height / 2 - 5


    # Deplacement de la balle en tenant compte des collisions avec les bords
    # Augmenté avec collisions briques et raquettes
    def deplacement(self, raquette, briques):
        if self.rectangle.left <= 0 or self.rectangle.right >= self.limite_largeur:
            self.direction.x *= -1
        if self.rectangle.top <= 0:
            self.direction.y *= -1
        
        self.collision_briques(briques)
        self.collision_raquette(raquette)

        self.update()

        return briques
        

    def collision_briques(self, briques):
        # Test des collisions avec les briques
        for brique in briques:
            if self.rectangle.colliderect(brique.rectangle):
                # On calcule le contre de la balle et de la brique pour déterminer l'endroit de la collision
                overlap_x = min(self.rectangle.right - brique.rectangle.left, brique.rectangle.right - self.rectangle.left)
                overlap_y = min(self.rectangle.bottom - brique.rectangle.top, brique.rectangle.bottom - self.rectangle.top)
                
                if overlap_x < overlap_y:
                    self.direction.x *= -1
                else:
                    self.direction.y *= -1
                
                brique.touche()


    def collision_raquette(self, raquette):
        if self.rectangle.colliderect(raquette.rectangle):
            # Calcul du centre de la raquette
            x_relatif = (self.rectangle.centerx - raquette.rectangle.left) - raquette.rectangle.width / 2
            ratio = x_relatif / (raquette.rectangle.width / 2)
            angle_rebond = ratio * ANGLE_MAX

        #    print(f"Xrelatif : {x_relatif} / ratio : {ratio} / rebond : {angle_rebond}" )
    
            # Restreint l'angle possible du rebond
            angle_rebond = max(min(angle_rebond, ANGLE_MAX), -ANGLE_MAX)

            # Calculate the new direction of the ball
            self.direction = pygame.math.Vector2(math.cos(math.radians(angle_rebond)), -math.sin(math.radians(angle_rebond))).normalize()

    
    def update(self) :
        self.rectangle.x += self.vitesse * self.direction[0]
        self.rectangle.y += self.vitesse * self.direction[1]


    def afficher(self, fenetre):
        fenetre.blit(self.image, self.rectangle)