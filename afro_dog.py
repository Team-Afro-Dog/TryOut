import pygame

SIZE = [250,250]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

def afro():
    
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    pygame.display.set_caption("Team Afro Dog")

    done = False

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    font1 = pygame.font.Font(None, 72)
    font3 = pygame.font.Font(None, 14)
    font4 = pygame.font.Font(None, 20)

    

    count = 0
    while not done:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                done = True
        if count == 0:
            screen.fill(WHITE)
        elif count  == 1:
            screen.fill(BLUE)
        elif count  == 2:
            screen.fill(GREEN)
        elif count == 3:
            screen.fill(BLACK)
        elif count == 4:
            screen.fill(RED)
        if count == 4:
            count = 0
            
        text = font1.render("TEAM", True, GREEN)
        screen.blit(text, [10, 20])

        text = font1.render("AFRO", True, RED)
        screen.blit(text, [30, 60])

        text = font1.render("DOG", True, BLACK)
        screen.blit(text, [50, 100])


        count += 1
                
        clock.tick(60)
        pygame.display.flip()
    
    










afro()
