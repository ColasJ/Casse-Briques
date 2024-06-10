import pygame

class Bouton:
    def __init__(self, x, y, largeur, hauteur, couleur, texte, police):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.couleur = couleur
        self.texte = texte
        self.police = pygame.font.SysFont(None, police)
        self.texte_surface = self.police.render(str(texte), True, (0, 0, 0))
        self.texte_rect = self.texte_surface.get_rect(center=self.rect.center)
    
    def dessiner(self, surface):
        pygame.draw.rect(surface, self.couleur, self.rect)

    def action(self):
        None

class BoutonRecommencer (Bouton):
    def __init__(self, x, y):
        super().__init__(self, x, y, 200, 400, (255, 255, 255), "Recommencer", 36)

    def action(self):
        super().action

class BoutonQuitter (Bouton):
    def __init__(self, x, y):
        super().__init__(self, x, y, 200, 400, (255, 255, 255), "Quitter", 36)

    def action(self):
        super().action
        