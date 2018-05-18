import pygame

pygame.init()

#WIDTH ALWAYS COMES BEFORE HEIGHT
window = pygame.display.set_mode((500, 400))

#WILL NEVER FINISH BECAUSE TRUE IS ALWAYS TRUE. KEEPS PROGRAM RUNNING AS LONG AS WE LIKE
while True:
    #In order: 'draw on window', 'set rgb colors', 
    #'set [from the left of the viewport] width, height, shape width, shape height
    #pygame.draw.rect(window, (255, 0, 0), (0, 0, 50, 50))
    #pygame.draw.rect(window, (0, 255, 0), (50, 0, 50, 50))
    #pygame.draw.rect(window, (0, 0, 255), (100, 0, 50, 50))

    pygame.draw.rect(window, (255, 0, 0), (100, 100, 100, 50), 2)
    pygame.draw.ellipse(window, (255, 0, 0), (100, 100, 100, 50))

    pygame.draw.rect(window, (0, 255, 0), (100, 150, 80, 40), 2)
    #Inc. inner width (2) - without a width defined, this defaults to 0 and fills the shape
    pygame.draw.ellipse(window, (0, 255, 0), (100, 150, 80, 40), 2)

    pygame.draw.rect(window, (0, 0, 255), (100, 190, 60, 30), 2)
    pygame.draw.ellipse(window, (0, 0, 255), (100, 190, 60, 30))

    #Circle - if the width and height parameters are the same, this is a circle
    pygame.draw.ellipse(window, (0, 255, 0), (100, 250, 40, 40))
    #WHERE TO DRAW, (RED, GREEN, BLUE), (X COORDINATE, Y COORDINATE), RADIUS, HEIGHT, WIDTH)
    #pygame.draw.circle(window, (255, 255, 0), (250, 200), 20, 0)

    pygame.display.update()