from typing import Any
import pygame
import math
import numpy as np

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
        self.rectangle.centerx = raquette.rectangle.centerx
        self.rectangle.centery = raquette.rectangle.centery - raquette.rectangle.height // 2 - self.rayon


    # Deplacement de la balle en tenant compte des collisions avec les bords
    # Augmenté avec collisions briques et raquettes
    def deplacement(self, raquette, briques):
        self.collision_bord()
        self.collision_briques(briques)
        self.collision_raquette(raquette)

        self.update()

        return briques
        
    # Rebond sur un bord du jeu    
    def collision_bord(self):
        if self.rectangle.left <= 0 or self.rectangle.right >= self.limite_largeur:
            self.direction.x *= -1
        if self.rectangle.top <= 0:
            self.direction.y *= -1    

    # Test des collisions avec les briques
    def collision_briques(self, briques):
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

    # Test des collisions avec la raquette. Methode de calcul du rebond encore non arrêtée
    def collision_raquette(self, raquette):
        if self.rectangle.colliderect(raquette.rectangle):
            # Calcul du centre de la raquette
            x_relatif = (self.rectangle.centerx - raquette.rectangle.left) - raquette.rectangle.width / 2
            ratio = x_relatif / (raquette.rectangle.width / 2)
            angle_rebond = ratio * ANGLE_MAX

            # Restreint l'angle possible du rebond
            angle_rebond = max(min(angle_rebond, ANGLE_MAX), -ANGLE_MAX)

            print(f"Xrelatif : {x_relatif} / ratio : {ratio} / rebond : {angle_rebond}" )

            # Calculate the new direction of the ball
            self.direction = pygame.math.Vector2(math.cos(math.radians(angle_rebond)), -math.sin(math.radians(angle_rebond))).normalize()

    
    def update(self) :
        self.rectangle.x += self.vitesse * self.direction[0]
        self.rectangle.y += self.vitesse * self.direction[1]

    def calcul_angle_rebond (self, raquette):
        vecteur_balle = np.array(vecteur_balle, dtype=float)
    
        # Le vecteur normal à la raquette est horizontal
        vecteur_normal = np.array([1, 0], dtype=float)
        
        # Calculer la réflexion du vecteur d'entrée sur le vecteur normal
        normalisé = vecteur_normal / np.linalg.norm(vecteur_normal)
        vecteur_rebond = vecteur_balle - 2 * np.dot(vecteur_balle, normalisé) * normalisé

        distance_impact = abs(self.rectangle.centerx) / (raquette.rectangle.width / 2.0)
        
        # Ajuster la magnitude du vecteur de rebond en fonction de la position d'impact
        facteur_ajustement = 1 + (0.5 * distance_impact) if distance_impact < 0 else 1 - (0.5 * distance_impact)
        
        vecteur_rebond *= facteur_ajustement

        self.direction = vecteur_rebond

    # Calculer la réflexion du vecteur d'entrée sur le vecteur normal
    def calculer_reflexion(vecteur, normal):
        normalisé = normal / np.linalg.norm(normal)
        return vecteur - 2 * np.dot(vecteur, normalisé) * normalisé

    def afficher(self, fenetre):
        fenetre.blit(self.image, self.rectangle)