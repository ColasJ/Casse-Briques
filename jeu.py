import pygame

class Jeu :

    def __init__ (self, vies : int):
        self.vies = vies
        self.niveau = 0

    def levelUp (self):
        self.niveau += 1

    def perdsVie (self, fenetre): 
        self.vies -= 1  
        if self.vies == 0:
            return True
        else:
            return False
 
    def afficherVies (self, fenetre, police):   
        fenetre.blit(police.render("Vies : " + str(self.vies), True, (255, 255, 255)), (10, 10))

    def afficherNiveau (self, fenetre, police):   
        fenetre.blit(police.render("Niveau : " + str(self.niveau), True, (255, 255, 255)), (100, 10))