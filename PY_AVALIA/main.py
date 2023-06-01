import pygame
pygame.init()
#tela
larg = 1066
alt = 600
fundo = pygame.image.load("universe.jpg")
#display=tela
tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption("SPACE MARKER")
#looping1
on = True
while on:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            on = False

    tela.fill((0, 0, 0))
    tela.blit(fundo,(0,0)) 

    pygame.display.flip()

pygame.quit()