import pygame

NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRIS = (128, 128, 128)

ORDRE_COULEURS=[BLANC, VERT, BLEU, JAUNE, ROUGE]



class Brique(pygame.sprite.Sprite):
    def __init__(self, positionX, positionY, largeur, hauteur, nbVies):
        super().__init__()
        self.nbVies = nbVies
        self.image = pygame.Surface((largeur, hauteur))
        self.image.fill(ORDRE_COULEURS[nbVies + 1])
        self.rect = self.image.get_rect(topleft=(positionX, positionY)) 
    
    def touche(self):
        self.nbVies -= 1

    def detruit(self):
        if self.nbVies <= 0:
            return True
        
    def couleur(self):
        self.image.fill(ORDRE_COULEURS[self.nbVies + 1])
    
    def afficher(self, fenetre):
        pygame.draw.rect(fenetre, self.couleur, self.rect)