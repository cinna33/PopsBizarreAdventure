 # -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 12:24:56 2019

@author: youss
"""
import pygame
#variable utiles pour les algorithmes plus bas qui sont réinitialisé

nP = 0

frameP = 0

pygame.display.init()
width   = pygame.display.Info().current_w  # caractéristiques de la fenêtre
height  = pygame.display.Info().current_h
#ratio qui aide à redimensionner tous les éléments graphiques
#si égal à 1, veut dire que le jeu est dans les dimensions de base c'est à dire 1920*1080    ratiox = width/1920

#coordonnées du texte dans les dialogues
loading = pygame.image.load
frontpops   = []
backpops    = [] 
rightpops   = []
leftpops    = []
for i in range(6):
    fronti = pygame.transform.scale(loading("sprite_walking/front/front{}.png".format(i+1)),(int(91*ratiox),int(237*ratioy)))
    frontpops.append(fronti)
    backi = pygame.transform.scale(loading("sprite_walking/back/back{}.png".format(i+1)),(int(90*ratiox),int(237*ratioy)))
    backpops.append(backi)
    righti = pygame.transform.scale(loading("sprite_walking/right/right{}.png".format(i+1)),(int(79*ratiox),int(237*ratioy)))
    rightpops.append(righti)
    lefti = pygame.transform.scale(loading("sprite_walking/left/left{}.png".format(i+1)),(int(77*ratiox),int(237*ratioy)))
    leftpops.append(lefti)



class Sprite: #Classe pour définir les attributs d'un sprite rapidement
    global ratiox,ratioy
    
    
    def __init__(self, x, y, heightP, widthP, vel, option):
        self.x = x * option.ratiox
        self.y = y * option.ratioy
        self.height = heightP * option.ratioy
        self.width  = widthP * option.ratioy
        self.vel = self.slow = vel * option.ratioy
        self.acc = self.slow + 5 * option.ratioy
        self.front  = True
        self.back  = False
        self.right = False
        self.left  = False
        self.dialogue = False
        self.commande = True
        self.animation = False
        
   
    def walking(self,screen): #frame à l'image quand il marche sur la carte
        global frameP,nP,frontpops,backpops
            
        if self.front:
            #affiche le sprite de face et etc grâce aux valeurs
            #données par la rubriques Commandes dans PopsBizarreAdventure.py
            if nP < 5:
                frameP = 0
            elif nP >= 6 and nP < 11:
                frameP = 1
            elif nP >= 12 and nP < 17:
                frameP = 4
            elif nP >= 18 and nP < 23:
                frameP = 5
                if nP == 22:
                    nP = 0
            nP += 1
                
            screen.blit(frontpops[frameP], (self.x,self.y))
        elif self.right:
            if nP < 5:
                frameP = 0
            elif nP >= 6 and nP < 11:
                frameP = 1
            elif nP >= 12 and nP < 17:
                frameP = 4
            elif nP >= 18 and nP < 23:
                frameP = 5
                if nP == 22:
                    nP = 0
            nP += 1
            screen.blit(rightpops[frameP], (self.x,self.y))
        elif self.back:    
            if nP < 5:
                frameP = 0
            elif nP >= 6 and nP < 11:
                frameP = 1
            elif nP >= 12 and nP < 17:
                frameP = 4
            elif nP >= 18 and nP < 23:
                frameP = 5
                if nP == 22:
                    nP = 0
            nP += 1
            screen.blit(backpops[frameP], (self.x,self.y))
        elif self.left:
            if nP < 5:
                frameP = 0
            elif nP >= 6 and nP < 11:
                frameP = 1
            elif nP >= 12 and nP < 17:
                frameP = 4
            elif nP >= 18 and nP < 23:
                frameP = 5
                if nP == 22:
                    nP = 0
            nP += 1
            screen.blit(leftpops[frameP], (self.x,self.y))    
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

class Event:
    
    def __init__(self):
        self.menu = True
        self.game = False
        self.fadetoblack = False
        self.fadeout = False
    
    def set_menu(self, state):
        self.menu = state
        
    def set_game(self, state):
        self.game = state
    
    def set_fadetoblack(self, state):
        self.fadetoblack = state
    
    def game_get(self):
        return self.game
    
    def menu_get(self):
        return self.menu
    
    def fadetoblack_get(self):
        return self.fadetoblack

class Option:
    
    def __init__(self):
        self.w = 1920
        self.h = 1080
        self.ratiox = 1
        self.ratioy = 1
    # Pour redimensionner la fenêtre
    def dimension(self,width,height):
        self.w = width
        self.h = height
        self.ratiox = int(self.w/1920)
        self.ratioy = int(self.h/1080)
        

    

#Fonction pour faire apparaître les lettres les unes après les autres
