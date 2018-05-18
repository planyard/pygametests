import pygame

pygame.init()
window = pygame.display.set_mode((500, 400))

while True:
    #WHERE TO DRAW, COLOR, X AND Y TUPLE START, X AND Y TUPLE END, LINE WIDTH
    pygame.draw.line(window, (255,255,255), (0, 0), (500, 400), 1)
    pygame.display.update()