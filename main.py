import os
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


size = width, height = 1200, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
image = load_image("monop.png")
monop = pygame.sprite.Sprite(all_sprites)
monop.image = image
monop.rect = monop.image.get_rect()
monop.rect.x = 50
monop.rect.y = 50
pygame.draw.rect(screen, 'white', (0, 0, 50, 50))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("black"))
    pygame.draw.rect(screen, 'white', (50, 50, 700, 700), 1)
    pygame.draw.rect(screen, 'white', (150, 150, 500, 500), 1)

    pygame.draw.rect(screen, 'white', (650, 650, 100, 100), 1)

    pygame.draw.rect(screen, 'white', (594, 650, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (539, 650, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (482, 650, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (426, 650, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (370, 650, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (314, 650, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (258, 650, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (202, 650, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (150, 650, 52, 100), 1)

    pygame.draw.rect(screen, 'white', (50, 650, 100, 100), 1)

    pygame.draw.rect(screen, 'white', (50, 594, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (50, 539, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (50, 482, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (50, 426, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (50, 370, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (50, 314, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (50, 258, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (50, 202, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (50, 150, 100, 52), 1)

    pygame.draw.rect(screen, 'white', (50, 50, 100, 100), 1)

    pygame.draw.rect(screen, 'white', (150, 50, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (206, 50, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (262, 50, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (318, 50, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (374, 50, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (430, 50, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (486, 50, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (542, 50, 56, 100), 1)
    pygame.draw.rect(screen, 'white', (596, 50, 54, 100), 1)

    pygame.draw.rect(screen, 'white', (650, 50, 100, 100), 1)

    pygame.draw.rect(screen, 'white', (650, 150, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (650, 206, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (650, 262, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (650, 318, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (650, 374, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (650, 430, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (650, 486, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (650, 542, 100, 56), 1)
    pygame.draw.rect(screen, 'white', (650, 596, 100, 54), 1)

    pygame.draw.rect(screen, 'white', (320, 320, 180, 180), 1)
    # all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()

"""1 - (650, 650, 100, 100)
2 - (594, 650, 56, 100)
3 - (539, 650, 56, 100)
4 - (482, 650, 56, 100)
5 - (426, 650, 56, 100)
6 - (370, 650, 56, 100)
7 - (314, 650, 56, 100)
8 - (258, 650, 56, 100)
9 - (202, 650, 56, 100)
10 - (150, 650, 52, 100)
11 - (50, 650, 100, 100)
12 - (50, 594, 100, 56)
13 - (50, 539, 100, 56)
14 - (50, 482, 100, 56)
15 - (50, 426, 100, 56)
16 - (50, 370, 100, 56)
17 - (50, 314, 100, 56)
18 - (50, 258, 100, 56)
19 - (50, 202, 100, 56)
20 - (50, 150, 100, 52)
21 - (50, 50, 100, 100)
22 - (150, 50, 56, 100)
23 - (206, 50, 56, 100)
24 - (262, 50, 56, 100)
25 - (318, 50, 56, 100)
26 - (374, 50, 56, 100)
27 - (430, 50, 56, 100)
28 - (486, 50, 56, 100)
29 - (542, 50, 56, 100)
30 - (596, 50, 54, 100)
31 - (650, 50, 100, 100)
32 - (650, 150, 100, 56)
33 - (650, 206, 100, 56)
34 - (650, 262, 100, 56)
35 - (650, 318, 100, 56)
36 - (650, 374, 100, 56)
37 - (650, 430, 100, 56)
38 - (650, 486, 100, 56)
39 - (650, 542, 100, 56)
40 - (650, 596, 100, 54)
поле для бросания кубиков - (320, 320, 180, 180)
"""
