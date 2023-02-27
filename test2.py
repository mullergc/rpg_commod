import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('teste')

sprite_sheet_image = pygame.image.load('images/bedhosp.png').convert_alpha()

BG = (50,50,50)

run = True
while run:
  #update background
  screen.fill(BG)

  #display image
  screen.blit(sprite_sheet_image,(0,0))

  # event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  pygame.display.update()

pygame.quit()