import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode([626, 391])
pygame.display.set_caption("Russian_substance")

bg = pygame.image.load('Images/bg.jpg')
bg2 = pygame.image.load('Images/bg2.jpg')
bro1 = pygame.image.load('Images/bro1.png')
bro2 = pygame.image.load('Images/bro2.png')
bro3 = pygame.image.load('Images/bro3.png')
bro4 = pygame.image.load('Images/bro4.png')
bro = [bro1, bro2, bro3, bro4]
bro_i = 0
x = 0
h_x = 10
h_y = 280

run = True
while run:

    screen.blit(bg,(x,0))
    screen.blit(bg2, (x+626, 0))
    x = x-5
    dt = clock.tick(60) / 1000
    if x < -626:
        x = 0

    screen.blit(bro[bro_i],(h_x, h_y))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        h_y-=1
    if keys[pygame.K_s]:
        h_y+=1
    if keys[pygame.K_a]:
        h_x-=1
    if keys[pygame.K_d]:
        h_x +=1
        bro_i +=1
        if bro_i == 4:
            bro_i = 0
    else:
        bro_i = 0







    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

