import os

import pygame
import random
import sqlite3

pygame.init()
main_dict = {1: [650, 650, 100, 100, "GO", "", (255, 255, 255)],
             40: [594, 650, 56, 100, "BOARDWALK", "$400", (70, 130, 180), 200, 0, 0, 50, 200, 600, 1400, 1700, 2000],
             39: [539, 650, 56, 100, "LUXURY TAX", "PAY $100", (255, 255, 255)],
             38: [482, 650, 56, 100, "PARK PLACE", "$350", (70, 130, 180), 200, 0, 0, 35, 175, 500, 1100, 1300, 1500],
             37: [426, 650, 56, 100, "CHANCE", "", (255, 255, 255)],
             36: [370, 650, 56, 100, "SHORT LINE", "$200", (255, 255, 255)],
             35: [314, 650, 56, 100, "PENNSYLVANIA AVENUE", "$320", (0, 128, 0), 200, 0, 0, 28, 150, 450, 1000, 1200,
                  1400],
             34: [258, 650, 56, 100, "COMMUNITY CHEST", "", (255, 255, 255)],
             33: [202, 650, 56, 100, "NORTH CAROLINA AVENUE", "$300", (0, 128, 0), 200, 0, 0, 26, 130, 390, 900, 1100,
                  1275],
             32: [150, 650, 52, 100, "PACIFIC AVENUE", "$300", (0, 128, 0), 200, 0, 0, 26, 130, 390, 900, 1100, 1275],
             31: [50, 650, 100, 100, "GO TO JAIL", "", (255, 255, 255)],
             30: [50, 594, 100, 56, "MARVIN GARDENS", "$280", (255, 255, 0), 150, 0, 0, 24, 120, 360, 850, 1025, 1200],
             29: [50, 539, 100, 56, "WATER WORKS", "$150", (255, 255, 255)],
             28: [50, 482, 100, 56, "VENTNOR AVENUE", "$260", (255, 255, 0), 150, 0, 0, 22, 110, 330, 800, 975, 1150],
             27: [50, 426, 100, 56, "ATLANTIC AVENUE", "$260", (255, 255, 0), 150, 0, 0, 22, 110, 330, 800, 975, 1150],
             26: [50, 370, 100, 56, "B. & O. RAILROAD", "$200", (255, 255, 255)],
             25: [50, 314, 100, 56, "ILLINOIS AVENUE", "$240", (255, 0, 0), 100, 0, 0, 20, 100, 300, 750, 925, 1100],
             24: [50, 258, 100, 56, "INDIANA AVENUE", "$220", (255, 0, 0), 100, 0, 0, 18, 90, 250, 700, 875, 1050],
             23: [50, 202, 100, 56, "CHANCE", "", (255, 255, 255)],
             22: [50, 150, 100, 52, "KENTUCKY AVENUE", "$220", (255, 0, 0), 100, 0, 0, 18, 90, 250, 700, 875, 1050],
             21: [50, 50, 100, 100, "FREE PARKING", "", (255, 255, 255)],
             20: [150, 50, 56, 100, "NEW YORK AVENUE", "$200", (255, 140, 0), 100, 0, 0, 16, 80, 220, 600, 800, 1000],
             19: [206, 50, 56, 100, "TENNESSEE AVENUE", "$180", (255, 140, 0), 100, 0, 0, 14, 70, 200, 550, 750, 950],
             18: [262, 50, 56, 100, "COMMUNITY CHEST", "", (255, 255, 255)],
             17: [318, 50, 56, 100, "ST. JAMES PLACE", "$180", (255, 140, 0), 100, 0, 0, 14, 70, 200, 550, 750, 950],
             16: [374, 50, 56, 100, "PENNSYLVANIA RAILROAD", "$200", (255, 255, 255)],
             15: [430, 50, 56, 100, "VIRGINIA AVENUE", "$160", (199, 21, 133), 100, 0, 0, 12, 60, 180, 500, 700, 900],
             14: [486, 50, 56, 100, "STATES AVENUE", "$140", (199, 21, 133), 100, 0, 0, 10, 50, 150, 450, 625, 750],
             13: [542, 50, 56, 100, "ELECTRIC COMPANY", "$150", (255, 255, 255)],
             12: [596, 50, 54, 100, "ST. CHARLES PLACE", "$140", (199, 21, 133), 100, 0, 0, 10, 50, 150, 450, 625, 750],
             11: [650, 50, 100, 100, "JUST VISITING", "", (255, 255, 255)],
             10: [650, 150, 100, 56, "CONNECTICUT AVENUE", "$120", (175, 238, 238), 50, 0, 0, 8, 40, 100, 300, 450,
                  600],
             9: [650, 206, 100, 56, "VERMONT AVENUE", "$100", (175, 238, 238), 50, 0, 0, 6, 30, 90, 270, 400, 550],
             8: [650, 262, 100, 56, "CHANCE", "", (255, 255, 255)],
             7: [650, 318, 100, 56, "ORIENTAL AVENUE", "$100", (175, 238, 238), 50, 0, 0, 6, 30, 90, 270, 400, 550],
             6: [650, 374, 100, 56, "READING RAILROAD", "$200", (255, 255, 255)],
             5: [650, 430, 100, 56, "INCOME TAX", "PAY $200", (255, 255, 255)],
             4: [650, 486, 100, 56, "BALTIC AVENUE", "$60", (77, 34, 14), 50, 0, 0, 4, 20, 60, 180, 320, 450],
             3: [650, 542, 100, 56, "COMMUNITY CHEST", "", (255, 255, 255)],
             2: [650, 596, 100, 54, "MEDITERRANEAN AVENUE", "$60", (77, 34, 14), 50, 0, 0, 2, 10, 30, 90, 160, 250],
             'main': (320, 320, 180, 180)
             }
n1, n2 = 0, 0
chest_dict = dict()
for i, x in enumerate(open('data/chest.txt', encoding='utf-8')):
    chest_dict[i] = x[:-1]
num_chest = list(range(len(chest_dict)))
random.shuffle(num_chest)

con = sqlite3.connect("data/cards.sqlite")
cur = con.cursor()
numbers1 = list(range(16))
random.shuffle(numbers1)
numbers2 = list(range(16))
random.shuffle(numbers2)


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


