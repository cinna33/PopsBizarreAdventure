import pygame 
pygame.init() 

#premiere classe pour le joueur 
class Player(pygame.sprite.Sprite): 

    def __init__(self): 
        super().__init__() 
        self.health = 100 
        self.max_health = 100 
        self.velocity = 10
        self.image = pygame.image.load("test.gif") 
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.jumping = False 
    

    def move_right(self): 
        self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity
    def move_down(self):
        self.rect.y += self.velocity 
    def move_up(self): 
        self.rect.y -= self.velocity 
  
    


#seconde classe pour le jeux 
class Game: 
    def __init__(self): 
        #générer notre joueur 
        self.player = Player()
        self.pressed = {}

window_resolution = (1350,700)  #pour afficher en plein écran 
CLOCK = pygame.time.Clock() 
FPS = 120

pygame.display.set_caption("Mario 2D")
window_surface = pygame.display.set_mode(window_resolution)

fond_image = pygame.image.load("frame1.png")
fond_image2 = pygame.image.load("frame2.png") 
fond_image.convert() 


#charger notre jeux 
game = Game() 



x = 0 



launched = True 
while launched: 
    
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            launched = False 
        #detecter si un joueur appuie sur une touche du clavier 
        elif event.type == pygame.KEYDOWN: 
           game.pressed[event.key] = True 
        elif event.type == pygame.KEYUP: 
            game.pressed[event.key] = False 
            
#scrolling horizontal 
    rel_x = x % fond_image.get_rect().width 
    window_surface.blit(fond_image, (rel_x - fond_image.get_rect().width, 0)) 
    if rel_x < 1300: 
        window_surface.blit(fond_image2, (rel_x, 0)) 
    x -= 1
    pygame.display.update()
    CLOCK.tick(FPS) 
    
    
    
    
    
    
    
    
    
    
          
    #appliquer l'image de mon joueur 
    window_surface.blit(game.player.image, game.player.rect) #l'image se positionne par rapport à rect 


    #verifier si le joueur souhaite aller à gauche ou à droite, en haut ou en bas 
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x <1280: #le joueur va pas au delà de 700px 
        game.player.move_right() 
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x >0: 
        game.player.move_left() 
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y >0:
        game.player.move_down()
    elif game.pressed.get(pygame.K_UP) and game.player.rect.y >0: 
        game.player.move_up()
    

    pygame.display.flip() 


