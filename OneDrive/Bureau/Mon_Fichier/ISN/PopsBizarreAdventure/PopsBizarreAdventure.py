# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:55:24 2019

@author: youss
"""

import pygame
from ressource import Sprite,animation_text
#Petit disclaimer : le jeu doit être pensé pour fonctionner à chaque frame
#Par exemple, ne faites pas de boucles for pour faire une action plusieurs fois
#comme on a pu le faire dans le Mini-projet avec turtle
#Cela paralyse le fonctionnement du jeu
#Préférez créer une liste puis son indice qui augmente à chaque frame 

# define a main function
def main():
    width   = 1920 # caractéristiques de la fenêtre
    height  = 1080
    black = (0,0,0) # référence RGB du noir
    white = (255,255,255) # référence RGB du blanc
    screen  = pygame.display.set_mode((width,height),pygame.RESIZABLE) # pour ouvrir une fenêtre aux dimensions height width
       
    loading = pygame.image.load # pour que ce soit plus rapide pour charger des images  
    
    Pops    = Sprite(350,250,100,200,5) # toutes les caractéristiques de Pops (cf ressource.py)
    
    # initialize the pygame module
    pygame.init()
    # On initialise le son (si jamais)
    pygame.mixer.init()
    # le titre en fenêtre de jeu
    pygame.display.set_caption("Pops' Bizarre Adventure")
    #on lance le module qui gère les textes
    pygame.font.init()
    
    #La police d'écriture du jeu
    font = pygame.font.Font("VCR_OSD_MONO_1.001.ttf",26)   
    # define a variable to control the main loop
    running = True
    # définit si le jeu est en plein écran ou pas 
    fullscreen = False
    # Textes pour tester les boites de dialogues
    text        = "Je vais t'éventrer comme je le fais à des bébés tous les samedis soirs lol"
    anothertext = "Une autre ligne"
    #Objet qui permet de contrôler le nombre de frame et le temps
    clock = pygame.time.Clock()
    # main loop
    while running:
        # Je bloque tous les évenements avec la souris car ils m'ont bien fait chier
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        clock.tick(60) # contrôle le nombre de frame du jeu
         # On associe keys pour gérer les touches plus efficacement
        key = pygame.key.get_pressed()
        
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # Si une touche est pressée ...
            elif event.type == pygame.KEYDOWN:
                # Si c'est pendant un dialogue :
                if Pops.dialogue:
                    # On bloque les commandes
                    Pops.commande_set(False) 
       
        # On remplit le fond par du noir
        screen.fill(black)
        
        #Commandes
        if Pops.commande:
            #Shift
            if key[pygame.K_LSHIFT] and Pops.vel<Pops.acc :
                Pops.vel += Pops.acc
            elif not key[pygame.K_LSHIFT]:
                    Pops.vel = Pops.slow
            #Gauche    
            if key[pygame.K_LEFT] and Pops.x>0:
                Pops.x -= Pops.vel
                Pops.set_left()  # permet de figer le perso dans la dernière pose qu'il faisait
                # Si jamais d'autres touches sont pressées
                if key[pygame.K_UP] and Pops.y>0:
                    Pops.x -= Pops.vel/2
                    Pops.y -= Pops.vel/2
                    Pops.set_back()
                elif key[pygame.K_DOWN] and Pops.y<height-Pops.height:
                   Pops.x -= Pops.vel/2
                   Pops.y += Pops.vel/2
                   Pops.set_front()  
                    
            #Droite    
            elif key[pygame.K_RIGHT] and Pops.x<width-Pops.width:
                Pops.x += Pops.vel
                Pops.set_right()  # Aussi
                if key[pygame.K_UP] and Pops.y>0:
                    Pops.x += Pops.vel/2
                    Pops.y -= Pops.vel/2
                    Pops.set_back()
                elif key[pygame.K_DOWN] and Pops.y<height-Pops.height:
                    Pops.x += Pops.vel/2
                    Pops.y += Pops.vel/2
                    Pops.set_front()
            #Bas
            elif key[pygame.K_DOWN] and Pops.y<height-Pops.height:
                Pops.y += Pops.vel
                Pops.set_front()
              
            #Haut
            elif key[pygame.K_UP] and Pops.y>0:
                Pops.y -= Pops.vel
                Pops.set_back()
        
            #Si on appuie sur echap       
            if key[pygame.K_ESCAPE]:
                #Le programme se ferme
                running = False
                
            #On appelle la méthode qui permet d'afficher le sprite
            Pops.walking(screen)
            #Puis on met à jour à l'écran qui affichera tout à l'écran
            pygame.display.update()
        # Le programme recherche si un évenement s'est produit par exemple appuyer sur une touche
        # Sans ça le programme pourrait penser qu'il a planté donc arrêter de fonctionner
        pygame.event.pump()
        # Si il y a un évenement :
        for event in pygame.event.get():
            #Si cet évenment est une touche et que c'est z : 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                #On active les dialogues
                Pops.dialogue = True
        #Si les dialogues sont activés
        if Pops.dialogue:
            #On appelle la fonction qui affiche les textes avec en paramètre le texte qu'on veut afficher
            animation_text(text,screen,Pops)
        #Puis on met à jour l'écran une dernière fois pour s'assurer    
        pygame.display.update()
    pygame.quit()            
 
   
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
