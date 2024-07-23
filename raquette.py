import pygame

ANGLE_MAX = 40

VITESSE_DEPLACEMENT = 15

class Raquette(pygame.sprite.Sprite):
    def __init__(self, x : int, y : int, largeur : int, epaisseur : int, couleur):
        super().__init__()
        self.largeur = largeur
        self.epaisseur = epaisseur
        self.surface = pygame.Surface((largeur, epaisseur))
        self.rectangle = self.surface.get_rect()
        self.couleur = couleur
        self.surface.fill(couleur)
        self.rectangle.x = x
        self.rectangle.y = y
        self.vitesse = VITESSE_DEPLACEMENT

    def set_taille (self, largeur):
        self.size = largeur

    def set_vitesse (self, vitesse):
        self.vitesse = vitesse

    # Definit quelle zone a été touchée (gauche, centre ou droite de la raquette)
    # Les trois zones occupent chacune 1/3 de la raquette
    def zone_contact (self, balle):
        normalise = 100 * (balle.rectangle.centerx - self.rectangle.left) / (self.rectangle.width)
        if normalise < 33 :
            return -1
        if normalise > 66 :
            return 1
        return 0
        
        
    
    # Deplacement de la raquette du joueur
    def bouger_raquette (self, gauche, droite, largeur_ecran) :
        if gauche:
            if not self.rectangle.left <= 0:
                self.rectangle.x -= self.vitesse
        elif droite:
            if not self.rectangle.right >= largeur_ecran:
                self.rectangle.x += self.vitesse
        return self

    def afficher(self, fenetre):
        pygame.draw.rect(fenetre, self.couleur, self.rectangle)