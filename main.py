import os

import pygame
import random

pygame.init()
main_dict = {1:  [650, 650, 100, 100, "GO", "", (255, 255, 255)],
             40: [594, 650, 56, 100, "BOARDWALK", "$400", (70, 130, 180), (50, 100, 200, 600, 1400, 1700, 2000)],
             39: [539, 650, 56, 100, "LUXURY TAX", "PAY $100", (255, 255, 255)],
             38: [482, 650, 56, 100, "PARK PLACE", "$350", (70, 130, 180), (35, 70, 175, 500, 1100, 1300, 1500)],
             37: [426, 650, 56, 100, "CHANCE", "", (255, 255, 255)],
             36: [370, 650, 56, 100, "SHORT LINE", "$200", (255, 255, 255), (25, 50, 100, 200)],
             35: [314, 650, 56, 100, "PENNSYLVANIA AVENUE", "$320", (0, 128, 0), (28, 56, 150, 450, 1000, 1200, 1400)],
             34: [258, 650, 56, 100, "COMMUNITY CHEST", "", (255, 255, 255)],
             33: [202, 650, 56, 100, "NORTH CAROLINA AVENUE", "$300", (0, 128, 0), (26, 52, 130, 390, 900, 1100, 1275)],
             32: [150, 650, 52, 100, "PACIFIC AVENUE", "$300", (0, 128, 0), (26, 52, 130, 390, 900, 1100, 1275)],
             31: [50, 650, 100, 100, "GO TO JAIL", "", (255, 255, 255)],
             30: [50, 594, 100, 56, "MARVIN GARDENS", "$280", (255, 255, 0), (24, 48, 120, 360, 850, 1025, 1200)],
             29: [50, 539, 100, 56, "WATER WORKS", "$150", (255, 255, 255)],
             28: [50, 482, 100, 56, "VENTNOR AVENUE", "$260", (255, 255, 0), (22, 44, 110, 330, 800, 975, 1150)],
             27: [50, 426, 100, 56, "ATLANTIC AVENUE", "$260", (255, 255, 0), (22, 44, 110, 330, 800, 975, 1150)],
             26: [50, 370, 100, 56, "B. & O. RAILROAD", "$200", (255, 255, 255), (25, 50, 100, 200)],
             25: [50, 314, 100, 56, "ILLINOIS AVENUE", "$240", (255, 0, 0), (20, 40, 100, 300, 750, 925, 1100)],
             24: [50, 258, 100, 56, "INDIANA AVENUE", "$220", (255, 0, 0), (18, 36, 90, 250, 700, 875, 1050)],
             23: [50, 202, 100, 56, "CHANCE", "", (255, 255, 255)],
             22: [50, 150, 100, 52, "KENTUCKY AVENUE", "$220", (255, 0, 0), (18, 36, 90, 250, 700, 875, 1050)],
             21: [50, 50, 100, 100, "FREE PARKING", "", (255, 255, 255)],
             20: [150, 50, 56, 100, "NEW YORK AVENUE", "$200", (255, 140, 0), (16, 32, 80, 220, 600, 800, 1000)],
             19: [206, 50, 56, 100, "TENNESSEE AVENUE", "$180", (255, 140, 0), (14, 28, 70, 200, 550, 750, 950)],
             18: [262, 50, 56, 100, "COMMUNITY CHEST", "", (255, 255, 255)],
             17: [318, 50, 56, 100, "ST. JAMES PLACE", "$180", (255, 140, 0), (14, 28, 70, 200, 550, 750, 950)],
             16: [374, 50, 56, 100, "PENNSYLVANIA RAILROAD", "$200", (255, 255, 255), (25, 50, 100, 200)],
             15: [430, 50, 56, 100, "VIRGINIA AVENUE", "$160", (199, 21, 133), (12, 24, 60, 180, 500, 700, 900)],
             14: [486, 50, 56, 100, "STATES AVENUE", "$140", (199, 21, 133), (10, 20, 50, 150, 450, 625, 750)],
             13: [542, 50, 56, 100, "ELECTRIC COMPANY", "$150", (255, 255, 255)],
             12: [596, 50, 54, 100, "ST. CHARLES PLACE", "$140", (199, 21, 133), (10, 20, 50, 150, 450, 625, 750)],
             11: [650, 50, 100, 100, "JUST VISITING", "", (255, 255, 255)],
             10: [650, 150, 100, 56, "CONNECTICUT AVENUE", "$120", (175, 238, 238), (8, 16, 40, 100, 300, 450, 600)],
             9:  [650, 206, 100, 56, "VERMONT AVENUE", "$100", (175, 238, 238), (6, 12, 30, 90, 270, 400, 550)],
             8:  [650, 262, 100, 56, "CHANCE", "", (255, 255, 255)],
             7:  [650, 318, 100, 56, "ORIENTAL AVENUE", "$100", (175, 238, 238), (6, 12, 30, 90, 270, 400, 550)],
             6:  [650, 374, 100, 56, "READING RAILROAD", "$200", (255, 255, 255), (25, 50, 100, 200)],
             5:  [650, 430, 100, 56, "INCOME TAX", "PAY $200", (255, 255, 255)],
             4:  [650, 486, 100, 56, "BALTIC AVENUE", "$60", (77, 34, 14), (4, 8, 20, 60, 180, 320, 450)],
             3:  [650, 542, 100, 56, "COMMUNITY CHEST", "", (255, 255, 255)],
             2:  [650, 596, 100, 54, "MEDITERRANEAN AVENUE", "$60", (77, 34, 14), (2, 4, 10, 30, 90, 160, 250)],
             'main': (320, 320, 180, 180)
             }

