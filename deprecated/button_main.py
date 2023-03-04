import pygame
import button

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button images
start_img = pygame.image.load('../images/button_resume.png').convert_alpha()
exit_img = pygame.image.load('../images/button_quit.png').convert_alpha()
easy_img = pygame.image.load('../images/easy_button.png').convert_alpha()
normal_img = pygame.image.load('../images/normal_button.png').convert_alpha()
hard_img = pygame.image.load('../images/hard_button.png').convert_alpha()

#create button instances
start_button = button.Button(200, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)
easy_button = button.Button(100, 200, easy_img, 0.8)
normal_button = button.Button(300, 200, normal_img, 0.8)
hard_button = button.Button(450, 200, hard_img, 0.8)

#game loop
run = True
while run:

	screen.fill((202, 228, 241))

	if start_button.draw(screen):
		print('START')

	if exit_button.draw(screen):
		print('EXIT')

	#event handler
	for event in pygame.event.get():
		#easy_button.draw(screen)
		#normal_button.draw(screen)
		#hard_button.draw(screen)

		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()