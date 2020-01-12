 # -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 12:24:56 2019

@author: youss
"""
import pygame
i=0
n=0
frame = 0
p = 0
dialogue_x = 50
dialogue_y = 728 
first_x = dialogue_x
first_y = dialogue_y
string = ""
passer = False
finir = False

white = (255,255,255) #référence RGB du blanc
black = (0,0,0)
 	
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.display.init()
pygame.mixer.init()
pygame.mixer
keys = pygame.key.get_pressed()
sfx_dialogue = pygame.mixer.Sound("text.wav")
sfx_dialogue.set_volume(0.2)
loading     = pygame.image.load #pour que ce soit plus rapide pour charger des images  
dialogue_box = loading("dialogue/dialogue_box.png")
curseur = [loading("dialogue/curseur/Sprite-0001.png"),loading("dialogue/curseur/Sprite-0002.png")]

    



class Sprite: #Classe pour définir les attributs d'un sprite rapidement
    
    
    def __init__(self, x, y, heightP, widthP, vel):
        self.x = x
        self.y = y
        self.height = heightP
        self.width  = widthP
        self.vel = self.slow = vel
        self.acc = self.slow + 20
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
    if n%2 == 0:
        screen.blit(dialogue_box,(33,700))
    else:
        screen.blit(dialogue_box,(33,700))
        screen.blit(font.render(string,False,white),(first_x,first_y))
    if sprite.commande:
        sprite.commande = False
        sprite.animation = True
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and not event.key in (pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT):
            if sprite.animation:
                passer = True
            if finir:
                n = 0
                string = ""
                finir = False
                dialogue_x = first_x
                dialogue_y = first_y
                sprite.dialogue = False
                sprite.commande = True
    
    if passer:
        i = font.render(text, False, white)
        screen.blit(i,(first_x,first_y))
        sprite.animation = False  
        passer = False
        finir = True

        
    if sprite.animation:
        if n%2 == 0:
            m = int(n/2)
            j = font.render(string,False,white) 
            string += text[m]
            i = font.render(text[m],False,white)
            screen.blit(j,(first_x,first_y)) 
            screen.blit(i,(dialogue_x,dialogue_y))
            if n%4 == 0:
                sfx_dialogue.play()
            dialogue_x += (font.size(text)[0] / len(text)) 
            pygame.display.update()
        n += 1
    if n == len(text)*2 - 1:
        sprite.animation = False
        n = 0
        finir = True
    if not sprite.animation:
        if p == 59:
            p = 0        
        i = font.render(text, False, white)
        screen.blit(i,(first_x,first_y))
        if p<15 or p >= 30 and p < 45: 
            frame = 0
            screen.blit(curseur[frame],(940,950))
        elif p >= 15 and p < 30 or p >= 45:
            frame = 1
            screen.blit(curseur[frame],(940,950))
        p += 1
