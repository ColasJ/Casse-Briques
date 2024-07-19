import pygame
import sys
import os
from balle import Balle
from brique import Brique
from raquette import Raquette
from jeu import Jeu
from bouton import Bouton, BoutonRecommencer, BoutonQuitter


# Taille de la fenêtre
LARGEUR = 1200
HAUTEUR = 800
FPS = 60

# Chemin de base pour les images
CHEMIN_IMAGES = os.path.join(os.path.dirname(__file__), 'images')

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

# Raquette
RAQUETTE_POSITION_INITIALE = (400, HAUTEUR - 20)
RAQUETTE_LARGEUR_INITIALE = 150
RAQUETTE_EPAISSEUR_INITIALE = 20

# Génération des briques (un gros rectangle pour le moment)
LARGEUR_BRIQUE_0 = 59
HAUTEUR_BRIQUE_0 = 29
    
#Balle
VITESSE_BALLE = 6
RAYON_BALLE = 8


###########################################################################

 # Générateur simplifié de briques
def generation_briques(nombre_largeur, nombre_hauteur):
    alignement_gauche = 250
    alignement_haut = 150    

    briques = pygame.sprite.Group()

    for i in range(nombre_largeur) :
        for j in range(nombre_hauteur) :
            brique = Brique(alignement_gauche + (i * 60), alignement_haut + (j * 30), LARGEUR_BRIQUE_0, HAUTEUR_BRIQUE_0, 1)
            briques.add(brique)
    
    return briques

# Charger une image à partir du chemin de base
def charger_image(nom_image):
    chemin_image = os.path.join(CHEMIN_IMAGES, nom_image)
    image = pygame.image.load(chemin_image).convert_alpha()
    return image

# Gèrer la sortie de terrain
def test_sortie():
    if balle.rectangle.bottom >= HAUTEUR :
        jeu.perds_vie()
        if jeu.get_vies() <= 0:
            boutons.add(BoutonRecommencer(200, 400))
            boutons.add(BoutonQuitter(200, 800))

# Afficher balle, raquette et toutes les briques
def affichage(balle, raquette, briques):
    raquette.afficher(fenetre)
    balle.afficher(fenetre)

    for brique in briques :
        if brique.detruit() :
            briques.remove(brique)
        else :
            brique.afficher(fenetre)


###########################################################################

# Initialisation de Pygame
pygame.init()
police = pygame.font.SysFont(None, 36)
police_fin = pygame.font.SysFont(None, 100)

# Création de la fenêtre
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Casse-Brique")
clock = pygame.time.Clock()

# Chargement des images
img_fond = charger_image('image_fond.jpg')
img_balle = charger_image('balle.png')
img_balle = pygame.transform.scale(img_balle, (RAYON_BALLE * 2, RAYON_BALLE * 2))

# Informations générales du jeu
NOMBRE_VIES_INITIALES = 5
jeu = Jeu(NOMBRE_VIES_INITIALES)

# On créer un ensemble de Sprites pour regrouper tous les objets
ensemble_sprites = pygame.sprite.Group()

# Création de la raquette
raquette = Raquette(RAQUETTE_POSITION_INITIALE[0], RAQUETTE_POSITION_INITIALE[1], RAQUETTE_LARGEUR_INITIALE, RAQUETTE_EPAISSEUR_INITIALE, BLANC)
ensemble_sprites.add(raquette)

# Création de la balle
balle = Balle(RAYON_BALLE, img_balle, 0, HAUTEUR, LARGEUR)
balle.init_position(raquette)
ensemble_sprites.add(balle)

# On crée notre amas de briques
ensemble_briques = generation_briques(10, 5)
ensemble_sprites.add(ensemble_briques)

# Touches enfoncées ou non
touche_gauche_enfoncee = False
touche_droite_enfoncee = False

# Gestions des boutons (pour recommencer par exemple)
boutons = []

# Pour lancer la balle
debut = True

###################################################################################

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
                    if bouton.rectangle.collidepoint(event.pos):
                        bouton.action()
                    

    # Traiter les touches enfoncées 
    raquette.bouger_raquette(touche_gauche_enfoncee, touche_droite_enfoncee, LARGEUR)

    # Mechaniques du jeu
    balle.deplacement(raquette, ensemble_briques)
    test_sortie()

    # Affichages
    fenetre.blit(img_fond, (0, 0))
    affichage(balle, raquette, ensemble_briques)

    pygame.display.flip()
    clock.tick(FPS)


# Quitter Pygame
pygame.quit()
sys.exit()