chest_dict = dict()
for i, x in enumerate(open('data/chest.txt', encoding='utf-8')):
    chest_dict[i] = x[:-1]
num_chest = list(range(len(chest_dict)))
random.shuffle(num_chest)
n = 0


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
screen.fill(pygame.Color("black"))
running = True
changer = 0


class Chip:
    def __init__(self, ident, color, number_person, prison):
        self.cordinate_chip = 1
        self.ident = ident
        self.prison = prison
        self.color = color
        self.number = number_person
        self.go_to_jail = 0
        self.x = main_dict[self.cordinate_chip][0] + self.ident[0]
        self.y = main_dict[self.cordinate_chip][0] + self.ident[1]
        self.count = 0
        self.money = 1500
    
    def print_money(self, money, color, cor=(900, 50)):
        t = pygame.font.Font(None, 50)
        text = t.render(f'Деньги: ${money}', False, pygame.Color(color))
        screen.blit(text, cor)

    def draw(self):
        pygame.draw.circle(screen, pygame.Color(self.color), (self.x, self.y), 10, 0)

    def step(self, num):
        global changer
        screen.fill((0, 0, 0))
        self.print_money(self.money, self.color)
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
            if self.go_to_jail > 0:
                pass
            else:
                for i in range(sum(num)):
                    all_sprites.draw(screen)
                    self.cordinate_chip += 1
                    if self.cordinate_chip > 40:
                        screen.fill((0, 0, 0))
                        all_sprites.draw(screen)
                        self.print_money(self.money, self.color)
                        self.cordinate_chip = 1
                    if 21 >= self.cordinate_chip > 11:
                        self.x = main_dict[self.cordinate_chip][1] + self.ident[0]
                        self.y = main_dict[self.cordinate_chip][0] + self.ident[1] - 30
                    elif 40 > self.cordinate_chip > 31:
                        self.x = main_dict[self.cordinate_chip][1] + self.ident[0] + 30
                        self.y = main_dict[self.cordinate_chip][0] + self.ident[1] - 20
                    elif self.cordinate_chip == 11:
                        self.x = main_dict[11][1] + 10
                        self.y = main_dict[11][0] + self.prison
                    else:
                        self.x = main_dict[self.cordinate_chip][1] + self.ident[0]
                        self.y = main_dict[self.cordinate_chip][0] + self.ident[1]
                    all_draw_pict()
                    clock.tick(5)
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
        text_chest = fort_chest.render(chest_dict[n], True, (0, 0, 0))
        text_chest_x = width // 2 - text_chest.get_width() // 2
        text_chest_y = text_cc_y + text_cc.get_height() + ((text_ok_y - 10 - (text_cc_y + text_cc.get_height()))
                                                           // 2 - text_chest.get_height() // 2)
        screen.blit(text_chest, (text_chest_x, text_chest_y))
        while a != 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if text_ok_x - 20 + text_ok_w + 40 >= event.pos[0] >= text_ok_x - 20 and \
                            text_ok_y - 10 + text_ok_h + 20 >= event.pos[1] >= text_ok_y - 10:
                        screen.fill((0, 0, 0))
                        self.print_money(self.money, self.color)
                        a = 1
            pygame.display.flip()

    def chance(self):
        a = 0
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
        fort_cc = pygame.font.Font(None, 60)
        text_cc = fort_cc.render("Шанс:", True, (0, 0, 0))
        text_cc_x = width // 2 - text_cc.get_width() // 2
        text_cc_y = 230
        screen.blit(text_cc, (text_cc_x, text_cc_y))
        fort_chest = pygame.font.Font(None, 40)
        text_chest = fort_chest.render(chest_dict[n], True, (0, 0, 0))
        text_chest_x = width // 2 - text_chest.get_width() // 2
        text_chest_y = text_cc_y + text_cc.get_height() + ((text_ok_y - 10 - (text_cc_y + text_cc.get_height()))
                                                           // 2 - text_chest.get_height() // 2)
        screen.blit(text_chest, (text_chest_x, text_chest_y))
        while a != 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if text_ok_x - 20 + text_ok_w + 40 >= event.pos[0] >= text_ok_x - 20 and \
                            text_ok_y - 10 + text_ok_h + 20 >= event.pos[1] >= text_ok_y - 10:
                        screen.fill((0, 0, 0))
                        self.print_money(self.money, self.color)
                        a = 1
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
            pygame.draw.rect(screen, (0, 0, 0), (176, 56, 448, 608), 0)
            pygame.draw.rect(screen, main_dict[index][6], (180, 60, 440, 600), 0)
            pygame.draw.rect(screen, (255, 255, 255), (180, 160, 440, 500), 0)
            font_street_name = pygame.font.Font(None, 40)
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
            all_sprites = pygame.sprite.Group()
            image = load_image("{}.png".format(picture))
            pict = pygame.sprite.Sprite(all_sprites)
            pict.image = image
            pict.rect = pict.image.get_rect()
            pict.rect.x = 300
            pict.rect.y = 250
            all_sprites.draw(screen)
            if main_dict[index][4] == "INCOME TAX" or main_dict[index][4] == "LUXURY TAX":
                while a != 1:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 306 <= event.pos[0] <= 494 and 670 <= event.pos[1] <= 728:
                                if self.money >= int(main_dict[self.cordinate_chip][5][5:]):
                                    screen.fill((0, 0, 0))
                                    self.money -= int(main_dict[self.cordinate_chip][5][5:])
                                    self.print_money(self.money, self.color)
                                    a = 1
                                else:
                                    chips.pop(self.number - 1)
                                    a = 1
                                    # ВЫВОД О ПРОИГРЫШЕ ИГРОКА
                            
                    pygame.display.flip()
            else:
                while a != 1:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 196 <= event.pos[0] <= 384 and 670 <= event.pos[1] <= 728:
                                if main_dict[self.cordinate_chip][5][:6] != 'BOUGHT' and self.money >= int(main_dict[self.cordinate_chip][5][1:]):
                                    self.money -= int(main_dict[self.cordinate_chip][5][1:])
                                    main_dict[self.cordinate_chip][5] = 'BOUGHT_' + str(self.number)
                                    screen.fill((0, 0, 0))
                                    self.print_money(self.money, self.color)
                                    a = 1
                                else:
                                    pass
                                    a = 1
                                    # Красная табличка на счёт денег
                            elif 416 <= event.pos[0] <= 604 and 670 <= event.pos[1] <= 728:
                                screen.fill((0, 0, 0))
                                a = 1
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
                            if self.go_to_jail == 0:
                                self.go_to_jail += 1
                                self.x = main_dict[11][1] + self.ident[0] + 30
                                self.y = main_dict[11][0] + self.ident[1]
                                screen.fill((0, 0, 0))
                            else:
                                self.go_to_jail = 0
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
                screen.blit(price, (180 + p, 600))
                font_pokupka = pygame.font.Font(None, 40)
                kupit = font_pokupka.render("КУПИТЬ", True, "green")
                font_pokupka = pygame.font.Font(None, 30)
                nekupit = font_pokupka.render("НЕ ПОКУПАТЬ", True, "red")
                p = (180 - kupit.get_size()[0]) // 2
                screen.blit(kupit, (200 + p, 685))
                p = (180 - nekupit.get_size()[0]) // 2
                screen.blit(nekupit, (420 + p, 690))
                while a != 1:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 196 <= event.pos[0] <= 384 and 670 <= event.pos[1] <= 728:
                                if self.money > int(main_dict[self.cordinate_chip][5][1:]):
                                    self.money -= int(main_dict[self.cordinate_chip][5][1:])
                                    main_dict[self.cordinate_chip][5] = 'BOUGHT_' + str(self.number)
                                    screen.fill((0, 0, 0))
                                    self.print_money(self.money, self.color)
                                else:
                                    pass
                                    # Красная табличка на счёт денег
                                a = 1
                            elif 416 <= event.pos[0] <= 604 and 670 <= event.pos[1] <= 728:
                                screen.fill((0, 0, 0))
                                self.print_money(self.money, self.color)
                                a = 1
                    pygame.display.flip()
            else:
                t = pygame.font.Font(None, 50)
                text = t.render(f'Налог: ${main_dict[self.cordinate_chip][7][0]}', False, pygame.Color('yellow'))
                screen.fill((0, 0, 0))
                screen.blit(text, (900, 150))
                self.money -= int(main_dict[self.cordinate_chip][7][0])
                print(self.money)
                enemy = chips[int(main_dict[self.cordinate_chip][5][7]) - 1]
                enemy.money += int(main_dict[self.cordinate_chip][7][0])
                print(self.money)
                self.print_money(self.money, self.color)
                self.print_money(enemy.money, enemy.color, (900, 100))


chips = []
n = 2
for i in range(n):
    if i == 0:
        chips.append(Chip((20, 40), 'red', i + 1, 15))
    elif i == 1:
        chips.append(Chip((20, 60), 'blue', i + 1, 40))
    elif i == 2:
        chips.append(Chip((40, 40), 'yellow', i + 1, 65))
    else:
        chips.append(Chip((40, 60), 'green', i + 1, 90))


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
pygame.quit()
