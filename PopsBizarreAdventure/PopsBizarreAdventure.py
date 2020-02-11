# -*- coding: utf-8 -*-

import pygame
from ressource import Sprite,Event,Option
from animation import animation_text

# définition d'une fonction qui lance le menu principal au lancement du jeu 


# define a main function
def main():
    option = Option()
    width   = option.w  # caractéristiques de la fenêtre
    height  = option.h
    black = pygame.Color(0,0,0) # crée un objet couleur  en ayant référence RGB du noir
    fade  = pygame.Surface((width,height)) 
    fade.fill((0,0,0))
    fade.set_alpha(0)
    white = pygame.Color(255,255,255) # crée un objet couleur  en ayant référence RGB du blanc
    red   = pygame.Color(255,0,0) # de même
    screen  = pygame.display.set_mode((width,height),pygame.RESIZABLE) # pour ouvrir une fenêtre aux dimensions height width
       
    loading = pygame.image.load # pour que ce soit plus rapide pour charger des images  
    
    Pops    = Sprite(350,250,100,200,10) # toutes les caractéristiques de Pops
    
    maps = loading("map.png")
    #redimensionne l'image pour qu'elle soit en conformation avec la taille de la fenêtre
    maps = pygame.transform.scale(maps,(int(1575*option.ratiox),int(941*option.ratioy)))    
    
    
    # initialize the pygame module
    pygame.init()
    # On initialise le son (si jamais)
    pygame.mixer.init()
    # le titre en fenêtre de jeu
    pygame.display.set_caption("Pops' Bizarre Adventure")
    #active le module de texte
    pygame.font.init()
    
    #La police d'écriture du jeu
    font = pygame.font.Font("VCR_OSD_MONO_1.001.ttf",int(30*option.ratiox))   
    # define a variable to control the main loop
    running = True
    # Textes pour tester les boites de dialogues
    text        = "J'aime les carrotes"
    #Objet qui permet de contrôler le nombre de frame et le temps
    clock = pygame.time.Clock()
    starting = Event()
    hitbox_pops = pygame.Rect(Pops.x,Pops.y,97*option.ratiox,327*option.ratioy)
    
    # définiton d'une fonction pour le menu principal au lancement du jeu
    def menu(font):  
        screen.fill(black)
        #remplir le fond de la couleur
        hitbox_lancerjeu = pygame.Rect(800,400,200,50)
        mousepos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        if hitbox_lancerjeu.collidepoint(mousepos[0],mousepos[1]): 
            screen.blit(font.render("Lancer jeu",False,red),(800,400))
            if click:
                starting.set_fadetoblack(True)
                starting.set_menu(False)
                
        else:
            screen.blit(font.render("Lancer jeu",False,white),(800,400))
            
        pygame.display.update()
            
    # définition de la fonction du jeu principal
    def game(key):
        if not Pops.dialogue_get():
            # On remplit le fond par du noir
            screen.fill(black)
            screen.blit(maps,(0,0))
        
        #Commandes
        #Si les commandes sont activées
        if Pops.commande_get():
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
            # puis on affiche le sprite
            Pops.walking(screen)
            hitbox_pops.move(Pops.x, Pops.y)
            # puis on met à jour l'écran
            pygame.display.update(hitbox_pops)
       
        
        # vérifie s'il y un évenement genre appuyer sur une touche
        pygame.event.pump()
        # récupère les évenements dans la queue
        for event in pygame.event.get():
            #si c'est une touche et la touche est z (problème donc pour tester faut appuyer sur w)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                #on active les dialogues
                Pops.set_dialogue(True)
        # si on actives les dialogues
        if Pops.dialogue_get():
            # on active l'animation du texte avec pour paramètre le texte que l'on veut
            animation_text(text,screen,Pops,font)
        #puis on met à jour l'écran
        pygame.display.update()
    
    # def d'une fonction qui permet de faire un fondu en noir
    def fadetoblack(speed):
        nonlocal fade
        if not starting.fadeout:
            screen.blit(font.render("Lancer jeu",False,red),(800,400))
            screen.blit(fade,(0,0))
            
            pygame.display.update()
            # si la valeur alpha du noir est en dessous de 255
            if fade.get_alpha() < 255:
                fade.set_alpha(fade.get_alpha() + speed)
                # on incrémente de 1 alpha
                # si alpha est à son maximum
                if fade.get_alpha() == 255:
                    starting.fadeout = True
                    
                    # on  active le processus inverse
        # si processus inverse activé
        elif starting.fadeout:
            #on baisse alpha
            screen.fill(black)
            screen.blit(maps,(0,0))
            Pops.walking(screen)
            # puis on met à jour l'écran
            screen.blit(fade,(0,0))
            
            pygame.display.update()
            if fade.get_alpha() > 0:
                fade.set_alpha(fade.get_alpha() - speed)
                # si alpha est égale à 0
                if fade.get_alpha() == 0:
                    # on désactive le processus
                    starting.set_fadetoblack(False)
                    starting.set_game(True)
            
    # main loop
    while running:
        
        # Je bloque tous les évenements avec la souris car ils m'ont bien fait chier
        clock.tick_busy_loop(60) # contrôle le nombre de frame du jeu
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
                if Pops.dialogue_get() or starting.fadetoblack_get():
                    # On bloque les commandes
                    Pops.set_commande(False) 
        # si on appuie sur echap
        if key[pygame.K_ESCAPE]:
            # le jeu se ferme
            running = False
        if starting.menu_get():
            menu(font)
         
        elif starting.fadetoblack_get():
            fadetoblack(5)
        
        elif starting.game_get:
            game(key)
        
       
    #quitter pygame donc arrêter le programme
    pygame.quit()            
 
   
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