class Chip:
    def __init__(self, ident, color, number_person, prison):
        self.cordinate_chip = 1
        self.homes = {'red': [], 'blue': [], 'orange': [], 'green': []}
        self.ident = ident
        self.prison = prison
        self.color = color
        self.number = number_person
        self.x = main_dict[self.cordinate_chip][0] + self.ident[0]
        self.y = main_dict[self.cordinate_chip][0] + self.ident[1]
        self.count = 0
        self.money = 1500
        self.jail_free = False
        self.house = 0
        self.hotel = 0

    def ne_hvataet_deneg(self):
        pygame.draw.rect(screen, 'red', (174, 54, 452, 612), 0)
        pygame.draw.rect(screen, (255, 255, 255), (180, 60, 440, 600), 0)
        font = pygame.font.Font(None, 35)
        t = font.render("К сожалению, ", True, "black")
        screen.blit(t, (320, 200))
        t = font.render("вам не хватает денег для покупки", True, "black")
        screen.blit(t, (195, 230))
        pygame.draw.rect(screen, 'red', (194, 668, 412, 62), 0)
        pygame.draw.rect(screen, (255, 255, 255), (200, 674, 400, 50), 0)
        font = pygame.font.Font(None, 60)
        t = font.render("ОК", True, "black")
        screen.blit(t, (370, 680))
        b = 0
        while b != 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 194 <= event.pos[0] <= 606 and 668 <= event.pos[1] <= 730:
                        b = 1
            pygame.display.flip()

    def bankrot(self):
        pygame.draw.rect(screen, 'red', (174, 54, 452, 612), 0)
        pygame.draw.rect(screen, (255, 255, 255), (180, 60, 440, 600), 0)
        font = pygame.font.Font(None, 50)
        t = font.render("ВЫ СТАЛИ БАНКРОТОМ".format(self.color), True, "black")
        screen.blit(t, (190, 200))
        font = pygame.font.Font(None, 35)
        t = font.render("Вы выбываете из игры", True, "black")
        screen.blit(t, (260, 245))
        pygame.draw.rect(screen, self.color, (194, 668, 412, 62), 0)
        pygame.draw.rect(screen, (255, 255, 255), (200, 674, 400, 50), 0)
        font = pygame.font.Font(None, 60)
        t = font.render("ОК", True, "black")
        screen.blit(t, (370, 680))
        b = 0
        while b != 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 194 <= event.pos[0] <= 606 and 668 <= event.pos[1] <= 730:
                        b = 1
            pygame.display.flip()
        for s in chips:
            if s.get_color() == self.color:
                del chips[chips.index(s)]

    def go_to_card(self):
        if 21 >= self.cordinate_chip > 11:
            self.x = main_dict[self.cordinate_chip][1] + self.ident[0]
            self.y = main_dict[self.cordinate_chip][0] + self.ident[1] - 30
        elif 40 >= self.cordinate_chip > 31:
            self.x = main_dict[self.cordinate_chip][1] + self.ident[0] + 30
            self.y = main_dict[self.cordinate_chip][0] + self.ident[1] - 20
        elif self.cordinate_chip == 11:
            self.x = main_dict[11][1] + 10
            self.y = main_dict[11][0] + self.prison
        else:
            self.x = main_dict[self.cordinate_chip][1] + self.ident[0]
            self.y = main_dict[self.cordinate_chip][0] + self.ident[1]
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        self.print_money()
        all_draw_pict()
        pygame.display.flip()
        image = load_image("monop.png")
        monop = pygame.sprite.Sprite(all_sprites)
        monop.image = image
        monop.rect = monop.image.get_rect()
        monop.rect.x = 50
        monop.rect.y = 50
        pygame.display.flip()
        self.card(self.cordinate_chip)

    def print_money(self):
        pygame.draw.rect(screen, self.color, (780, 45, 390, 60), 0)
        t = pygame.font.Font(None, 50)
        text = t.render(f'Ваш капитал: ${self.money}', False, pygame.Color(245, 245, 245))
        screen.blit(text, (785, 60))

    def draw(self):
        if len(self.homes[self.color]) == 5:
            color = (150, 0, 24)
        else:
            color = (0, 69, 36)
        for i in self.homes:
            if len(self.homes[i]) == 5:
                pygame.draw.rect(screen, color, self.homes[i][-1], 0)
            else:
                for j in self.homes[i]:
                    pygame.draw.rect(screen, color, j, 0)
        pygame.draw.circle(screen, pygame.Color(self.color), (self.x, self.y), 10, 0)

    def step(self, num):
        global changer
        self.postroyka = 0
        screen.fill((0, 0, 0))
        self.print_money()
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
        if self.count != 3:
            if go_to_jail[self.color] > 0:
                pass
            else:
                for i in range(sum(num)):
                    all_sprites.draw(screen)
                    self.cordinate_chip += 1
                    if self.cordinate_chip > 40:
                        screen.fill((0, 0, 0))
                        all_sprites.draw(screen)
                        self.print_money()
                        self.cordinate_chip = 1
                        self.money += 200
                        self.print_money()
                    if 21 >= self.cordinate_chip > 11:
                        self.x = main_dict[self.cordinate_chip][1] + self.ident[0]
                        self.y = main_dict[self.cordinate_chip][0] + self.ident[1] - 30
                    elif 40 >= self.cordinate_chip > 31:
                        self.x = main_dict[self.cordinate_chip][1] + self.ident[0] + 30
                        self.y = main_dict[self.cordinate_chip][0] + self.ident[1] - 20
                    elif self.cordinate_chip == 11:
                        self.x = main_dict[11][1] + 10
                        self.y = main_dict[11][0] + self.prison
                    else:
                        self.x = main_dict[self.cordinate_chip][1] + self.ident[0]
                        self.y = main_dict[self.cordinate_chip][0] + self.ident[1]
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
            if go_to_jail[self.color] > 0:
                pass
            else:
                if self.color == 'red':
                    self.x = 95
                    self.y = 670
                    self.cordinate_chip = 11
                if self.color == 'blue':
                    self.x = 125
                    self.y = 670
                    self.cordinate_chip = 11
                if self.color == 'yellow':
                    self.x = 95
                    self.y = 700
                    self.cordinate_chip = 11
                if self.color == 'green':
                    self.x = 125
                    self.y = 700
                    self.cordinate_chip = 11
                self.count = 0
        all_draw_pict()
        if main_dict[self.cordinate_chip][4] == "COMMUNITY CHEST":
            self.community_chest()
        elif main_dict[self.cordinate_chip][4] == "CHANCE":
            self.chance()
        else:
            self.card(self.cordinate_chip)

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
        result = cur.execute("""SELECT ru FROM community_chest WHERE number = ?""",
                             (numbers1[n1] + 1,)).fetchall()
        text = abc(result[0][0])
        for i in range(len(text)):
            text_chest = fort_chest.render(text[i], True, (0, 0, 0))
            text_chest_x = width // 2 - text_chest.get_width() // 2
            text_chest_y = text_cc_y + text_cc.get_height() + ((text_ok_y - 10 - (text_cc_y + text_cc.get_height()))
                                                               // 2 - text_chest.get_height() * len(text) // 2) \
                           + i * text_chest.get_height()
            screen.blit(text_chest, (text_chest_x, text_chest_y))
        while a != 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if text_ok_x - 20 + text_ok_w + 40 >= event.pos[0] >= text_ok_x - 20 and \
                            text_ok_y - 10 + text_ok_h + 20 >= event.pos[1] >= text_ok_y - 10:
                        n = numbers1[n1]
                        if n == 0:
                            self.money += 200
                            self.cordinate_chip = 1
                            self.go_to_card()

                        elif n == 1:
                            self.money += 200

                        elif n == 2:
                            self.money -= 50

                        elif n == 3:
                            self.money += 50

                        elif n == 4:
                            self.jail_free = True

                        elif n == 5:
                            self.cordinate_chip = 31
                            self.go_to_card()

                        elif n == 6:
                            self.money += 100

                        elif n == 7:
                            self.money += 20

                        elif n == 8:
                            for i in chips:
                                i.money -= 10
                                self.money += 10

                        elif n == 9:
                            self.money += 100

                        elif n == 10:
                            self.money -= 100

                        elif n == 11:
                            self.money -= 50

                        elif n == 12:
                            self.money += 25

                        elif n == 13:
                            self.money -= self.house * 40
                            self.money -= self.hotel * 115

                        elif n == 14:
                            self.money += 10

                        elif n == 15:
                            self.money += 100

                        if self.money < 0:
                            self.bankrot()
                            a = 1
                            screen.fill((0, 0, 0))
                        else:
                            screen.fill((0, 0, 0))
                            all_sprites.draw(screen)
                            self.print_money()
                            all_draw_pict()
                            pygame.display.flip()
                            image = load_image("monop.png")
                            monop = pygame.sprite.Sprite(all_sprites)
                            monop.image = image
                            monop.rect = monop.image.get_rect()
                            monop.rect.x = 50
                            monop.rect.y = 50
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
        result = cur.execute("""SELECT ru FROM chance WHERE number = ?""", (numbers2[n2] + 1,)).fetchall()
        text = abc(result[0][0])
        for i in range(len(text)):
            text_chance = fort_chance.render(text[i], True, (0, 0, 0))
            text_chance_x = width // 2 - text_chance.get_width() // 2
            text_chance_y = text_ch_y + text_ch.get_height() + ((text_ok_y - 10 - (text_ch_y + text_ch.get_height()))
                                                                // 2 - text_chance.get_height() * len(text) // 2) \
                            + i * text_chance.get_height()
            screen.blit(text_chance, (text_chance_x, text_chance_y))
        while a != 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if text_ok_x - 20 + text_ok_w + 40 >= event.pos[0] >= text_ok_x - 20 and \
                            text_ok_y - 10 + text_ok_h + 20 >= event.pos[1] >= text_ok_y - 10:
                        n = numbers2[n2]
                        if n == 0:
                            self.cordinate_chip = 40
                            self.go_to_card()

                        elif n == 1:
                            self.money += 200
                            self.cordinate_chip = 1
                            self.go_to_card()

                        elif n == 2:
                            if self.cordinate_chip > 25:
                                self.money += 200
                            self.cordinate_chip = 25
                            self.go_to_card()

                        elif n == 3:
                            if self.cordinate_chip > 12:
                                self.money += 200
                            self.cordinate_chip = 12
                            self.go_to_card()

                        elif n == 4 or n == 5:
                            d = 41
                            for i in [6, 16, 26, 36]:
                                if i < self.cordinate_chip:
                                    a = self.cordinate_chip - i
                                    b = 40 - self.cordinate_chip + i
                                else:
                                    a = i - self.cordinate_chip
                                    b = 40 - i + self.cordinate_chip
                                c = min(a, b)
                                if c <= d:
                                    d = c
                                    e = i
                            self.cordinate_chip = e
                            self.go_to_card()
                            # недоделанно

                        elif n == 6:
                            d = 41
                            for i in [13, 29]:
                                if i < self.cordinate_chip:
                                    a = self.cordinate_chip - i
                                    b = 40 - self.cordinate_chip + i
                                else:
                                    a = i - self.cordinate_chip
                                    b = 40 - i + self.cordinate_chip
                                c = min(a, b)
                                if c <= d:
                                    d = c
                                    e = i
                            self.cordinate_chip = e
                            self.go_to_card()
                            # недоделанно

                        elif n == 7:
                            self.money += 50

                        elif n == 8:
                            self.jail_free = True

                        elif n == 9:
                            self.cordinate_chip -= 3
                            if self.cordinate_chip < 1:
                                self.cordinate_chip = 40 - self.cordinate_chip
                            self.go_to_card()

                        elif n == 10:
                            self.cordinate_chip = 31
                            self.go_to_card()

                        elif n == 11:
                            self.money -= self.house * 25
                            self.money -= self.hotel * 100

                        elif n == 12:
                            self.money -= 15

                        elif n == 13:
                            if self.cordinate_chip > 6:
                                self.money += 200
                            self.cordinate_chip = 6
                            self.go_to_card()

                        elif n == 14:
                            for i in chips:
                                i.money += 50
                                self.money -= 50

                        elif n == 15:
                            self.money += 150

                        if self.money < 0:
                            self.bankrot()
                            a = 1
                        else:
                            screen.fill((0, 0, 0))
                            all_sprites.draw(screen)
                            self.print_money()
                            all_draw_pict()
                            pygame.display.flip()
                            image = load_image("monop.png")
                            monop = pygame.sprite.Sprite(all_sprites)
                            monop.image = image
                            monop.rect = monop.image.get_rect()
                            monop.rect.x = 50
                            monop.rect.y = 50
                            a = 1
                            n2 += 1
            pygame.display.flip()

    def card(self, index):
        a = 0
        if main_dict[index][4] == "GO" or main_dict[index][4] == "FREE PARKING" or \
                main_dict[index][4] == "JUST VISITING":
            pass
        elif "RAILROAD" in main_dict[index][4] or main_dict[index][4] == "SHORT LINE" or \
                main_dict[index][4] == "INCOME TAX" or main_dict[index][4] == "ELECTRIC COMPANY" or \
                main_dict[index][4] == "WATER WORKS" or main_dict[index][4] == "LUXURY TAX":
            if "RAILROAD" in main_dict[index][4] or main_dict[index][4] == "SHORT LINE":
                picture = "train"
            elif main_dict[index][4] == "INCOME TAX":
                picture = "income"
            elif main_dict[index][4] == "ELECTRIC COMPANY":
                picture = "electric"
            elif main_dict[index][4] == "WATER WORKS":
                picture = "kran"
            elif main_dict[index][4] == "LUXURY TAX":
                picture = "luxury"
            font_street_name = pygame.font.Font(None, 40)
            if main_dict[index][4] == "INCOME TAX" or main_dict[index][4] == "LUXURY TAX":
                pygame.draw.rect(screen, (0, 0, 0), (176, 56, 448, 608), 0)
                pygame.draw.rect(screen, main_dict[index][6], (180, 60, 440, 600), 0)
                pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 500), 0)
                all_sprites = pygame.sprite.Group()
                image = load_image("{}.png".format(picture))
                pict = pygame.sprite.Sprite(all_sprites)
                pict.image = image
                pict.rect = pict.image.get_rect()
                pict.rect.x = 300
                pict.rect.y = 250
                street_name = font_street_name.render("{}".format(main_dict[index][4]), True, (0, 0, 0))
                p = (440 - street_name.get_size()[0]) // 2
                screen.blit(street_name, (180 + p, 100))
                font_price = pygame.font.Font(None, 50)
                price = font_price.render("{}".format(main_dict[index][5]), True, (0, 0, 0))
                p = (440 - price.get_size()[0]) // 2
                screen.blit(price, (180 + p, 600))
                all_sprites.draw(screen)
            else:
                if 'BOUGHT' not in main_dict[self.cordinate_chip][5]:
                    pygame.draw.rect(screen, (0, 0, 0), (176, 56, 448, 608), 0)
                    pygame.draw.rect(screen, main_dict[index][6], (180, 60, 440, 600), 0)
                    pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 500), 0)
                    font_street_name = pygame.font.Font(None, 40)
                    all_sprites = pygame.sprite.Group()
                    image = load_image("{}.png".format(picture))
                    pict = pygame.sprite.Sprite(all_sprites)
                    pict.image = image
                    pict.rect = pict.image.get_rect()
                    pict.rect.x = 300
                    pict.rect.y = 150
                    if "RAILROAD" in main_dict[index][4] or main_dict[index][4] == "SHORT LINE":
                        font_rent = pygame.font.Font(None, 36)
                        rent = font_rent.render('Рента', True, (0, 0, 0))
                        screen.blit(rent, (365, 360))
                        font_rent = pygame.font.Font(None, 28)
                        rent = font_rent.render('Если игрок владеет 1 станцией', True, (0, 0, 0))
                        screen.blit(rent, (195, 420))
                        rent = font_rent.render('$25', True, (0, 0, 0))
                        screen.blit(rent, (555, 420))
                        rent = font_rent.render('Если игрок владеет 2 станциями', True, (0, 0, 0))
                        screen.blit(rent, (195, 460))
                        rent = font_rent.render('$50', True, (0, 0, 0))
                        screen.blit(rent, (555, 460))
                        rent = font_rent.render('Если игрок владеет 3 станциями', True, (0, 0, 0))
                        screen.blit(rent, (195, 500))
                        rent = font_rent.render('$100', True, (0, 0, 0))
                        screen.blit(rent, (555, 500))
                        rent = font_rent.render('Если игрок владеет 4 станциями', True, (0, 0, 0))
                        screen.blit(rent, (195, 540))
                        rent = font_rent.render('$200', True, (0, 0, 0))
                        screen.blit(rent, (555, 540))
                    else:
                        font_rent = pygame.font.Font(None, 28)
                        rent = font_rent.render('Чтобы вычислить ренту, киньте', True, (0, 0, 0))
                        screen.blit(rent, (250, 345))
                        rent = font_rent.render('кубики еще раз', True, (0, 0, 0))
                        screen.blit(rent, (330, 365))
                        font_rent = pygame.font.Font(None, 28)
                        rent = font_rent.render('Если игрок владеет один видом', True, (0, 0, 0))
                        screen.blit(rent, (240, 405))
                        rent = font_rent.render('коммунального предприятия, Рента', True, (0, 0, 0))
                        screen.blit(rent, (225, 425))
                        rent = font_rent.render('равна сумме выпавших очков,', True, (0, 0, 0))
                        screen.blit(rent, (250, 445))
                        rent = font_rent.render('умноженных на 4', True, (0, 0, 0))
                        screen.blit(rent, (315, 465))
                        font_rent = pygame.font.Font(None, 28)
                        rent = font_rent.render('Если игрок владеет обоими видами', True, (0, 0, 0))
                        screen.blit(rent, (240, 500))
                        rent = font_rent.render('коммунального предприятия, Рента', True, (0, 0, 0))
                        screen.blit(rent, (225, 520))
                        rent = font_rent.render('равна сумме выпавших очков,', True, (0, 0, 0))
                        screen.blit(rent, (250, 540))
                        rent = font_rent.render('умноженных на 10', True, (0, 0, 0))
                        screen.blit(rent, (315, 560))
                    all_sprites.draw(screen)
                    street_name = font_street_name.render("{}".format(main_dict[index][4]), True, (0, 0, 0))
                    p = (440 - street_name.get_size()[0]) // 2
                    screen.blit(street_name, (180 + p, 100))
                    font_price = pygame.font.Font(None, 50)
                    price = font_price.render("{}".format(main_dict[index][5]), True, (0, 0, 0))
                    p = (440 - price.get_size()[0]) // 2
                    screen.blit(price, (180 + p, 600))
            if main_dict[index][4] == "INCOME TAX" or main_dict[index][4] == "LUXURY TAX":
                pygame.draw.rect(screen, "black", (306, 670, 188, 58), 0)
                pygame.draw.rect(screen, (255, 255, 255), (310, 674, 180, 50), 0)
                pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 4), 0)
                font_oplata = pygame.font.Font(None, 40)
                oplata = font_oplata.render("ОПЛАТИТЬ", True, "black")
                p = (180 - oplata.get_size()[0]) // 2
                screen.blit(oplata, (310 + p, 687))
            else:
                if 'BOUGHT' not in main_dict[self.cordinate_chip][5]:
                    pygame.draw.rect(screen, "green", (196, 670, 188, 58), 0)
                    pygame.draw.rect(screen, "red", (416, 670, 188, 58), 0)
                    pygame.draw.rect(screen, (255, 255, 255), (200, 674, 180, 50), 0)
                    pygame.draw.rect(screen, (255, 255, 255), (420, 674, 180, 50), 0)
                    pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 4), 0)
                    font_pokupka = pygame.font.Font(None, 40)
                    kupit = font_pokupka.render("КУПИТЬ", True, "green")
                    font_pokupka = pygame.font.Font(None, 30)
                    nekupit = font_pokupka.render("НЕ ПОКУПАТЬ", True, "red")
                    p = (180 - kupit.get_size()[0]) // 2
                    screen.blit(kupit, (200 + p, 685))
                    p = (180 - nekupit.get_size()[0]) // 2
                    screen.blit(nekupit, (420 + p, 690))
            if main_dict[index][4] == "INCOME TAX" or main_dict[index][4] == "LUXURY TAX":
                while a != 1:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 306 <= event.pos[0] <= 494 and 670 <= event.pos[1] <= 728:
                                if self.money >= int(main_dict[self.cordinate_chip][5][5:]):
                                    self.money -= int(main_dict[self.cordinate_chip][5][5:])
                                    self.print_money()
                                    a = 1
                                else:
                                    self.bankrot()
                                    a = 1
                        pygame.display.flip()
            else:
                if 'BOUGHT' not in main_dict[self.cordinate_chip][5]:
                    while a != 1:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if 196 <= event.pos[0] <= 384 and 670 <= event.pos[1] <= 728:
                                    if self.money >= int(main_dict[self.cordinate_chip][5][1:]):
                                        self.money -= int(main_dict[self.cordinate_chip][5][1:])
                                        if "RAILROAD" in main_dict[index][4] or main_dict[index][4] == "SHORT LINE":
                                            sp_railroads[self.color] += 1
                                        else:
                                            sp_predpr[self.color] += 1
                                        main_dict[self.cordinate_chip][
                                            5] = 'BOUGHT_' + self.color.upper() + '_{}'.format(
                                            main_dict[self.cordinate_chip][5])
                                        self.print_money()
                                        a = 1
                                    else:
                                        self.ne_hvataet_deneg()
                                        a = 1
                                elif 416 <= event.pos[0] <= 604 and 670 <= event.pos[1] <= 728:
                                    a = 1
                        pygame.display.flip()
                else:
                    a = 0
                    if self.color.upper() not in main_dict[self.cordinate_chip][5]:
                        if "RAILROAD" in main_dict[index][4] or main_dict[index][4] == "SHORT LINE":
                            pygame.draw.rect(screen, (0, 0, 0), (176, 56, 448, 608), 0)
                            pygame.draw.rect(screen, main_dict[index][6], (180, 60, 440, 600), 0)
                            pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 500), 0)
                            font_street_name = pygame.font.Font(None, 40)
                            street_name = font_street_name.render("{}".format(main_dict[index][4]), True, (0, 0, 0))
                            p = (440 - street_name.get_size()[0]) // 2
                            screen.blit(street_name, (180 + p, 100))
                            font_rent = pygame.font.Font(None, 35)
                            rent = font_rent.render("Вы попали на железную дорогу, ", True, (0, 0, 0))
                            screen.blit(rent, (200, 210))
                            rent = font_rent.render("которой владеет другой игрок", True, (0, 0, 0))
                            screen.blit(rent, (210, 238))
                            all_sprites = pygame.sprite.Group()
                            image = load_image("{}.png".format(picture))
                            pict = pygame.sprite.Sprite(all_sprites)
                            pict.image = image
                            pict.rect = pict.image.get_rect()
                            pict.rect.x = 305
                            pict.rect.y = 270
                            all_sprites.draw(screen)
                            font_rent = pygame.font.Font(None, 40)
                            rent = font_rent.render("Заплатите ренту:", True, (0, 0, 0))
                            screen.blit(rent, (290, 475))
                            f = main_dict[self.cordinate_chip][5].index('_')
                            h = main_dict[self.cordinate_chip][5][f + 1:]
                            f = h[:h.index('_')].lower()
                            r = sp_railroads[f]
                            font_rent = pygame.font.Font(None, 50)
                            rent = font_rent.render("${}".format(50 * r), True, (0, 0, 0))
                            p = (180 - rent.get_size()[0]) // 2
                            screen.blit(rent, (312 + p, 515))
                            pygame.draw.rect(screen, "black", (186, 670, 425, 58), 0)
                            pygame.draw.rect(screen, (255, 255, 255), (190, 674, 417, 50), 0)
                            pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 4), 0)
                            font_oplata = pygame.font.Font(None, 40)
                            oplata = font_oplata.render("ОПЛАТИТЬ", True, "black")
                            p = (180 - oplata.get_size()[0]) // 2
                            screen.blit(oplata, (310 + p, 687))
                            while a != 1:
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if 190 <= event.pos[0] <= 611 and 670 <= event.pos[1] <= 728:
                                            if self.money >= int(main_dict[self.cordinate_chip][1]):
                                                self.money -= r * 50
                                                sp_rent[f] += r * 50
                                                self.print_money()
                                                a = 1
                                            else:
                                                self.bankrot()
                                                a = 1
                                    pygame.display.flip()
                        else:
                            pygame.draw.rect(screen, (0, 0, 0), (176, 56, 448, 608), 0)
                            pygame.draw.rect(screen, main_dict[index][6], (180, 60, 440, 600), 0)
                            pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 500), 0)
                            font_street_name = pygame.font.Font(None, 40)
                            street_name = font_street_name.render("{}".format(main_dict[index][4]), True, (0, 0, 0))
                            p = (440 - street_name.get_size()[0]) // 2
                            screen.blit(street_name, (180 + p, 100))
                            font_rent = pygame.font.Font(None, 35)
                            rent = font_rent.render("Вы попали на предприятие, ", True, (0, 0, 0))
                            screen.blit(rent, (230, 210))
                            rent = font_rent.render("которым владеет другой игрок", True, (0, 0, 0))
                            screen.blit(rent, (210, 238))
                            all_sprites = pygame.sprite.Group()
                            image = load_image("{}.png".format(picture))
                            pict = pygame.sprite.Sprite(all_sprites)
                            pict.image = image
                            pict.rect = pict.image.get_rect()
                            pict.rect.x = 305
                            pict.rect.y = 270
                            all_sprites.draw(screen)
                            rent = font_rent.render('Чтобы вычислить ренту, бросьте', True, (0, 0, 0))
                            screen.blit(rent, (200, 465))
                            rent = font_rent.render('кубики еще раз', True, (0, 0, 0))
                            screen.blit(rent, (300, 490))
                            pygame.draw.rect(screen, "black", (186, 670, 425, 58), 0)
                            pygame.draw.rect(screen, (255, 255, 255), (190, 674, 417, 50), 0)
                            pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 4), 0)
                            font_oplata = pygame.font.Font(None, 40)
                            oplata = font_oplata.render("БРОСИТЬ КУБИКИ", True, "black")
                            p = (180 - oplata.get_size()[0]) // 2
                            screen.blit(oplata, (310 + p, 687))
                            b = 0
                            f = main_dict[self.cordinate_chip][5].index('_')
                            h = main_dict[self.cordinate_chip][5][f + 1:]
                            f = h[:h.index('_')].lower()
                            s = 0
                            while b != 1:
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if 190 <= event.pos[0] <= 611 and 670 <= event.pos[1] <= 728:
                                            r = random.randint(1, 6) + random.randint(1, 6)
                                            if sp_predpr[f] == 1:
                                                s = 4
                                            elif sp_predpr[f] == 1:
                                                s = 10
                                            self.print_money()
                                            b = 1
                                    pygame.display.flip()
                            pygame.draw.rect(screen, (0, 0, 0), (176, 56, 448, 608), 0)
                            pygame.draw.rect(screen, main_dict[index][6], (180, 60, 440, 600), 0)
                            pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 500), 0)
                            font_street_name = pygame.font.Font(None, 40)
                            street_name = font_street_name.render("{}".format(main_dict[index][4]), True, (0, 0, 0))
                            p = (440 - street_name.get_size()[0]) // 2
                            screen.blit(street_name, (180 + p, 100))
                            font_rent = pygame.font.Font(None, 35)
                            rent = font_rent.render("Вы попали на предприятие, ", True, (0, 0, 0))
                            screen.blit(rent, (230, 210))
                            rent = font_rent.render("которым владеет другой игрок", True, (0, 0, 0))
                            screen.blit(rent, (210, 238))
                            all_sprites = pygame.sprite.Group()
                            image = load_image("{}.png".format(picture))
                            pict = pygame.sprite.Sprite(all_sprites)
                            pict.image = image
                            pict.rect = pict.image.get_rect()
                            pict.rect.x = 305
                            pict.rect.y = 270
                            all_sprites.draw(screen)
                            font_rent = pygame.font.Font(None, 40)
                            rent = font_rent.render("Заплатите ренту:", True, (0, 0, 0))
                            screen.blit(rent, (290, 475))
                            font_rent = pygame.font.Font(None, 50)
                            rent = font_rent.render("${}".format(s * r), True, (0, 0, 0))
                            p = (180 - rent.get_size()[0]) // 2
                            screen.blit(rent, (312 + p, 515))
                            pygame.draw.rect(screen, "black", (186, 670, 425, 58), 0)
                            pygame.draw.rect(screen, (255, 255, 255), (190, 674, 417, 50), 0)
                            pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 4), 0)
                            font_oplata = pygame.font.Font(None, 40)
                            oplata = font_oplata.render("ОПЛАТИТЬ", True, "black")
                            p = (180 - oplata.get_size()[0]) // 2
                            screen.blit(oplata, (310 + p, 687))
                            while a != 1:
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if 190 <= event.pos[0] <= 611 and 670 <= event.pos[1] <= 728:
                                            if self.money >= r * s:
                                                self.money -= r * s
                                                sp_rent[f] += r * s
                                                self.print_money()
                                                a = 1
                                            else:
                                                self.bankrot()
                                                a = 1
                                    pygame.display.flip()
                    elif self.color.upper() in main_dict[self.cordinate_chip][5]:
                        if "RAILROAD" in main_dict[index][4] or main_dict[index][4] == "SHORT LINE":
                            sl = 'железную дорогу'
                        else:
                            sl = 'предприятие'
                        pygame.draw.rect(screen, (0, 47, 85), (835, 500, 282, 60), 0)
                        pygame.draw.rect(screen, (245, 245, 245), (841, 506, 270, 48), 0)
                        f3 = pygame.font.Font(None, 28)
                        text3 = f3.render('Продать {}'.format(sl), True, (0, 0, 0))
                        if sl == 'железную дорогу':
                            screen.blit(text3, (845, 520))
                        else:
                            screen.blit(text3, (870, 520))
                        pygame.draw.rect(screen, 'white', (762, 640, 425, 60))
                        pygame.draw.rect(screen, 'darkgrey', (762, 640, 425, 60), 3)
                        f3 = pygame.font.Font(None, 28)
                        text3 = f3.render('Оставить {} без изменений'.format(sl), True, (0, 0, 0))
                        if sl == 'железную дорогу':
                            screen.blit(text3, (765, 660))
                        else:
                            screen.blit(text3, (787, 660))
                        while a != 1:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if 762 <= event.pos[0] <= 1187 and 640 <= event.pos[1] <= 700:
                                        screen.fill((0, 0, 0))
                                        self.print_money()
                                        a = 1
                                    elif 835 <= event.pos[0] <= 1117 and 500 <= event.pos[1] <= 560:
                                        if sl == 'железную дорогу':
                                            self.money += 100
                                            sp_railroads[self.color] -= 1
                                        else:
                                            self.money += 75
                                            sp_predpr[self.color] -= 1
                                        k = main_dict[self.cordinate_chip][5][7:]
                                        main_dict[self.cordinate_chip][5] = k
                                        p = main_dict[self.cordinate_chip][5][
                                            main_dict[self.cordinate_chip][5].index('_') + 1:]
                                        main_dict[self.cordinate_chip][5] = p
                                        screen.fill((0, 0, 0))
                                        self.print_money()
                                        a = 1
                            all_draw_pict()
                            pygame.display.flip()

        elif main_dict[index][4] == "GO TO JAIL":
            pygame.draw.rect(screen, (0, 0, 0), (176, 56, 448, 608), 0)
            pygame.draw.rect(screen, main_dict[index][6], (180, 60, 440, 600), 0)
            pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 500), 0)
            pygame.draw.rect(screen, "black", (306, 670, 188, 58), 0)
            pygame.draw.rect(screen, (255, 255, 255), (310, 674, 180, 50), 0)
            pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 4), 0)
            font_price = pygame.font.Font(None, 50)
            price = font_price.render("{}".format(main_dict[index][5]), True, (0, 0, 0))
            p = (440 - price.get_size()[0]) // 2
            screen.blit(price, (180 + p, 600))
            font_go = pygame.font.Font(None, 50)
            go = font_go.render("GO", True, "black")
            p = (180 - go.get_size()[0]) // 2
            screen.blit(go, (310 + p, 685))
            all_sprites = pygame.sprite.Group()
            image = load_image("gotojail.png")
            pict = pygame.sprite.Sprite(all_sprites)
            pict.image = image
            pict.rect = pict.image.get_rect()
            pict.rect.x = 260
            pict.rect.y = 220
            all_sprites.draw(screen)
            while a != 1:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 306 <= event.pos[0] <= 494 and 670 <= event.pos[1] <= 728:
                            if go_to_jail[self.color] == 0 and self.jail_free is False:
                                go_to_jail[self.color] = 1
                                self.x = main_dict[11][1] + self.ident[0] + 30
                                self.y = main_dict[11][0] + self.ident[1]
                                self.cordinate_chip = 11
                            elif self.jail_free is True:
                                self.jail_free = False
                                go_to_jail[self.color] = 0
                                self.x = main_dict[11][1] + self.ident[0] + 30
                                self.y = main_dict[11][0] + self.ident[1]
                                self.cordinate_chip = 11
                            a = 1
                pygame.display.flip()
        else:
            if main_dict[self.cordinate_chip][5][:6] != 'BOUGHT':
                pygame.draw.rect(screen, (0, 0, 0), (176, 56, 448, 608), 0)
                pygame.draw.rect(screen, main_dict[index][6], (180, 60, 440, 600), 0)
                pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 500), 0)
                pygame.draw.rect(screen, "green", (196, 670, 188, 58), 0)
                pygame.draw.rect(screen, "red", (416, 670, 188, 58), 0)
                pygame.draw.rect(screen, (255, 255, 255), (200, 674, 180, 50), 0)
                pygame.draw.rect(screen, (255, 255, 255), (420, 674, 180, 50), 0)
                pygame.draw.rect(screen, (0, 0, 0), (180, 160, 440, 4), 0)
                font_street_name = pygame.font.Font(None, 40)
                street_name = font_street_name.render("{}".format(main_dict[index][4]), True, (0, 0, 0))
                p = (440 - street_name.get_size()[0]) // 2
                screen.blit(street_name, (180 + p, 200))
                font_price = pygame.font.Font(None, 50)
                price = font_price.render("{}".format(main_dict[index][5]), True, (0, 0, 0))
                p = (440 - price.get_size()[0]) // 2
                screen.blit(price, (185 + p, 605))
                font_pokupka = pygame.font.Font(None, 40)
                kupit = font_pokupka.render("КУПИТЬ", True, "green")
                font_pokupka = pygame.font.Font(None, 30)
                nekupit = font_pokupka.render("НЕ ПОКУПАТЬ", True, "red")
                p = (180 - kupit.get_size()[0]) // 2
                screen.blit(kupit, (200 + p, 685))
                p = (180 - nekupit.get_size()[0]) // 2
                screen.blit(nekupit, (420 + p, 690))
                font_renta = pygame.font.Font(None, 30)
                renta = font_renta.render("Рента", True, "black")
                screen.blit(renta, (240, 265))
                font_cena = pygame.font.Font(None, 30)
                cena = font_cena.render("${}".format(main_dict[self.cordinate_chip][10]), True, "black")
                screen.blit(cena, (510, 265))
                font_renta = pygame.font.Font(None, 30)
                renta = font_renta.render("Рента с 1 домом", True, "black")
                screen.blit(renta, (240, 305))
                font_cena = pygame.font.Font(None, 30)
                cena = font_cena.render("${}".format(main_dict[self.cordinate_chip][11]), True, "black")
                screen.blit(cena, (510, 305))
                font_renta = pygame.font.Font(None, 30)
                renta = font_renta.render("Рента с 2 домами", True, "black")
                screen.blit(renta, (240, 345))
                font_cena = pygame.font.Font(None, 30)
                cena = font_cena.render("${}".format(main_dict[self.cordinate_chip][12]), True, "black")
                screen.blit(cena, (510, 345))
                font_renta = pygame.font.Font(None, 30)
                renta = font_renta.render("Рента с 3 домами", True, "black")
                screen.blit(renta, (240, 390))
                font_cena = pygame.font.Font(None, 30)
                cena = font_cena.render("${}".format(main_dict[self.cordinate_chip][13]), True, "black")
                screen.blit(cena, (510, 390))
                font_renta = pygame.font.Font(None, 30)
                renta = font_renta.render("Рента с 4 домами", True, "black")
                screen.blit(renta, (240, 435))
                font_cena = pygame.font.Font(None, 30)
                cena = font_cena.render("${}".format(main_dict[self.cordinate_chip][14]), True, "black")
                screen.blit(cena, (510, 435))
                font_renta = pygame.font.Font(None, 30)
                renta = font_renta.render("Рента с отелем", True, "black")
                screen.blit(renta, (240, 475))
                font_cena = pygame.font.Font(None, 30)
                cena = font_cena.render("${}".format(main_dict[self.cordinate_chip][15]), True, "black")
                screen.blit(cena, (510, 475))
                font_renta = pygame.font.Font(None, 30)
                renta = font_renta.render("Стоимость постройки дома или отеля", True, "black")
                screen.blit(renta, (185, 545))
                font_cena = pygame.font.Font(None, 30)
                cena = font_cena.render("${}".format(main_dict[self.cordinate_chip][7]), True, "black")
                screen.blit(cena, (570, 545))
                pygame.draw.line(screen, (0, 0, 0), (180, 530), (620, 530), 4)
                pygame.draw.line(screen, (0, 0, 0), (180, 580), (620, 580), 4)
                while a != 1:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 196 <= event.pos[0] <= 384 and 670 <= event.pos[1] <= 728:
                                if self.money >= int(main_dict[self.cordinate_chip][5][1:]):
                                    self.money -= int(main_dict[self.cordinate_chip][5][1:])
                                    main_dict[self.cordinate_chip][5] = 'BOUGHT_' + self.color.upper() + '_{}'.format(
                                        main_dict[self.cordinate_chip][5])
                                    self.print_money()
                                    a = 1
                                else:
                                    self.ne_hvataet_deneg()
                                    a = 1
                            elif 416 <= event.pos[0] <= 604 and 670 <= event.pos[1] <= 728:
                                self.print_money()
                                a = 1
                    pygame.display.flip()
            elif self.color.upper() in main_dict[self.cordinate_chip][5]:
                h = 0
                k = main_dict[self.cordinate_chip][6]
                for i in main_dict:
                    if i != 'main':
                        if main_dict[i][6] == k and self.color.upper() in main_dict[i][5]:
                            h += 1
                            if h == 3:
                                break
                if (k == (77, 34, 14) or k == (70, 130, 180)) and h == 2:
                    h = True
                elif h == 3:
                    h = True
                else:
                    h = False
                if h:
                    if main_dict[self.cordinate_chip][8] == 4:
                        color = (139, 0, 0)
                        sl = 'отель'
                    else:
                        color = (0, 69, 36)
                        sl = 'дом'
                    if main_dict[self.cordinate_chip][8] == 0:
                        pygame.draw.rect(screen, color, (850, 150, 250, 60), 0)
                        pygame.draw.rect(screen, (245, 245, 245), (856, 156, 238, 48), 0)
                        f3 = pygame.font.Font(None, 36)
                        text3 = f3.render('Построить {}'.format(sl), True, (0, 0, 0))
                        screen.blit(text3, (880, 168))
                if main_dict[self.cordinate_chip][9] == 1:
                    sl = 'отель'
                elif main_dict[self.cordinate_chip][8] >= 1:
                    sl = 'дом'
                else:
                    sl = 'улицу'
                pygame.draw.rect(screen, (0, 47, 85), (850, 500, 250, 60), 0)
                pygame.draw.rect(screen, (245, 245, 245), (856, 506, 238, 48), 0)
                f3 = pygame.font.Font(None, 36)
                text3 = f3.render('Продать {}'.format(sl), True, (0, 0, 0))
                screen.blit(text3, (880, 518))
                pygame.draw.rect(screen, 'white', (790, 640, 380, 60))
                pygame.draw.rect(screen, 'darkgrey', (790, 640, 380, 60), 3)
                f3 = pygame.font.Font(None, 34)
                text3 = f3.render('Оставить улицу без изменений', True, (0, 0, 0))
                screen.blit(text3, (800, 658))
                while a != 1:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 850 <= event.pos[0] <= 1100 and 150 <= event.pos[1] <= 210 and h:
                                self.money -= main_dict[self.cordinate_chip][7]
                                self.print_money()
                                time_dict = {0: (10, 10, 20, 20), 1: (10, 40, 20, 20), 2: (40, 10, 20, 20), 3: (40, 40, 20, 20), 4: (20, 20, 30, 30)}
                                if 0 <= main_dict[self.cordinate_chip][8] <= 4:
                                    self.homes[self.color].append((main_dict[self.cordinate_chip][1] + time_dict[main_dict[self.cordinate_chip][8]][0],
                                        main_dict[self.cordinate_chip][0] + time_dict[main_dict[self.cordinate_chip][8]][1], 
                                        time_dict[main_dict[self.cordinate_chip][8]][2], time_dict[main_dict[self.cordinate_chip][8]][3]))
                                    main_dict[self.cordinate_chip][8] += 1
                                    self.house += 1
                                    if main_dict[self.cordinate_chip][8] == 4:
                                        main_dict[self.cordinate_chip][9] = 1
                                        self.house -= 5
                                        self.hotel += 1
                                screen.fill((0, 0, 0))
                                a = 1
                            if 850 <= event.pos[0] <= 1100 and 500 <= event.pos[1] <= 560:
                                if main_dict[self.cordinate_chip][9] == 1:
                                    main_dict[self.cordinate_chip][8] -= 1
                                    main_dict[self.cordinate_chip][9] = 0
                                    del self.homes[self.color][-1]
                                elif main_dict[self.cordinate_chip][8] != 0:
                                    main_dict[self.cordinate_chip][8] -= 1
                                    del self.homes[self.color][-1]
                                else:
                                    k = main_dict[self.cordinate_chip][5][7:]
                                    main_dict[self.cordinate_chip][5] = k
                                    p = main_dict[self.cordinate_chip][5][
                                        main_dict[self.cordinate_chip][5].index('_') + 1:]
                                    main_dict[self.cordinate_chip][5] = p
                                self.money += main_dict[self.cordinate_chip][7] // 2
                                screen.fill((0, 0, 0))
                                self.print_money()
                                a = 1
                            elif 790 <= event.pos[0] <= 1173 and 640 <= event.pos[1] <= 703:
                                screen.fill((0, 0, 0))
                                self.print_money()
                                a = 1
                    all_draw_pict()
                    pygame.display.flip()
            else:
                time_dict = {10, 11, 12, 13, 14}
                pygame.draw.rect(screen, (0, 0, 0), (176, 56, 448, 608), 0)
                pygame.draw.rect(screen, main_dict[index][6], (180, 60, 440, 600), 0)
                pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 500), 0)
                font_street_name = pygame.font.Font(None, 40)
                street_name = font_street_name.render("{}".format(main_dict[index][4]), True, (0, 0, 0))
                p = (440 - street_name.get_size()[0]) // 2
                screen.blit(street_name, (180 + p, 100))
                font_rent = pygame.font.Font(None, 35)
                rent = font_rent.render("Вы попали на улицу, ", True, (0, 0, 0))
                screen.blit(rent, (270, 210))
                rent = font_rent.render("которой владеет другой игрок", True, (0, 0, 0))
                screen.blit(rent, (210, 235))
                font_rent = pygame.font.Font(None, 40)
                rent = font_rent.render("Заплатите ренту:", True, (0, 0, 0))
                screen.blit(rent, (290, 325))
                if main_dict[self.cordinate_chip][9] == 1:
                    k = 15
                else:
                    k = main_dict[self.cordinate_chip][8] + 10
                font_rent = pygame.font.Font(None, 50)
                rent = font_rent.render("${}".format(main_dict[self.cordinate_chip][k]), True, (0, 0, 0))
                p = (180 - rent.get_size()[0]) // 2
                screen.blit(rent, (310 + p, 365))
                pygame.draw.rect(screen, "black", (306, 670, 188, 58), 0)
                pygame.draw.rect(screen, (255, 255, 255), (310, 674, 180, 50), 0)
                pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 4), 0)
                font_oplata = pygame.font.Font(None, 40)
                oplata = font_oplata.render("ОПЛАТИТЬ", True, "black")
                p = (180 - oplata.get_size()[0]) // 2
                screen.blit(oplata, (310 + p, 687))
                pygame.draw.line(screen, (0, 0, 0), (180, 160), (620, 160), 4)
                while a != 1:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 306 <= event.pos[0] <= 494 and 670 <= event.pos[1] <= 728:
                                if self.money >= int(main_dict[self.cordinate_chip][k]):
                                    self.money -= int(main_dict[self.cordinate_chip][k])
                                    f = main_dict[self.cordinate_chip][5].index('_')
                                    h = main_dict[self.cordinate_chip][5][f + 1:]
                                    for q in sp_rent:
                                        if h[:h.index('_')].lower() == q:
                                            sp_rent[q] += int(main_dict[self.cordinate_chip][k])
                                    self.print_money()
                                    a = 1
                                else:
                                    self.bankrot()
                                    a = 1
                        pygame.display.flip()

    def get_color(self):
        return self.color


