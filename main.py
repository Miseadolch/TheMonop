import os
import pygame
import random

pygame.init()
main_dict = {1:(650, 650, 100, 100, "GO"),
40:(594, 650, 56, 100, "BOARDWALK"),
39:(539, 650, 56, 100, "LUXURY TAX"),
38:(482, 650, 56, 100, "PARK PLACE"),
37:(426, 650, 56, 100, "CHANCE"),
36:(370, 650, 56, 100, "SHORT LINE"),
35:(314, 650, 56, 100, "PENNSYLVANIA AVENUE"),
34:(258, 650, 56, 100, "COMMUNITY CHEST"),
33:(202, 650, 56, 100, "NORTH CAROLINA AVENUE"),
32:(150, 650, 52, 100, "PACIFIC AVENUE"),
31:(50, 650, 100, 100, "GO TO JAIL"),
30:(50, 594, 100, 56, "MARVIN GARDENS"),
29:(50, 539, 100, 56, "WATER WORKS"),
28:(50, 482, 100, 56, "VENTNOR AVENUE"),
27:(50, 426, 100, 56, "ATLANTIC AVENUE"),
26:(50, 370, 100, 56, "B. & O. RAILROAD"),
25:(50, 314, 100, 56, "ILLINOIS AVENUE"),
24:(50, 258, 100, 56, "INDIANA AVENUE"),
23:(50, 202, 100, 56, "CHANCE"),
22:(50, 150, 100, 52, "KENTUCKY AVENUE"),
21:(50, 50, 100, 100, "FREE PARKING"),
20:(150, 50, 56, 100, "NEW YORK AVENUE"),
19:(206, 50, 56, 100, "TENNESSEE AVENUE"),
18:(262, 50, 56, 100, "COMMUNITY CHEST"),
17:(318, 50, 56, 100, "ST. JAMES PLACE"),
16:(374, 50, 56, 100, "PENNSYLVANIA RAILROAD"),
15:(430, 50, 56, 100, "VIRGINIA AVENUE"),
14:(486, 50, 56, 100, "STATES AVENUE"),
13:(542, 50, 56, 100, "ELECTRIC COMPANY"),
12:(596, 50, 54, 100, "ST. CHARLES PLACE"),
11:(650, 50, 100, 100, "JUST VISITING"),
10:(650, 150, 100, 56, "CONNECTICUT AVENUE"),
9:(650, 206, 100, 56, "VERMONT AVENUE"),
8:(650, 262, 100, 56, "CHANCE"),
7:(650, 318, 100, 56, "ORIENTAL AVENUE"),
6:(650, 374, 100, 56, "READING RAILROAD"),
5:(650, 430, 100, 56, "INCOME TAX"),
4:(650, 486, 100, 56, "BALTIC AVENUE"),
3:(650, 542, 100, 56, "COMMUNITY CHEST"),
2:(650, 596, 100, 54, "MEDITERRANEAN AVENUE"),
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
monop = pygame.sprite.Sprite(all_sprites)
monop.image = image
monop.rect = monop.image.get_rect()
monop.rect.x = 50
monop.rect.y = 50
pygame.draw.rect(screen, 'white', (0, 0, 50, 50))
screen.fill(pygame.Color("black"))
running = True
changer = 0

class Chip:
    def __init__(self, ident, color, number_person):
        self.cordinate_chip = 1
        self.ident = ident
        self.color = color
        self.number = number_person
        self.x = main_dict[1][0] + self.ident[0]
        self.y = main_dict[1][0] + self.ident[1]

    
    def draw(self):
        pygame.draw.circle(screen, pygame.Color(self.color), (self.x, self.y), 10, 0)
    
    def step(self):
        screen.fill(pygame.Color("black"))
        num = (random.randint(1,6),random.randint(1,6))
        if sum(num) + self.cordinate_chip > 40:
            self.cordinate_chip = self.cordinate_chip - 40
        helper = self.cordinate_chip
        self.cordinate_chip += sum(num)
        print(self.cordinate_chip)
        for i in range(sum(num)):
            all_sprites.draw(screen)
            helper += 1
            if helper > 40:
                helper = 1
            self.x = main_dict[helper][1] + self.ident[0]
            self.y = main_dict[helper][0] + self.ident[1]
            all_draw_pict()
            clock.tick(5)
            pygame.display.flip()
        f1 = pygame.font.Font(None, 50)
        f2 = pygame.font.Font(None, 50)
        text2 = f2.render(f'Игроку {self.number} Выпало:', True, (255, 0, 0))
        if sum(num) <= 4:
            text1 = f1.render(f'{sum(num)} хода', True, (0, 255, 0))
        else:
            text1 = f1.render(f'{sum(num)} ходов', True, (0, 255, 0))
        screen.blit(text2, (800, 100))
        screen.blit(text1, (800, 150))
        if main_dict[self.cordinate_chip][4] == "COMMUNITY CHEST":
            self.community_chest()
        elif main_dict[self.cordinate_chip][4] == "CHANCE":
            self.chance()
        else:
            self.card()

    def community_chest(self):
        chest = open("data/chest.txt")
        chest_list = chest.read().split("\n")
        f3 = pygame.font.Font(None, 50)
        text3 = f3.render("Общественная казна:", True, (255, 0, 0))
        screen.blit(text3, (800, 200))
        f4 = pygame.font.Font(None, 50)
        text4 = f4.render(random.choice(chest_list), True, (0, 255, 0))
        screen.blit(text4, (800, 250))

    def chance(self):
        chest = open("data/chest.txt")
        chest_list = chest.read().split("\n")
        f3 = pygame.font.Font(None, 50)
        text3 = f3.render("Шанс:", True, (255, 0, 0))
        screen.blit(text3, (800, 200))
        f4 = pygame.font.Font(None, 50)
        text4 = f4.render(random.choice(chest_list), True, (0, 255, 0))
        screen.blit(text4, (800, 250))

    def card(self):
        f3 = pygame.font.Font(None, 50)
        text3 = f3.render(main_dict[self.cordinate_chip][4], True, (255, 0, 0))
        screen.blit(text3, (800, 200))
        f4 = pygame.font.Font(None, 50)
        text4 = f4.render("Купить?", True, (0, 255, 0))
        screen.blit(text4, (800, 250))
        yes = pygame.font.Font(None, 50)
        text_yes = yes.render("Да", True, (0, 0, 255))
        screen.blit(text_yes, (800, 300))
        no = pygame.font.Font(None, 50)
        text_no = no.render("Нет", True, (0, 0, 255))
        screen.blit(text_no, (900, 300))

chips = []
n = 1
for i in range(n):
    if i == 0:
        chips.append(Chip((10, 20), 'red', i + 1))
    elif i == 1:
        chips.append(Chip((40, 20), 'blue', i + 1))
    elif i == 2:
        chips.append(Chip((10, 50), 'yellow', i + 1))
    else:
        chips.append(Chip((40, 50), 'green', i + 1))

def all_draw_pict():
    for i in chips:
        i.draw()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 500 > event.pos[0] > 320 and 500 > event.pos[1] > 320:
                if changer == 0:
                    chips[0].step()
                    changer += 1
                    if changer >= n:
                        changer = 0
                elif changer == 1:
                    chips[1].step()
                    changer += 1
                    if changer >= n:
                        changer = 0
                elif changer == 2:
                    chips[2].step()
                    changer += 1
                    if changer >= n:
                        changer = 0
                elif changer == 3:
                    chips[3].step()
                    changer = 0
                    if changer >= n:
                        changer = 0
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
    all_draw_pict()
    pygame.display.flip()
pygame.quit()

