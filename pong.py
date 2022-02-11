import pygame
from playsound import playsound
pygame.init()
pygame.mixer.init

doExit = False
clock = pygame.time.Clock()
p1x = 20
p1y = 200
p2y = 300
p2x = 660
imposter = 0

sus = 350
by = 250
bVx = 5
bVy = 5

p1Score = 0
p2Score = 0
#this will break the program if you dont have a sound file named this in the directory(original sound is the taco bell dong)
score1 = pygame.mixer.Sound("bell.mp3")

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("computer tenis")


while imposter == 0:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExir = True
    #logic - - - -
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1y-=5
    if keys[pygame.K_s]:
        p1y+=5
    if keys[pygame.K_i]:
        p2y-=5
    if keys[pygame.K_k]:
        p2y+=5
    
    #move the ball
    sus += bVx
    by += bVy
    
    #bounce ball against walls
    if sus < 0 or sus + 20 > 700:
        bVx *= -1
    if by < 0 or by + 20 > 500:
        bVy *= -1
    
    #bounce ball off paddles
    if sus < p1x + 20 and by + 20 > p1y and by < p1y + 100:
        bVx *= -1
        
    if sus+20 > p2x and by + 20 < p2y and by > p2y - 100:
        bVx *= -1
    #following 2 statements use an audeo file
    if sus < 0:
        p2Score += 1
        score1.play()
    if sus > 680:
        p1Score += 1
        score1.play()
    #render - - - -
            
    screen.fill((0,0,15))
    pygame.draw.line(screen, (190,255,255), [349,0], [349,500],5)
    
    pygame.draw.rect(screen, (190, 255, 255), (p1x, p1y, 20, 100), 150)
    pygame.draw.rect(screen, (205, 255, 255), (p2x, (p2y-100), 20, 100), 150)
    pygame.draw.rect(screen, (205, 255, 255), (sus, by, 20, 20), 150)

    font = pygame.font.Font(None, 74)
    text = font.render(str(p1Score), 1, (150, 255, 255))
    screen.blit(text, (250,10))
    text = font.render(str(p2Score), 1, (150,255,255))
    screen.blit(text, (420,10))

    pygame.display.flip()  
pygame.quit()