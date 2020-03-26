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
    blue  = pygame.Color(0,0,255)
    green = pygame.Color(0,255,0)
    screen  = pygame.display.set_mode((width,height),pygame.RESIZABLE) # pour ouvrir une fenêtre aux dimensions height width
    
    
    loading = pygame.image.load # pour que ce soit plus rapide pour charger des images  
    
    initialPosX = 700
    initialPosY = 600
    widthPops   = 90
    heightPops  = 201
    velPops     = 5
    
    Pops    = Sprite(initialPosX,initialPosY,widthPops,heightPops,velPops,option) # toutes les caractéristiques de Pops
    
    cameraPosX = Pops.x
    cameraPosY = Pops.y
    VelX = 0
    VelY = 0
   
    frontpops   = []
    backpops    = [] 
    rightpops   = []
    leftpops    = []
    Wfrontpops  = []
    Wrightpops  = []
    Wleftpops   = []
    for i in range(6):
       
        frontpops.append(loading("images/sprite_walking/front/normal/front{}.png".format(i+1)).convert_alpha())
        
        backpops.append(loading("images/sprite_walking/back/back{}.png".format(i+1)).convert_alpha())
        
        rightpops.append(loading("images/sprite_walking/right/normal/right{}.png".format(i+1)).convert_alpha())
        
        leftpops.append(loading("images/sprite_walking/left/normal/left{}.png".format(i+1)).convert_alpha())
        
        Wfrontpops.append(loading("images/sprite_walking/front/wink/front{}.png".format(i+1)).convert_alpha())
    
        Wrightpops.append(loading("images/sprite_walking/right/wink/right{}.png".format(i+1)).convert_alpha())
        
        Wleftpops.append(loading("images/sprite_walking/left/wink/left{}.png".format(i+1)).convert_alpha())
    
    
    maps = loading("images/map.png").convert_alpha()
    dialogue_box = loading("images/dialogue/dialogue_box.png").convert()

    curseur = [loading("images/dialogue/curseur/Sprite-0001.png").convert_alpha(),loading("images/dialogue/curseur/Sprite-0002.png").convert_alpha()]
    
    stageWidth, stageHeight = maps.get_rect().size
    startScrollingX = option.mw
    stagePosX       = 500
    stagePosY       = -150
    initialSPosX = stagePosX
    stageLength  = stageWidth + 2*initialSPosX
    # initialize the pygame module
    pygame.init()
    # On initialise le son (si jamais)
    pygame.mixer.init()
    # le titre en fenêtre de jeu
    pygame.display.set_caption("Pops' Bizarre Adventure")
    #active le module de texte
    pygame.font.init()
    
    #La police d'écriture du jeu
    font = pygame.font.Font("VCR_OSD_MONO_1.001.ttf",30)   
    # define a variable to control the main loop
    running = True
    # Textes pour tester les boites de dialogues
    text        = "J'aime les carrotes"
    #Objet qui permet de contrôler le nombre de frame et le temps
    clock = pygame.time.Clock()
    starting = Event()
    save = {}
    save["paramètres"] = option
    save["joueur"] = Pops
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
   
    # def d'une fonction qui permet de faire un fondu en noir
    def fadetoblack(speed):
        nonlocal fade
        if not starting.fadeout:
            screen.blit(font.render("Lancer jeu",False,red),(800,400))
            screen.blit(fade,(0,0))
            
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
            screen.blit(maps,(stagePosX,stagePosY))
            Pops.walking(screen,cameraPosX,Pops.y,frontpops,backpops,rightpops,leftpops,Wfrontpops,Wrightpops,Wleftpops)
            # puis on met à jour l'écran
            screen.blit(fade,(0,0))
            
            if fade.get_alpha() > 0:
                fade.set_alpha(fade.get_alpha() - speed)
                # si alpha est égale à 0
                if fade.get_alpha() == 0:
                    # on désactive le processus
                    starting.set_fadetoblack(False)
                    starting.set_game(True)     
        pygame.display.update()
        
    # définition de la fonction du jeu principal
    def game(key):
        global cameraPosX, velX, velY
        nonlocal stagePosX
        #Commandes
        #Si les commandes sont activées
        if Pops.commande_get():
            #Gauche    
            if key[pygame.K_LEFT] and Pops.x - Pops.width/2 > stagePosX:
                Pops.x -= Pops.speed
                Pops.set_left()  # permet de figer le perso dans la dernière pose qu'il faisait
                # Si jamais d'autres touches sont pressées
                 #Bas
                if key[pygame.K_DOWN] and Pops.y + Pops.height < stagePosY + stageHeight:
                    Pops.y += Pops.speed
                    Pops.set_front()
              
                #Haut
                elif key[pygame.K_UP] and Pops.y>0:
                    Pops.y -= Pops.speed
                    Pops.set_back()
            #Droite    
            elif key[pygame.K_RIGHT] and Pops.x < stageLength - initialSPosX - (Pops.width + Pops.width/2):
                Pops.x += Pops.speed
                Pops.set_right()  # Aussi
                if key[pygame.K_DOWN] and Pops.y + Pops.height < stagePosY + stageHeight:
                    Pops.y += Pops.speed
                    Pops.set_front()
              
                #Haut
                elif key[pygame.K_UP] and Pops.y>0:
                    Pops.y -= Pops.speed
                    Pops.set_back()
            #Bas
            elif key[pygame.K_DOWN] and Pops.y + Pops.height < stagePosY + stageHeight:
                Pops.y += Pops.speed
                Pops.set_front()
              
            #Haut
            elif key[pygame.K_UP] and Pops.y>0:
                Pops.y -= Pops.speed
                Pops.set_back()
       
            if Pops.x < startScrollingX:
                cameraPosX = Pops.x
            
            elif Pops.x > stageLength - startScrollingX:
                cameraPosX = Pops.x - stageLength + option.w
            #Scrolling
            elif Pops.x >= startScrollingX:
                cameraPosX = startScrollingX
                if key[pygame.K_LEFT]:
                    velX = -Pops.speed
                elif key[pygame.K_RIGHT]:
                    velX = Pops.speed
                else:
                    velX = 0
                stagePosX -= velX
            
        # puis on affiche le sprite
        screen.fill(black)
        screen.blit(maps,(stagePosX, stagePosY))
        Pops.walking(screen,cameraPosX,Pops.y,frontpops,backpops,rightpops,leftpops,Wfrontpops,Wrightpops,Wleftpops)
     
    
        # vérifie s'il y un évenement genre appuyer sur une touche
            
        # si on actives les dialogues
        if Pops.dialogue_get():
            # on active l'animation du texte avec pour paramètre le texte que l'on veut
                animation_text(text,screen,Pops,font,dialogue_box,curseur,maps,stagePosX,stagePosY)
        #puis on met à jour l'écran
        pygame.display.update()
            
    # main loop
    while running:
        
        # Je bloque tous les évenements avec la souris car ils m'ont bien fait chier
        clock.tick_busy_loop(60) # contrôle le nombre de frame du jeu
         # On associe keys pour gérer les touches plus efficacement
        key = pygame.key.get_pressed()
        
        # event handling, gets all event from the event queue
        pygame.event.pump()
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # Si une touche est pressée ...
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11: 
                    screen = option.dimension(screen)
                # Si c'est pendant un dialogue :
                if Pops.dialogue_get() or starting.fadetoblack_get():
                    # On bloque les commandes
                    Pops.set_commande(False) 
                if event.key == pygame.K_SPACE:
                #on active les dialogues45
                    Pops.set_dialogue(True)
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
        
    pygame.quit()            
 
   
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
