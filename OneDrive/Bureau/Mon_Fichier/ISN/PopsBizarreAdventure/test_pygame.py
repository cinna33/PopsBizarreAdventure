# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:55:24 2019

@author: youss
"""

import pygame

frame = 0
width   = 1920 #caractéristiques de la fenêtre
height  = 1080
widthP  = 50 #caractéristique du joueur
heightP = 50
 
loading     = pygame.image.load #pour que ce soit plus rapide pour charger des images
screen      = pygame.display.set_mode((width,height)) #pour ouvrir une fenêtre aux dimensions height width
sprite_pops = [] #Je crée une liste vide
for i in range(24):
    sprite_pops.append(loading('sprite_face_discu_pops/{}.png'.format(i))) #pour compiler toutes les images dans sprite pops sans le faire à la main
    

    
# define a main function
def main():
    x = 0
    y = 0
    def sprite_discu(): #frame à l'image
        global frame
        screen.fill((0,0,0))
        screen.blit(sprite_pops[frame], (x,y))
        frame += 1
        if frame == 23:
            frame = 0
        pygame.display.update()
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("J'aime les bites")
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
       
        vel = slow = 5
        acc = 20
        pygame.time.delay(100) #L'holorge je crois
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LSHIFT] and vel<50 :
            vel += acc
        elif not keys[pygame.K_LSHIFT]:
            vel = slow 
        if keys[pygame.K_LEFT] and x>0:
            x -= vel
        elif keys[pygame.K_RIGHT] and x<width-widthP:
            x += vel
        elif keys[pygame.K_DOWN] and y<height-heightP:
            y += vel
        elif keys[pygame.K_UP] and y>0:
            y -= vel
        sprite_discu()
        pygame.display.update()
    pygame.quit()            
     
   
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()