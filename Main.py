import pygame
import sys
from balle import Balle
from brique import Brique
from raquette import Raquette
from jeu import Jeu
from bordure import Bordure
from bouton import Bouton, BoutonRecommencer, BoutonQuitter


def generation_briques(nombre_largeur, nombre_hauteur):
    # Génération des briques (un gros rectangle pour le moment)
    LARGEUR_BRIQUE_0 = 58
    HAUTEUR_BRIQUE_0 = 20
    
    ALIGNEMENT_GAUCHE = 250
    ALIGNEMENT_HAUT = 150

    ensemble_briques = pygame.sprite.Group()

    for i in range(nombre_largeur) :
        for j in range(nombre_hauteur) :
            brique = Brique(ALIGNEMENT_GAUCHE + (i * 60), ALIGNEMENT_HAUT + (j * 30), LARGEUR_BRIQUE_0, HAUTEUR_BRIQUE_0, 1)
            ensemble_briques.add(brique)
    
    return ensemble_briques



# Initialisation de Pygame
pygame.init()
police = pygame.font.SysFont(None, 36)
police_fin = pygame.font.SysFont(None, 100)

# Taille de la fenêtre
LARGEUR = 1200
HAUTEUR = 800
FPS = 60

# Création de la fenêtre
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Casse-Brique")
clock = pygame.time.Clock()

# Image de fond
img = pygame.image.load('image_fond.jpg').convert()

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRIS = (128, 128, 128)

# Informations générales du jeu
NOMBRE_VIES_INITIALES = 5
jeu = Jeu(NOMBRE_VIES_INITIALES)

#Balle
BALLE_POSITION_INITIALE = (200, 500)
DIRECTION = pygame.math.Vector2(1, 1).normalize()
VITESSE_BALLE = 6
balle = Balle(BALLE_POSITION_INITIALE[0], BALLE_POSITION_INITIALE[1], 5, ROUGE, DIRECTION, 0, LARGEUR, HAUTEUR)

# Raquette
RAQUETTE_POSITION_INITIALE = (400, HAUTEUR - 50)
RAQUETTE_LARGEUR_INITIALE = 100
RAQUETTE_EPAISSEUR_INITIALE = 10
raquette = Raquette(RAQUETTE_POSITION_INITIALE[0], RAQUETTE_POSITION_INITIALE[1], RAQUETTE_LARGEUR_INITIALE, RAQUETTE_EPAISSEUR_INITIALE, BLANC)


# Touches enfoncées ou non
touche_gauche_enfoncee = False
touche_droite_enfoncee = False

# Gestions des boutons (pour recommencer par exemple)
boutons = []

# Pour lancer la balle
debut = True

# On crée notre amas de briques
ensemble_briques = generation_briques(10, 5)

# Boucle principale du jeu
running = True
while running:

    # Gestion des événements (bouger raquette)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: # On appuie sur une touche
            if debut :
                debut = False
                balle.vitesse = VITESSE_BALLE
            if event.key == pygame.K_LEFT:
                touche_gauche_enfoncee = True
            elif event.key == pygame.K_RIGHT:
                touche_droite_enfoncee = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                touche_gauche_enfoncee = False
            elif event.key == pygame.K_RIGHT:
                touche_droite_enfoncee = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche de la souris
                for bouton in boutons:
                    if bouton.rect.collidepoint(event.pos):
                        bouton.action()
                    

    # Traiter les touches enfoncées
    raquette.bouger_raquette(touche_gauche_enfoncee, touche_droite_enfoncee, LARGEUR)

    # Test des collisions avec les briques
    for brique in ensemble_briques:
        if balle.rect.colliderect(brique.rect):
            if balle.rect.left <= brique.rect.right and balle.rect.right >= brique.rect.left:
                balle.direction.y *= -1  
            else:
                balle.direction.x *= -1  
            brique.touche()
            brique.couleur()
            if brique.detruit():
                ensemble_briques.remove(brique)

 #   if ensemble_briques.empty:
 #       jeu.niveauSuivant()

    # Test des collisions avec les raquettes
    if balle.rect.colliderect(raquette.raquette):
        balle.direction = raquette.rebond_raquette(balle)

    # Bouger la balle
    balle.deplacement()

    # Effacer l'écran avec la couleur de fond
    # fenetre.fill(NOIR)
    fenetre.blit(img, (0, 0))

    # Gèrer la sortie de terrain
    if balle.y > HAUTEUR :
        jeu.perds_vie()
        if jeu.getVie():
            boutons.add(BoutonRecommencer(200, 400))
            boutons.add(BoutonQuitter(200, 800))


    # Afficher les bordures, la raquette et la balle
    raquette.afficher(fenetre)
    balle.afficher(fenetre)

    # Afficher les briques
    ensemble_briques.draw(fenetre)

    # Mettre à jour l'affichage
    pygame.display.flip()
    clock.tick(FPS)


# Quitter Pygame
pygame.quit()
sys.exit()