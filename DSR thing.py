import pygame
import random
pygame.init()

legpos = 65
headpos = 50
bowlpos = 50

randnum = 0

monkey = pygame.image.load("monkey head.png")

fail = False

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1500, 500))

while fail == False:
    
    clock.tick(30)
    
    pygame.display.set_caption("Top text")
    screen.fill((0,0,15))
    if fail == False:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            legpos -= 3
            headpos -= 2
            #bowl stuff
            bowlpos -= 3
        if keys[pygame.K_RIGHT]:
            legpos += 3
            headpos += 2
            #bowl stuff
            bowlpos += 3
        if keys[pygame.K_a]:
            headpos -= 3
        if keys[pygame.K_d]:
            headpos += 3
        pygame.event.pump()
    

    #gameplay - - - - - - - - - - - - -
    
    #move the bowl
    if bowlpos+20 > headpos and bowlpos+10 < (headpos + 25):
        randnum = random.randrange(0,3)
        bowlpos -= randnum
        
    if bowlpos+10 > (headpos + 25) and bowlpos < headpos + 45:
        randnum = random.randrange(0,3)
        bowlpos += randnum

        
    #win/lose conditions - - - - - - - - - - - - -
    if bowlpos > 1450:     
        print("you win!")
        fail = True
        
    #lose conditions - - - - - - - - -
    if (bowlpos + 10) > (headpos +25):
        if bowlpos > (headpos + 50):
            print("You lose!")
            fail = True
            
    if bowlpos + 10 < headpos + 25:
        if (bowlpos + 20) < headpos:
            print("You lose!")
            fail = True
            
    if headpos > legpos:
        if (headpos - legpos) > 150:
            print("your legs and head were too far apart!")
            fail = True
            
    if legpos > headpos:
        if (legpos - headpos) > 150:
            print("your legs and head were too far apart!")
            fail = True
            
    #render - - - - - - - - -
            
    pygame.draw.rect(screen, (159, 97, 50), (legpos, 450, 20, 20), 150)
    pygame.draw.line(screen, (179, 117, 70), [headpos + 25, 360],[legpos + 10, 450], 10)
    screen.blit(monkey, (headpos-10, 340))
    #bowl
    pygame.draw.rect(screen, (15, 5, 150), (bowlpos, 250, 20, 100), 150)
    
    pygame.display.flip()
        
'''

'''
    
    

