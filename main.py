import os
import time
import sqlite3

import pygame
import random

pygame.init()
main_dict = {1: (650, 650, 100, 100, "GO"),
             40: (594, 650, 56, 100, "BOARDWALK"),
             39: (539, 650, 56, 100, "LUXURY TAX"),
             38: (482, 650, 56, 100, "PARK PLACE"),
             37: (426, 650, 56, 100, "CHANCE"),
             36: (370, 650, 56, 100, "SHORT LINE"),
             35: (314, 650, 56, 100, "PENNSYLVANIA AVENUE"),
             34: (258, 650, 56, 100, "COMMUNITY CHEST"),
             33: (202, 650, 56, 100, "NORTH CAROLINA AVENUE"),
             32: (150, 650, 52, 100, "PACIFIC AVENUE"),
             31: (50, 650, 100, 100, "GO TO JAIL"),
             30: (50, 594, 100, 56, "MARVIN GARDENS"),
             29: (50, 539, 100, 56, "WATER WORKS"),
             28: (50, 482, 100, 56, "VENTNOR AVENUE"),
             27: (50, 426, 100, 56, "ATLANTIC AVENUE"),
             26: (50, 370, 100, 56, "B. & O. RAILROAD"),
             25: (50, 314, 100, 56, "ILLINOIS AVENUE"),
             24: (50, 258, 100, 56, "INDIANA AVENUE"),
             23: (50, 202, 100, 56, "CHANCE"),
             22: (50, 150, 100, 52, "KENTUCKY AVENUE"),
             21: (50, 50, 100, 100, "FREE PARKING"),
             20: (150, 50, 56, 100, "NEW YORK AVENUE"),
             19: (206, 50, 56, 100, "TENNESSEE AVENUE"),
             18: (262, 50, 56, 100, "COMMUNITY CHEST"),
             17: (318, 50, 56, 100, "ST. JAMES PLACE"),
             16: (374, 50, 56, 100, "PENNSYLVANIA RAILROAD"),
             15: (430, 50, 56, 100, "VIRGINIA AVENUE"),
             14: (486, 50, 56, 100, "STATES AVENUE"),
             13: (542, 50, 56, 100, "ELECTRIC COMPANY"),
             12: (596, 50, 54, 100, "ST. CHARLES PLACE"),
             11: (650, 50, 100, 100, "JUST VISITING"),
             10: (650, 150, 100, 56, "CONNECTICUT AVENUE"),
             9: (650, 206, 100, 56, "VERMONT AVENUE"),
             8: (650, 262, 100, 56, "CHANCE"),
             7: (650, 318, 100, 56, "ORIENTAL AVENUE"),
             6: (650, 374, 100, 56, "READING RAILROAD"),
             5: (650, 430, 100, 56, "INCOME TAX"),
             4: (650, 486, 100, 56, "BALTIC AVENUE"),
             3: (650, 542, 100, 56, "COMMUNITY CHEST"),
             2: (650, 596, 100, 54, "MEDITERRANEAN AVENUE"),
             'main': (320, 320, 180, 180)
             }


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


def abc(a):
    list_str = list()
    b = a
    for _ in range(a.count("%%%")):
        c = b.find("%%%")
        list_str.append(b[:c])
        b = b[c + 3:]
    list_str.append(b)
    return list_str


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
screen.fill(pygame.Color("black"))
running = True
changer = 0

con = sqlite3.connect("data/cards.sqlite")
cur = con.cursor()
numbers1 = list(range(16))
random.shuffle(numbers1)
n1 = 0
numbers2 = list(range(16))
random.shuffle(numbers2)
print(numbers1)
n2 = 0


