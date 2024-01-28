import pygame

pygame.init()

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width,screen_height))


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update()
pygame.quit()
            