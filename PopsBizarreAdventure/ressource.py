# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 12:24:56 2019

@author: youss
"""
import pygame
#variable utiles pour les algorithmes plus bas qui sont réinitialisé
class Option:
    
    def __init__(self):
        self.w  = 1920
        self.h  = 1080
        self.mw = int(self.w/2)
        self.mh = int(self.h/2)
    # Pour redimensionner la fenêtre
    def dimension(self,screen):
        if screen == pygame.display.set_mode((self.w,self.h),pygame.RESIZABLE):
            screen = pygame.display.set_mode((self.w,self.h),pygame.FULLSCREEN)
        
        elif screen == pygame.display.set_mode((self.w,self.h),pygame.FULLSCREEN):
            screen = pygame.display.set_mode((self.w,self.h),pygame.RESIZABLE)
        
        return screen
option = Option()

nP = 0

frameP = 0

pygame.display.init()

#ratio qui aide à redimensionner tous les éléments graphiques
#si égal à 1, veut dire que le jeu est dans les dimensions de base c'est à dire 1920*1080    ratiox = width/1920

#coordonnées du texte dans les dialogues
loading = pygame.image.load

class Sprite: #Classe pour définir les attributs d'un sprite rapidement
    global option
    
    
    def __init__(self, x, y, widthP, heightP, speed, option):
        self.x = x
        self.y = y 
        self.width = widthP 
        self.height  = heightP 
        self.speed = speed 
        self.front  = True
        self.back  = False
        self.right = False
        self.left  = False
        self.dialogue = False
        self.commande = True
        self.animation = False
        
   
    def walking(self,screen,positionX,positionY,frontpops,backpops,rightpops,leftpops,Wfrontpops,Wrightpops,Wleftpops): #frame à l'image quand il marche sur la carte
        global frameP,nP
            
       
            #affiche le sprite de face et etc grâce aux valeurs
            #données par la rubriques Commandes dans PopsBizarreAdventure.py
            
        nP = nP % 208 # toutes les 208 frames
            
        if nP%52 < 11:
            frameP = 0
        elif nP%52 >= 12 and nP%52 < 23:
            frameP = 1
        elif nP%52 >= 24 and nP%52 < 29:
            frameP = 2
        elif nP%52 >= 30 and nP%52 < 35:
            frameP = 3
        elif nP%52 >= 36 and nP%52 < 41:
            frameP = 4
        elif nP%52 >= 42 and nP%52 < 53:
            frameP = 5
        nP += 1
        
        if self.front:
            if nP <= 156:
                screen.blit(frontpops[frameP], (positionX,positionY))
            else:
                screen.blit(Wfrontpops[frameP], (positionX,positionY))
            
        elif self.right:
            if nP <= 156:
                screen.blit(rightpops[frameP], (positionX,positionY))
            else:
                screen.blit(Wrightpops[frameP], (positionX,positionY))
            
        elif self.back:    
            screen.blit(backpops[frameP], (positionX,positionY))
        
        elif self.left:
            if nP <= 156:
                screen.blit(leftpops[frameP], (positionX,positionY)) 
            else:
                screen.blit(Wleftpops[frameP], (positionX,positionY))
                if nP == 208:
                    nP = 0
        
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

        

    

#Fonction pour faire apparaître les lettres les unes après les autres