chips = []
n = 2
for i in range(n):
    if i == 0:
        chips.append(Chip((20, 40), 'red', i + 1, 15))
    elif i == 1:
        chips.append(Chip((20, 60), 'blue', i + 1, 40))
    elif i == 2:
        chips.append(Chip((40, 40), 'orange', i + 1, 65))
    else:
        chips.append(Chip((40, 60), 'green', i + 1, 90))


def all_draw_pict():
    for i in chips:
        i.draw()


sp_predpr = {'red': 0, 'blue': 0, 'orange': 0, 'green': 0}
sp_railroads = {'red': 0, 'blue': 0, 'orange': 0, 'green': 0}
sp_rent = {'red': 0, 'blue': 0, 'orange': 0, 'green': 0}
go_to_jail = {'red': 0, 'blue': 0, 'orange': 0, 'green': 0}
count = 0
changer = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if go_to_jail[chips[changer].get_color()] == 1:
            go_to_jail[chips[changer].get_color()] = 0
            changer += 1
            if changer >= len(chips):
                changer = 0
        elif go_to_jail[chips[changer].get_color()] == 0 and event.type == pygame.MOUSEBUTTONDOWN:
            k = len(chips)
            if 1110 >= event.pos[0] >= 840 and 700 >= event.pos[1] >= 640:
                num = (random.randint(1, 6), random.randint(1, 6))
                if num[0] == num[1]:
                    count += 1
                else:
                    count = 0
                chips[changer].step(num)
                if num[0] != num[1]:
                    changer += 1
                    if changer >= len(chips):
                        changer = 0
                    count = 0
                elif count == 3:
                    changer += 1
                    if changer >= len(chips):
                        changer = 0
                    count = 0
                for i in sp_rent:
                    if sp_rent[i] != 0:
                        for j in chips:
                            if j.get_color() == i:
                                j.money += sp_rent[i]
                        sp_rent[i] = 0
            if k > len(chips) and changer != 0:
                changer -= 1
            if len(chips) == 1:
                pygame.draw.rect(screen, (60, 170, 60), (174, 54, 452, 612), 0)
                pygame.draw.rect(screen, (255, 255, 255), (180, 60, 440, 600), 0)
                font = pygame.font.Font(None, 50)
                t = font.render("Игрок {} победил!".format(chips[0].get_color()), True, "black")
                screen.blit(t, (225, 210))
                pygame.draw.rect(screen, chips[0].get_color(), (194, 668, 412, 62), 0)
                pygame.draw.rect(screen, (255, 255, 255), (200, 674, 400, 50), 0)
                font = pygame.font.Font(None, 60)
                t = font.render("Закончить игру", True, "black")
                screen.blit(t, (240, 680))
                all_sprites = pygame.sprite.Group()
                image = load_image("win.png")
                monop = pygame.sprite.Sprite(all_sprites)
                monop.image = image
                monop.rect = monop.image.get_rect()
                monop.rect.x = 200
                monop.rect.y = 300
                all_sprites.draw(screen)
                b = 0
                while b != 1:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 194 <= event.pos[0] <= 606 and 668 <= event.pos[1] <= 730:
                                b = 1
                    pygame.display.flip()
                running = False

    pygame.draw.rect(screen, 'white', (840, 640, 270, 60))
    pygame.draw.rect(screen, 'darkgrey', (840, 640, 270, 60), 3)
    all_sprites.draw(screen)
    f3 = pygame.font.Font(None, 34)
    text3 = f3.render('Бросить кубики', True, (0, 0, 0))
    screen.blit(text3, (880, 658))
    all_draw_pict()
    pygame.display.flip()
pygame.quit()
