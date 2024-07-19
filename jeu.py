
class Jeu :

    def __init__ (self, vies : int):
        self.vies = vies
        self.niveau = 0

    def level_up (self):
        self.niveau += 1

    def perds_vie (self): 
        self.vies -= 1  
        
    def get_vies (self):
        return self.vies
 
    def afficher_vies (self, fenetre, police):   
        fenetre.blit(police.render("Vies : " + str(self.vies), True, (255, 255, 255)), (10, 10))

    def afficher_niveau (self, fenetre, police):   
        fenetre.blit(police.render("Niveau : " + str(self.niveau), True, (255, 255, 255)), (100, 10))