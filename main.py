import os
import pygame
import random
pygame.init()
main_dict = {1:(650, 650, 100, 100),
40:(594, 650, 56, 100),
39:(539, 650, 56, 100),
38:(482, 650, 56, 100),
37:(426, 650, 56, 100),
36:(370, 650, 56, 100),
35:(314, 650, 56, 100),
34:(258, 650, 56, 100),
33:(202, 650, 56, 100),
32:(150, 650, 52, 100),
31:(50, 650, 100, 100),
30:(50, 594, 100, 56),
29:(50, 539, 100, 56),
28:(50, 482, 100, 56),
27:(50, 426, 100, 56),
26:(50, 370, 100, 56),
25:(50, 314, 100, 56),
24:(50, 258, 100, 56),
23:(50, 202, 100, 56),
22:(50, 150, 100, 52),
21:(50, 50, 100, 100),
20:(150, 50, 56, 100),
19:(206, 50, 56, 100),
18:(262, 50, 56, 100),
17:(318, 50, 56, 100),
16:(374, 50, 56, 100),
15:(430, 50, 56, 100),
14:(486, 50, 56, 100),
13:(542, 50, 56, 100),
12:(596, 50, 54, 100),
11:(650, 50, 100, 100),
10:(650, 150, 100, 56),
9:(650, 206, 100, 56),
8:(650, 262, 100, 56),
7:(650, 318, 100, 56),
6:(650, 374, 100, 56),
5:(650, 430, 100, 56),
4:(650, 486, 100, 56),
3:(650, 542, 100, 56),
2:(650, 596, 100, 54),
'main':(320, 320, 180, 180)
}

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
chiper = load_image('fishka.png')
monop = pygame.sprite.Sprite(all_sprites)
chip = pygame.sprite.Sprite(all_sprites)
monop.image = image
chip.image = chiper
monop.rect = monop.image.get_rect()
chip.rect = chip.image.get_rect()
monop.rect.x = 50
monop.rect.y = 50
chip.rect.x = main_dict[1][0] + main_dict[1][2]
chip.rect.y = main_dict[1][1] + main_dict[1][3]
pygame.draw.rect(screen, 'white', (0, 0, 50, 50))
screen.fill(pygame.Color("black"))
running = True
cordinate_chip = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 500 > event.pos[0] > 320 and 500 > event.pos[1] > 320:
                screen.fill(pygame.Color("black"))
                num = (random.randint(1,6),random.randint(1,6))
                if sum(num) + cordinate_chip > 40:
                    cordinate_chip = cordinate_chip - 40
                chip.rect.x = main_dict[cordinate_chip + sum(num)][1]
                chip.rect.y = main_dict[cordinate_chip + sum(num)][0]
                cordinate_chip += sum(num)
                f1 = pygame.font.Font(None, 50)
                if sum(num) <= 4:
                    text1 = f1.render(f'Выпало {sum(num)} хода', True, (0, 255, 0))
                else:
                    text1 = f1.render(f'Выпало {sum(num)} ходов', True, (0, 255, 0))
                screen.blit(text1, (800, 100))
                
        
    all_sprites.draw(screen)
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
    pygame.display.flip()
pygame.quit()

