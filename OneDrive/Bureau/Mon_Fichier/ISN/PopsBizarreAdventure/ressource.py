 # -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 12:24:56 2019

@author: youss
"""
import pygame
# variables qui seront utiles dessous
i=0
n=0
frame = 0
p = 0
#la position de base du texte des dialogues 
dialogue_x = 50
dialogue_y = 728 
#On garde les valeurs initiales dans d'autres variables
first_x = dialogue_x
first_y = dialogue_y
# on crée une chaîne vide qui sera utile pour animation_text
string = ""
# varible de base False utile pour animation_text
passer = False
finir = False

white = (255,255,255) #référence RGB du blanc
black = (0,0,0) #référence RGB du noir
#Prédispostion nécessaire pour que le son marche correctement 	
pygame.mixer.pre_init(44100, -16, 1, 512)
#On initialise le module de l'écran
pygame.display.init()
#et du son
pygame.mixer.init()
#Pour mieux gérer les touches
keys = pygame.key.get_pressed()
#son qui sera joué pendant les dialogues
sfx_dialogue = pygame.mixer.Sound("text.wav")
#je baisse le volume sinon trop fort
sfx_dialogue.set_volume(0.2)
loading     = pygame.image.load #pour que ce soit plus rapide pour charger des images  
dialogue_box = loading("dialogue/dialogue_box.png") #on charge l'image de la boite de dialogue
#et ceux pour le curseur de la boite de dialogue
curseur = [loading("dialogue/curseur/Sprite-0001.png"),loading("dialogue/curseur/Sprite-0002.png")]

    



class Sprite: #Classe pour définir les attributs d'un sprite rapidement
    
    
    def __init__(self, x, y, heightP, widthP, vel):
        self.x = x
        self.y = y
        self.height = heightP
        self.width  = widthP
        self.vel = self.slow = vel
        self.acc = self.slow + 5
        self.front  = True
        self.back  = False
        self.right = False
        self.left  = False
        self.dialogue = False
        self.commande = True
        self.animation = False
        
   
    def walking(self,screen): #frame à l'image quand il marche sur la carte
        global i 
        standpops   = loading("pops-walking.png")
        rightpops   = loading("Illustration226.png")
        backpops    = loading("Illustration225.png")  
        leftpops    = loading("Illustration224.png")
        #Si le sprite est de face
        if self.front:
            #afficher le sprite de face
            screen.blit(standpops, (self.x,self.y))
        #si le sprite est dirigé vers la droite    
        if self.right:
            #afficher le sprite de droite
            screen.blit(rightpops, (self.x,self.y))
        #si le sprite est de dos    
        elif self.back:
            #afficher le sprite de dos
            screen.blit(backpops, (self.x,self.y))
        #si le sprite est de gauche
        elif self.left:
            #afficher le sprite de gauche
            screen.blit(leftpops, (self.x,self.y))    
    
    #Pour aller plus vite, j'ai créé des méthodes qui tournent le sprite
    def set_right(self):
        self.right = True
        self.left  = False
        self.front = False
        self.back  = False
        
    def set_left(self):
        self.right = False
        self.left  = True
        self.front = False
        self.back  = False
        
    def set_front(self):
        self.right = False
        self.left  = False
        self.front = True
        self.back  = False
        
    def set_back(self):
        self.right = False
        self.left  = False
        self.front = False
        self.back  = True
    
    #Je vais mettre des accesseurs et des mutateurs maintenant
    def dialogue_get(self):
        return self.dialogue
    
    def commande_get(self):
        return self.commande
    
    def animation_get(self):
        return self.animation
    # mutateurs
    def set_dialogue(self,state):
        self.dialogue = state
    
    def set_commande(self,state):
       self.commande = state
        
    def set_animation(self,state):
        self.animation = state
        
#Fonction pour faire apparaître les lettres les unes après les autres
def animation_text(text,screen,sprite):
    global white,black
    global dialogue_x,dialogue_y,first_x,first_y,curseur
    global string,passer,finir
    global n,frame,p
    
    #on définit la police d'écriture et la taille
    font = pygame.font.Font("VCR_OSD_MONO_1.001.ttf",30)   
    
    #On regarde s'il y a un évenement
    pygame.event.pump()
    
    #puis on appelle la méthode qui affiche le sprite
    sprite.walking(screen)
    #une frame sur deux
    if n%2 == 0:
        #on affiche la boite de dialogue
        screen.blit(dialogue_box,(33,700))
    #Sinon sur l'autre frame
    else:
        #on affiche le boite dialogue et les lettres déjà affichées
        screen.blit(dialogue_box,(33,700))
        screen.blit(font.render(string,False,white),(first_x,first_y))
    
    
    #Si les commandes sont actives    
    if sprite.commande:
        #on les désactives et on lance l'animation du texte
        sprite.commande = False
        sprite.animation = True
    
    
    #Pour chaque évenement comme apuuyer sur une touche
    for event in pygame.event.get():
        #si l'évenement est une touche et que ce n'est ni Haut, Bas, Droite ou Gauche
        if event.type == pygame.KEYDOWN and not event.key in (pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT):
            #Si l'animation du texte est toujours active
            if sprite.animation:
                # on active le passage du texte
                passer = True
            # si le processus pour finir le dialogue est activé    
            if finir:
                #on réinitialise les variables
                n = 0
                string = ""
                finir = False
                dialogue_x = first_x
                dialogue_y = first_y
                #et on désactive les dialogues et on réactive les dialogues
                sprite.dialogue = False
                sprite.commande = True
    # si le processus de passage est activé
    if passer:
        #on affiche le texte entier
        i = font.render(text, False, white)
        screen.blit(i,(first_x,first_y))
        # puis on désactive l'animation
        sprite.animation = False  
        #puis on désactive le processus de passage et on active le processus de fin
        passer = False
        finir = True

    #si l'animation du texte est activé   
    if sprite.animation:
        #une frame sur deux
        if n%2 == 0:
            # pour réguler les frames
            m = int(n/2)
            #on affiche toutes les lettres qui ont été affiché auparavant
            j = font.render(string,False,white)
            screen.blit(j,(first_x,first_y)) 
            #puis on met à jour le string
            string += text[m]
            #puis on fait apparaître la lettre suivante
            i = font.render(text[m],False,white)
            #aux coordonées données
            screen.blit(i,(dialogue_x,dialogue_y))
            #une frame sur quatre
            if n%4 == 0:
                #jouer le son de lecture de texte
                sfx_dialogue.play()
            #puis on ajoute la taille d'un caractère en abscisse pour donner l'impression
            #que tout est normal et attaché comme dans un logiciel de traitement de texte
            dialogue_x += (font.size(text)[0] / len(text)) 
            #puis on met à jour l'écran
            pygame.display.update()
        #Puis on incrémente 1 à n pour simuler les frames
        n += 1
    #si la frame correspond à la longueur du texte (en gros la dernière lettre vient d'être afficher)
    if n == len(text)*2 - 1:
        #on désactive l'animation et on réinitialise n et on active le processus de fin
        sprite.animation = False
        n = 0
        finir = True
    #si l'animation est désactivée
    if not sprite.animation:
        #si la p est = à 59 en gros  il s'est passé 60 frames
        if p == 59:
            #on réinitialise p
            p = 0        
        #on affiche le texte en entier
        i = font.render(text, False, white)
        screen.blit(i,(first_x,first_y))
        #puis on on fait une animation de 4 images du curseur de la boîte de dialogue
        #en attendant un réponse du joueur pour continuer
        if p<15 or p >= 30 and p < 45: 
            frame = 0
        elif p >= 15 and p < 30 or p >= 45:
            frame = 1
        screen.blit(curseur[frame],(940,950))
        p += 1