class Chip:
    def __init__(self, ident, color, number_person, prison):
        self.cordinate_chip = 1
        self.ident = ident
        self.prison = prison
        self.color = color
        self.number = number_person
        self.x = main_dict[1][0] + self.ident[0]
        self.y = main_dict[1][0] + self.ident[1]
        self.count = 0

    def draw(self):
        pygame.draw.circle(screen, pygame.Color(self.color), (self.x, self.y), 10, 0)

    def step(self, num):
        global changer
        screen.fill(pygame.Color("black"))
        if num[0] == num[1]:
            self.count += 1
        else:
            self.count = 0
        for i in range(1, 7):
            if i == num[0]:
                image_kubik = load_image("kubik{}.png".format(i))
                kubik = pygame.sprite.Sprite(all_sprites)
                kubik.image = image_kubik
                kubik.rect = kubik.image.get_rect()
                kubik.rect.x = 280
                kubik.rect.y = 280
            if i == num[1]:
                image_kubik = load_image("kubik{}.png".format(i))
                kubik = pygame.sprite.Sprite(all_sprites)
                kubik.image = image_kubik
                kubik.rect = kubik.image.get_rect()
                kubik.rect.x = 400
                kubik.rect.y = 400
        if sum(num) + self.cordinate_chip > 40:
            self.cordinate_chip = self.cordinate_chip - 40
        self.cordinate_chip += sum(num)
        helper = self.cordinate_chip - sum(num)
        if self.count != 3:
            for i in range(sum(num)):
                helper += 1
                all_sprites.draw(screen)
                if helper > 40:
                    helper = 1
                elif helper == 11:
                    self.x = main_dict[11][1] + 10
                    self.y = main_dict[11][0] + self.prison
                else:
                    self.x = main_dict[helper][1] + self.ident[0]
                    self.y = main_dict[helper][0] + self.ident[1]
                all_draw_pict()
                clock.tick(2)
                pygame.display.flip()
            image = load_image("monop.png")
            monop = pygame.sprite.Sprite(all_sprites)
            monop.image = image
            monop.rect = monop.image.get_rect()
            monop.rect.x = 50
            monop.rect.y = 50
        else:
            if self.color == 'red':
                self.x = 95
                self.y = 670
            if self.color == 'blue':
                self.x = 125
                self.y = 670
            if self.color == 'yellow':
                self.x = 95
                self.y = 700
            if self.color == 'green':
                self.x = 125
                self.y = 700
            self.count = 0
            all_draw_pict()
        if main_dict[self.cordinate_chip][4] == "COMMUNITY CHEST":
            self.community_chest()
        elif main_dict[self.cordinate_chip][4] == "CHANCE":
            self.chance()
        else:
            self.card()

    def community_chest(self):
        a = 0
        global n1
        if n1 > 15:
            n1 = 0
        pygame.draw.rect(screen, (65, 155, 255), (290, 190, 620, 420), 0)
        pygame.draw.rect(screen, (255, 255, 255), (310, 210, 580, 380), 0)
        font_ok = pygame.font.Font(None, 50)
        text_ok = font_ok.render("OK", True, (0, 0, 0))
        text_ok_x = width // 2 - text_ok.get_width() // 2
        text_ok_y = 520
        text_ok_w = text_ok.get_width()
        text_ok_h = text_ok.get_height()
        screen.blit(text_ok, (text_ok_x, text_ok_y))
        pygame.draw.rect(screen, (0, 0, 0), (text_ok_x - 20, text_ok_y - 10, text_ok_w + 40, text_ok_h + 20), 1)
        fort_cc = pygame.font.Font(None, 60)
        text_cc = fort_cc.render("Общественная казна:", True, (0, 0, 0))
        text_cc_x = width // 2 - text_cc.get_width() // 2
        text_cc_y = 230
        screen.blit(text_cc, (text_cc_x, text_cc_y))
        fort_chest = pygame.font.Font(None, 40)
        result = cur.execute("""SELECT task FROM community_chest WHERE number = ?""", (numbers1[n1] + 1,)).fetchall()
        text = abc(result[0][0])
        for i in range(len(text)):
            text_chest = fort_chest.render(text[i], True, (0, 0, 0))
            text_chest_x = width // 2 - text_chest.get_width() // 2
            text_chest_y = text_cc_y + text_cc.get_height() + ((text_ok_y - 10 - (text_cc_y + text_cc.get_height()))
                                                               // 2 - text_chest.get_height() // 2)\
                           + i * text_chest.get_height()
            screen.blit(text_chest, (text_chest_x, text_chest_y))
        while a != 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if text_ok_x - 20 + text_ok_w + 40 >= event.pos[0] >= text_ok_x - 20 and \
                            text_ok_y - 10 + text_ok_h + 20 >= event.pos[1] >= text_ok_y - 10:
                        screen.fill((0, 0, 0))
                        a = 1
                        n1 += 1
            pygame.display.flip()

    def chance(self):
        a = 0
        global n2
        if n2 > 15:
            n2 = 0
        pygame.draw.rect(screen, (255, 155, 65), (290, 190, 620, 420), 0)
        pygame.draw.rect(screen, (255, 255, 255), (310, 210, 580, 380), 0)
        font_ok = pygame.font.Font(None, 50)
        text_ok = font_ok.render("OK", True, (0, 0, 0))
        text_ok_x = width // 2 - text_ok.get_width() // 2
        text_ok_y = 520
        text_ok_w = text_ok.get_width()
        text_ok_h = text_ok.get_height()
        screen.blit(text_ok, (text_ok_x, text_ok_y))
        pygame.draw.rect(screen, (0, 0, 0), (text_ok_x - 20, text_ok_y - 10, text_ok_w + 40, text_ok_h + 20), 1)
        fort_ch = pygame.font.Font(None, 60)
        text_ch = fort_ch.render("Шанс:", True, (0, 0, 0))
        text_ch_x = width // 2 - text_ch.get_width() // 2
        text_ch_y = 230
        screen.blit(text_ch, (text_ch_x, text_ch_y))
        fort_chance = pygame.font.Font(None, 40)
        result = cur.execute("""SELECT task FROM chance WHERE number = ?""", (numbers2[n2] + 1,)).fetchall()
        text = abc(result[0][0])
        for i in range(len(text)):
            text_chance = fort_chance.render(text[i], True, (0, 0, 0))
            text_chance_x = width // 2 - text_chance.get_width() // 2
            text_chance_y = text_ch_y + text_ch.get_height() + ((text_ok_y - 10 - (text_ch_y + text_ch.get_height()))
                                                                // 2 - text_chance.get_height() * len(text) // 2)\
                            + i * text_chance.get_height()
            screen.blit(text_chance, (text_chance_x, text_chance_y))
        while a != 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if text_ok_x - 20 + text_ok_w + 40 >= event.pos[0] >= text_ok_x - 20 and \
                            text_ok_y - 10 + text_ok_h + 20 >= event.pos[1] >= text_ok_y - 10:
                        screen.fill((0, 0, 0))
                        a = 1
                        n2 += 1
            pygame.display.flip()

    def card(self):
        pass


chips = []
n = 2
for i in range(n):
    if i == 0:
        chips.append(Chip((10, 20), 'red', i + 1, 15))
    elif i == 1:
        chips.append(Chip((40, 20), 'blue', i + 1, 40))
    elif i == 2:
        chips.append(Chip((10, 50), 'yellow', i + 1, 65))
    else:
        chips.append(Chip((40, 50), 'green', i + 1, 90))


def all_draw_pict():
    for i in chips:
        i.draw()


count = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 1110 >= event.pos[0] >= 840 and 700 >= event.pos[1] >= 640:
                num = (random.randint(1, 6), random.randint(1, 6))
                if num[0] == num[1]:
                    count += 1
                else:
                    count = 0
                if changer == 0:
                    chips[0].step(num)
                    if num[0] != num[1]:
                        changer += 1
                        count = 0
                    elif count == 3:
                        changer += 1
                        if changer >= n:
                            changer = 0
                        count = 0
                elif changer == 1:
                    chips[1].step(num)
                    if num[0] != num[1]:
                        changer += 1
                        if changer >= n:
                            changer = 0
                        count = 0
                    elif count == 3:
                        changer += 1
                        if changer >= n:
                            changer = 0
                        count = 0
                elif changer == 2:
                    chips[2].step(num)
                    if num[0] != num[1]:
                        changer += 1
                        if changer >= n:
                            changer = 0
                        count = 0
                    elif count == 3:
                        changer += 1
                        if changer >= n:
                            changer = 0
                        count = 0
                elif changer == 3:
                    chips[3].step(num)
                    if num[0] != num[1]:
                        changer = 0
                        if changer >= n:
                            changer = 0
                        count = 0
                    elif count == 3:
                        changer += 1
                        if changer >= n:
                            changer = 0
                        count = 0

    pygame.draw.rect(screen, 'white', (840, 640, 270, 60))
    pygame.draw.rect(screen, 'darkgrey', (840, 640, 270, 60), 3)
    all_sprites.draw(screen)
    f3 = pygame.font.Font(None, 34)
    text3 = f3.render('Бросить кубики', True, (0, 0, 0))
    screen.blit(text3, (880, 658))

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
    pygame.draw.rect(screen, 'white', (85, 650, 65, 65), 1)
    all_draw_pict()
    pygame.display.flip()
con.close()
pygame.quit()
