import pygame
import random
pygame.init()

legpos = 65
headpos = 50
bowlpos = 50

randnum = 0

monkey = pygame.image.load("monkey head.png")
bowls = pygame.image.load("bowls.png")
fallen = pygame.image.load("bowls fallen.png")
BG = pygame.image.load("background1.png")
ant = pygame.image.load("ant eater.png")
ant2 = pygame.image.load("ant eater2.png")
tail = pygame.image.load("tail.png")
#animated legs
legissue = False


legs = pygame.image.load("monkey legs.png")
frameWidth = 96
frameHeight = 96
RowNum = 0 
frameNum = 0
ticker = 0
game = False
scene = 1
timer = 0

fail = False
win = False
move = False
start = False

clock = pygame.time.Clock()

screen = pygame.display.set_mode((750, 750))
#-----------------------------------------------------------------------------------------    
screen.fill((0,0,0))

while scene == 1 and game != True:
    timer += 1
    
    font = pygame.font.Font(None, 30)
    text = font.render("One day Kanaporiwa the bird was flying over the hut of Iwariwa", 1, (90, 90, 90))
    screen.blit(text, (100,100))
    text = font.render("the Cayman when he saw something strange. . .", 1, (90, 90, 90))
    screen.blit(text, (100,130))
    pygame.display.flip()
    
    if timer > 1500:
            
        font = pygame.font.Font(None, 30)
        text = font.render("Iwariwa was bent over a strange orange heat that danced around.", 1, (90, 90, 90))
        screen.blit(text, (100,300))
        text = font.render("On the strange heat were some sweet potatos and when Iwariwa", 1, (90, 90, 90))
        screen.blit(text, (100,330))
        text = font.render("ate them Kanaporiwa could hear him talk about how sweet", 1, (90, 90, 90))
        screen.blit(text, (100,360))
        text = font.render("and tasty they were.", 1, (90, 90, 90))
        screen.blit(text, (100,390))
        pygame.display.flip()
    
    if timer > 3500:
        
        font = pygame.font.Font(None, 30)
        text = font.render("When Iwariwa was done with the heat, Kanaporiwa watched him", 1, (90, 90, 90))
        screen.blit(text, (100,500))
        text = font.render("hide it in a box in his mouth.", 1, (90, 90, 90))
        screen.blit(text, (100,530))
        pygame.display.flip()
        
    if timer > 4000:
        
        font = pygame.font.Font(None, 50)
        text = font.render("Press space to continue", 1, (90, 90, 90))
        screen.blit(text, (150,700))
        pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        scene = 2
    pygame.event.pump()
    
timer = 0
#---------------------------------------------------------------------------------
screen.fill((0,0,0))

while scene == 2 and game != True:
    
    timer += 1
    
    font = pygame.font.Font(None, 30)
    text = font.render("When Kanapori arived at the camp with the other animals he", 1, (90, 90, 90))
    screen.blit(text, (100,100))
    text = font.render("told them what he had seen.", 1, (90, 90, 90))
    screen.blit(text, (100,130))
    pygame.display.flip()
    
    if timer > 1500:
            
        font = pygame.font.Font(None, 30)
        text = font.render("All the animals were mad such a thing was not shared with them.", 1, (90, 90, 90))
        screen.blit(text, (100,300))
        pygame.display.flip()
    
    if timer > 3000:
        
        font = pygame.font.Font(None, 30)
        text = font.render("So they decided to come up with a plan to get the strange heat.", 1, (90, 90, 90))
        screen.blit(text, (100,500))
        text = font.render("from Iwariwa", 1, (90, 90, 90))
        screen.blit(text, (100,530))
        pygame.display.flip()
        
    if timer > 4500:
        
        font = pygame.font.Font(None, 50)
        text = font.render("Press space to continue", 1, (90, 90, 90))
        screen.blit(text, (150,700))
        pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and timer > 500:
        scene = 3
    pygame.event.pump()
    

timer = 0

#------------------------------------------------------------------------------------------------------------------
screen.fill((0,0,0))

while scene == 3 and game != True:
    
    timer += 1
    #fix indentation so all text is on screen - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    font = pygame.font.Font(None, 30)
    text = font.render("Their plan was to host a party that would have a funny talent show ", 1, (90, 90, 90))
    screen.blit(text, (98,100))
    text = font.render("in order to make Iwariwa laugh.", 1, (90, 90, 90))
    screen.blit(text, (98,130))
    pygame.display.flip()
    
    if timer > 1500:
            
        font = pygame.font.Font(None, 30)
        text = font.render("Yarime the monkey and his assistant, Tepe the anteater, came", 1, (90, 90, 90))
        screen.blit(text, (100,300))
        text = font.render("up with an act.", 1, (90, 90, 90))
        screen.blit(text, (100,330))
        pygame.display.flip()
    
    if timer > 3000:
        
        font = pygame.font.Font(None, 30)
        text = font.render("In their act Yarime would walk across the stage while ballencing", 1, (90, 90, 90))
        screen.blit(text, (100,500))
        text = font.render("four bowls of water on his head, then he would trip and cause the", 1, (90, 90, 90))
        screen.blit(text, (100,530))
        text = font.render("bowls of water to fall on Tepe.", 1, (90, 90, 90))
        screen.blit(text, (100,560))
        pygame.display.flip()
        
    if timer > 4500:
        
        font = pygame.font.Font(None, 50)
        text = font.render("Press space to continue", 1, (90, 90, 90))
        screen.blit(text, (200,700))
        pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and timer > 500:
        game = True
    pygame.event.pump()
    
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------


