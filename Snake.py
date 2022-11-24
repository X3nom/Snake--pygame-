from operator import truediv
import pygame,sys,random,time

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

head = pygame.transform.scale(pygame.image.load(r"C:\Users\Jakub\Programming\Python\pygame\Snake\textures\snake\head1.png"),(40,40))
head_eating = pygame.transform.scale(pygame.image.load(r"C:\Users\Jakub\Programming\Python\pygame\Snake\textures\snake\head2.png"),(40,40))
body1 = pygame.transform.scale(pygame.image.load(r"C:\Users\Jakub\Programming\Python\pygame\Snake\textures\snake\body1.png"),(40,40))
body2 = pygame.transform.scale(pygame.image.load(r"C:\Users\Jakub\Programming\Python\pygame\Snake\textures\snake\body2.png"),(40,40))
grass = pygame.transform.scale(pygame.image.load(r"C:\Users\Jakub\Programming\Python\pygame\Snake\textures\terrain\grass.png"),(40,40))
barricade = pygame.transform.scale(pygame.image.load(r"C:\Users\Jakub\Programming\Python\pygame\Snake\textures\terrain\barricade.png"),(40,40))
apple = pygame.transform.scale(pygame.image.load(r"C:\Users\Jakub\Programming\Python\pygame\Snake\textures\pickups\apple.png"),(40,40))
menu_BG = pygame.image.load(r"C:\Users\Jakub\Programming\Python\pygame\Snake\textures\Menu\death BG.png")

font = pygame.font.SysFont("Small Fonts",30)
died = False
w = False
a = False
s = False
d = False

while True: # menu loop
    in_menu = True
    if died == True:
        screen.blit(menu_BG,(0,0))
    while died == True:
        screen.blit(pygame.transform.scale(font.render("YOU DIED",False,(255,10,10)),(300,200)),(200,0))
        screen.blit(font.render(f"Score: {len(body_pos)-1}",False,(255,255,255)),(50,300))
        screen.blit(font.render("Press <SPACE> to continue",False,(255,255,255)),(50,750))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        died = False
        pygame.display.update()
    for x in range(800): #BG generation
            for y in range(800):
                if x % 40 == 0 and y % 40 == 0:
                    screen.blit(grass,(x,y))
    screen.blit(menu_BG,(0,0))
    screen.blit(pygame.transform.scale(font.render("SNAKE",False,(255,255,255)),(500,300)),(130,30))
    while in_menu:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        in_menu = False
        pygame.display.update()
        


    direction = [0,-1]
    direction_lock = direction
    head_pos = [360,360]
    body_pos = [head_pos]
    head_rotation = 0
    event_clock = 0
    apple_pos = [random.randint(0,19)*40,random.randint(0,19)*40]
    died = False
    border_kill = True
    speed = 6
    difficulty = 0

    while died == False: #                     >>> Game Loop <<<
        for x in range(800): #BG generation
            for y in range(800):
                if x % 40 == 0 and y % 40 == 0:
                    screen.blit(grass,(x,y))
        #--------------------------------------------------        
        event_clock += 1
        if event_clock == speed:
            event_clock = 0
            if head_pos == apple_pos:
                body_pos.insert(0,head_pos)
                #moves apple, checks if it doesnt colide            
                intersects = True
                while intersects == True:
                    intersects = False
                    apple_pos = [random.randint(0,19)*40,random.randint(0,19)*40]
                    for part in body_pos:
                        if part == apple_pos:
                            intersects = True
                    if apple_pos == head_pos:
                        intersects = True
            else:
                for i in range(len(body_pos)):
                    if i+1 < len(body_pos):
                        body_pos[len(body_pos)-i-1] = body_pos[len(body_pos)-i-2]
                    else:
                        body_pos[0] = head_pos
            
            head_pos = [x + y*40 for (x, y) in zip(head_pos, direction)]
            direction_lock = direction
            
            #head = pygame.transform.rotate(head,)
            

            #checks if colided with body
            for part in body_pos:
                if head_pos == part:
                    died = True
            #border collision
            if head_pos[0] < 0:
                if border_kill == True:
                    died = True
                else:
                    head_pos[0] = 760
            if head_pos[0] > 760:
                if border_kill == True:
                    died = True
                else:
                    head_pos[0] = 0
            if head_pos[1] < 0:
                if border_kill == True:
                    died = True
                else:
                    head_pos[1] = 760
            if head_pos[1] > 760:
                if border_kill == True:
                    died = True
                else:
                    head_pos[1] = 0
                
        #--Graphics------------------------------------------------
        screen.blit(apple,apple_pos)
        for part in body_pos:
            screen.blit(body1,part)
        screen.blit(head,head_pos)
        screen.blit(font.render("score:{}".format(len(body_pos)-1),False,(255,255,255)),(0,0))
        
        #---Inputs-----------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and direction_lock != [0,1]:
                    direction = [0,-1]
                    w = True
                if event.key == pygame.K_s and direction_lock != [0,-1]:
                    direction = [0,1]
                    s = True
                if event.key == pygame.K_a and direction_lock != [1,0]:
                    direction = [-1,0]
                    a = True
                if event.key == pygame.K_d and direction_lock != [-1,0]:
                    direction = [1,0]
                    d = True
        
        
        pygame.display.update()
        clock.tick(60)