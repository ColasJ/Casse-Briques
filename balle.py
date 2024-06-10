from brique import Brique
import math
import pygame

class Balle (pygame.sprite.Sprite):
    def __init__(self, x, y, rayon, couleur, direction, vitesse, largeur, hauteur):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((rayon*2, rayon*2))
        self.rect = self.image.get_rect(center=(x, y))
        self.vitesse = vitesse
        self.couleur = couleur
        self.rayon = rayon
        self.direction = direction
        self.largeur_max = largeur
        self.hauteur_max = hauteur
        print (str(self.rect.center))

    def deplacement(self):
        if self.rect.left < 0 or self.rect.right > self.largeur_max:
            self.direction.x *= -1
        if self.rect.top < 0:
            self.direction.y *= -1
        if self.rect.bottom > self.hauteur_max :
            return True
        
        self.x += self.vitesse * self.direction[0]
        self.y += self.vitesse * self.direction[1]

        self.rect.center = (self.x, self.y)

        
    def afficher(self, fenetre):
        pygame.draw.circle(fenetre, self.couleur, (int(self.x), int(self.y)), self.rayon)