screen = pygame.display.set_mode((1500, 400))


while game == True:
    
    clock.tick(25)

    pygame.display.set_caption("Top text")
    screen.fill((0,0,15))
    keys = pygame.key.get_pressed()
    if fail == False and win == False and legissue == False:
        if keys[pygame.K_LEFT]:
            legpos -= 3
            headpos -= 2
            #bowl stuff
            bowlpos -= 3
            move = True
            start = True
        if keys[pygame.K_RIGHT] and legpos < 1350:
            legpos += 3
            headpos += 2
            move = True
            #bowl stuff
            bowlpos += 3
            start = True
        if keys[pygame.K_a]:
            headpos -= 3
            start = True
        if keys[pygame.K_d]:
            headpos += 3
            start = True
        pygame.event.pump()
        
        if keys[pygame.K_RIGHT] == False and keys[pygame.K_LEFT] == False:
            move = False
    if fail == True or win == True:
        move = False


    #gameplay - - - - - - - - - - - - -
    
    #controls
    #move the bowl
    if start == True:
        if fail == False and win == False and legissue == False:
            if bowlpos+20 > headpos and bowlpos+10 < (headpos + 25):
                randnum = random.randrange(0,3)
                bowlpos -= randnum
                
            if bowlpos+10 > (headpos + 25) and bowlpos < headpos + 45:
                randnum = random.randrange(0,3)
                bowlpos += randnum

        
    #win/lose conditions - - - - - - - - - - - - -
    if bowlpos > 1350:     
        win = True
        
        
    #lose conditions - - - - - - - - -
    if (bowlpos + 10) > (headpos +20):
        if bowlpos > (headpos + 50):
            fail = True
            
    if bowlpos + 10 < headpos + 20:
        if (bowlpos + 20) < headpos:
            fail = True
            
    if headpos > legpos:
        if (headpos - legpos) > 100:
            legissue = True
            
    if legpos > headpos:
        if (legpos - headpos) > 100:
            legissue = True
            
    #render - - - - - - - - -
            
    screen.blit(BG, (0,0))
    screen.blit(BG, (800,0))
    screen.blit(tail, (legpos-55, 275))
    pygame.draw.line(screen, (51, 25, 0), [headpos + 25, 250],[legpos + 10, 340], 10)
    screen.blit(monkey, (headpos-10, 240))
    #bowl
    if win != True and fail != True and legissue != True:
        screen.blit(bowls, (bowlpos-37,145))
        
    pygame.display.flip
    pygame.draw.rect(screen, (71, 40, 2), [1411, 308, 100, 200])
    
    if win == True or fail == True or legissue == True:
        screen.blit(fallen, (bowlpos-37,145))
        
    if win == False:
        screen.blit(ant, (1350,220))
    pygame.display.flip()
    if win == True:
        screen.blit(ant2,(1350,220))


        
    if move == True:
        RowNum = 0
        ticker+=1
        if ticker%5==0: 
          frameNum+=1
        if frameNum>6: 
            frameNum = 0
            
    screen.blit(legs, ((legpos-36), 300), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    
    if start == False:
        font = pygame.font.Font(None, 74)
        text = font.render("controls:", 1, (10, 10, 10))
        screen.blit(text, (200,100))
        font = pygame.font.Font(None, 30)
        text = font.render("To win you must balence the bowls on top of your head and dump them on Tepe at the end of the screen", 1, (10, 10, 10))
        screen.blit(text, (220,150))
        text = font.render("Walk by using the arrow keys and move your head by using A and D.", 1, (10, 10, 10))
        screen.blit(text, (220,180))
        font = pygame.font.Font(None, 74)
        text = font.render("Game Name", 1, (10, 10, 10))
        screen.blit(text, (200,10))
        font = pygame.font.Font(None, 30)
        text = font.render("Based off the Yamonami tale, How Iwariwa the Cayman Learned to Share.", 1, (10, 10, 10))
        screen.blit(text, (220,70))

        
    if win == True:
        font = pygame.font.Font(None, 100)
        text = font.render("You win!", 1, (10, 10, 10))
        screen.blit(text, (220,70))
        pygame.display.flip()
    
    if fail == True:
        font = pygame.font.Font(None, 100)
        text = font.render("You lose!", 1, (10, 10, 10))
        screen.blit(text, (220,70))
        pygame.display.flip()
        
    if legissue == True:
        font = pygame.font.Font(None, 100)
        text = font.render("Your legs and head were too far apart!", 1, (10, 10, 10))
        screen.blit(text, (220,70))
        pygame.display.flip()
        

    pygame.display.flip()
        
'''

'''
    
    

