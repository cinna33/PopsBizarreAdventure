 # -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 12:24:56 2019

@author: youss
"""
import pygame
#variable utiles pour les algorithmes plus bas qui sont réinitialisé
i=0
n=0
frame = 0
p = 0
#coordonnées du texte dans les dialogues
dialogue_x = 50
dialogue_y = 728 
#on garde les valeurs initiales dans d'autres variables
first_x = dialogue_x
first_y = dialogue_y
#on crée une chaîne vide pour  conserver les anciennes lettres dans animation_text
string = ""
#les processus de passage et de fin sont de base désactivés
passer = False
finir = False

white = (255,255,255) #référence RGB du blanc
black = (0,0,0) #référence RGB du noir

#Prédisposition pour que le son marche bien 	
pygame.mixer.pre_init(44100, -16, 1, 512)
#on démarre le module de l'écran
pygame.display.init()
#on démarre le son
pygame.mixer.init()

keys = pygame.key.get_pressed()
#on charge le son de lecture des textes
sfx_dialogue = pygame.mixer.Sound("text.wav")
#et on baisse le son
sfx_dialogue.set_volume(0.2)
loading     = pygame.image.load #pour que ce soit plus rapide pour charger des images  
#et on charge les images nécessaires
dialogue_box = loading("dialogue/dialogue_box.png")
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
        
        if self.front:
            #affiche le sprite de face et etc grâce aux valeurs
            #données par la rubriques Commandes dans PopsBizarreAdventure.py
            screen.blit(standpops, (self.x,self.y))
        if self.right:
            screen.blit(rightpops, (self.x,self.y))
        elif self.back:
            screen.blit(backpops, (self.x,self.y))
        elif self.left:
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
    font = pygame.font.Font("VCR_OSD_MONO_1.001.ttf",30)   
    pygame.event.pump()
    sprite.walking(screen)
    #une frame sur deux
    if n%2 == 0:
        #on affiche la boite de dialogue
        screen.blit(dialogue_box,(33,700))
    else:
        #on affiche la boite de dialogue
        screen.blit(dialogue_box,(33,700))
        #et le texte qui a déjà été affiché
        screen.blit(font.render(string,False,white),(first_x,first_y))
    #si les commandes sont actives
    if sprite.commande_get():
        #On les désactive et on active l'animation du texte
        sprite.set_commande(False)
        sprite.set_animation(True)
    #On récupere les events
    for event in pygame.event.get():
        #si l'event est une touche et ce n'est ni Haut, Bas, Gauche ou Droite
        if event.type == pygame.KEYDOWN and not event.key in (pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT):
            #Si l'animation est en cours
            if sprite.animation_get():
                #on active le processus de passage
                passer = True
            #si le processus de fin est activé
            if finir:
                #on réinitialise les variables
                n = 0
                string = ""
                finir = False
                dialogue_x = first_x
                dialogue_y = first_y
                #et on désactive les dialogues et active les commandes
                sprite.set_dialogue(False)
                sprite.set_commande(True)
    
    
    #si processus de passage activé
    if passer:
        #on affiche le texte en entier
        i = font.render(text, False, white)
        screen.blit(i,(first_x,first_y))
        #on désactive l'animation
        sprite.set_animation(False) 
        #et on désactive le processus de passage et active le processus de fin
        passer = False
        finir = True

    # si le processus d'animation est activé    
    if sprite.animation_get():
        #une frame sur deux
        if n%2 == 0:
            #pour réguler les frames
            m = int(n/2)
            #puis on fait afficher les lettres déjà passées
            j = font.render(string,False,white) 
            screen.blit(j,(first_x,first_y))
            #puis on ajoute la lettre suivante à string pour la réafficher à la prochaine frame
            string += text[m]
            #puis on affiche la prochaine lettre au coordonnées données
            i = font.render(text[m],False,white)
            screen.blit(i,(dialogue_x,dialogue_y))
            #une frame sur quatre
            if n%4 == 0:
                #jouer le son de texte
                sfx_dialogue.play()
            #on ajoute la taille d'un caractère pour donner l'impression
            #que c'est comme dans un logiciel de traitement de texte
            dialogue_x += (font.size(text)[0] / len(text)) 
            #puis on met à jour l'écran
            pygame.display.update()
        #puis on incrémente pour simuler les frames
        n += 1
    #si la dernière lettre a été affichée
    if n == len(text)*2 - 1:
        #on désactive le processus d'animation et on active le processus de fin
        sprite.set_animation(False)
        finir = True
    # si animation désactivée
    if not sprite.animation_get():
        #si c'est la 60ème frame
        if p == 59:
            #on remet à 0
            p = 0        
        #on affiche tout le texte
        i = font.render(text, False, white)
        screen.blit(i,(first_x,first_y))
        #puis on fait l'animation en 4 images
        if p<15 or p >= 30 and p < 45: 
            frame = 0
        elif p >= 15 and p < 30 or p >= 45:
            frame = 1
        screen.blit(curseur[frame],(940,950))
        # puis on incrémente pour simuler les frames
        p += 1
