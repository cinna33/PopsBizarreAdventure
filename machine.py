import pygame
import numpy 
pygame.init()

# creer une classe qui va gérer la notion d'emplacement
class Emplacement(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('projectile/bar.png').convert
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def set_image(self, image):
        self.image = image
    
 # definir une fonction lancement
 
def lancement(): 
    global jetons

    # choix au hasard selon les probabilités
    hasard = numpy.random.choice(fruits, 3, p=proba_fruits)
    fruit_gauche = fruits_dict[hasard[0]]
    fruit_milieu = fruits_dict[hasard[1]]
    fruit_droite = fruits_dict[hasard[2]]

    # changement des images
    emplacement_gauche.set_image(fruit_gauche)
    emplacement_milieu.set_image(fruit_milieu)
    emplacement_droite.set_image(fruit_droite)

    # faire la verification des lots
    if hasard[0] == hasard[1] == hasard[2]: # les 3 premiers fruits sont identique
        fruit = hasard[0]
        jetons_gagnes = fruits_dict_gains[fruit]
        jetons += jetons_gagnes 
        jackpot.play()
        ecran.blit((30,0))
                

 # creation de la fenetre
largeur = 1280
hauteur = 720
pygame.display.set_caption("Machine à sous")
purple = [242, 122, 218] # couleur violette 
ecran = pygame.display.set_mode((largeur, hauteur), pygame.RESIZABLE)
 
# argent du joueur
jetons = 100

# dictionnaire de fruits
image_test = pygame.image.load('projectile/bouteille.png')
fruits_dict = {
"bière": pygame.image.load('projectile/bière.png'),
"ananas": pygame.image.load('ananas.png'),
"bouteille": pygame.image.load('projectile/bouteille.png'),
"capsule": pygame.image.load('projectile/capsule.png'),
"bar": pygame.image.load('projectile/bar.png')
}

# liste stockant le nom de chaque fruit
fruits = ["ananas", "bière", "bouteille", "capsule", "bar"]
proba_fruits = [0.2, 0.25, 0.4, 0.1, 0.05]

fruits_dict_gains = {
"bouteille": 5,
"bière": 15,
"ananas": 20,
"capsule": 30,
"bar": 50
}

 # chargement des emplacements
hauteur_emplacement = hauteur / 4
emplacement_x_milieu = largeur / 4 + 64
emplacement_x_gauche = emplacement_x_milieu - image_test.get_width() - 22
emplacement_x_droite = emplacement_x_milieu + image_test.get_width() + 20

emplacements = pygame.sprite.Group()
emplacement_gauche = Emplacement(emplacement_x_gauche, hauteur_emplacement)
emplacement_milieu = Emplacement(emplacement_x_milieu, hauteur_emplacement)
emplacement_droite = Emplacement(emplacement_x_droite, hauteur_emplacement)

# rangement des emplacements dans le groupe
emplacements.add(emplacement_gauche)
emplacements.add(emplacement_milieu)
emplacements.add(emplacement_droite)

# charger l'image de l'arriere plan
fond = pygame.image.load('machine3.png')
police = pygame.font.SysFont("comicsansms", 30)

#différents bruitages
pygame.mixer.fadeout(300) #Fondu à 300ms de la fin de tous les objets Sound
jackpot = pygame.mixer.Sound("bruitages/jackpot.wav")
defaite = pygame.mixer.Sound("bruitages/defaite.wav")



running = True
while running:

    ecran.fill(purple)
    ecran.blit(fond, (0, 0))
    emplacements.draw(ecran)

    # afficher son nombre de jetons
    text = police.render(str(jetons) + " jetons", True, (0, 0, 0))
    ecran.blit(text, (10, 0))
    
    pygame.display.flip() #rafraichissement de l'écran 
    
    for event in pygame.event.get():
        # verifier si le joueur ferme la fenetre
        if event.type == pygame.QUIT:
            running = False
            quit()
        # verifier si le joueur appuie sur une touche
        if event.type == pygame.KEYDOWN:
            # si la touche est la touche ESPACE
            if event.key == pygame.K_SPACE and jetons >= 5:
                lancement() # appeler la fonction
                jetons -= 5
                defaite.stop()
                if jetons == 0: 
                    ecran.blit((30,0))
                    defaite.play()
            elif event.key == pygame.K_ESCAPE: 
                running = False 
                quit()
pygame.quit()
ecran.display.flip() #rafraichir l'écran 

