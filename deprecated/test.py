import pygame, sys
pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.draw.rect(screen, (255,255,255), (400, 400, 20, 20),0)
screen.fill((255,255,255))

pygame.display.update()


# waint until user quits
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()