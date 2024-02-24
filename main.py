# import sys module
import pygame
import sys
from random import *

pygame.display.init()
pygame.font.init()

pygame.display.set_caption("nomina cadentia")
clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 600])
base_font = pygame.font.SysFont("arial", 28, True)
user_text = ""
color = pygame.Color(255, 255, 255)
schrift = pygame.font.SysFont("arial", 17, True)
schrift2 = pygame.font.SysFont("arial", 90, True)
schrift3 = pygame.font.SysFont("arial", 50, True)
schrift4 = pygame.font.SysFont("arial", 17, True)
schrift5 = pygame.font.SysFont("arial", 12, True)
input_rect = pygame.Rect(240, 550, 140, 32)
punkte_rect = pygame.Rect(450, 550, 40, 32)
punkte = 0
hit = 0
o = False
a = False
d = False
z = False
oo = False
aa = False
dd = False
zz = False
highscore = 0

fragen = (("Nom. Sg.", "dominus "), ("Gen. Sg.", "domini "), ("Dat. Sg.", "domino "), ("Akk. Sg.", "dominum "),
          ("Abl. Sg.", "domino "), ("Nom. Pl.", "domini "), ("Gen. Pl.", "dominorum "), ("Dat. Pl.", "dominis "),
          ("Akk. Pl.", "dominos "), ("Abl. Pl.", "dominis "))
aDekl = (("Nom. Sg.", "serva "), ("Gen. Sg.", "servae "), ("Dat. Sg.", "servae "), ("Akk. Sg.", "servam "),
         ("Abl. Sg.", "serva "), ("Nom. Pl.", "servae "), ("Gen. Pl.", "servarum "), ("Dat. Pl.", "servis "),
         ("Akk. Pl.", "servas "), ("Abl. Pl.", "servis "))
dDekl = (("Nom. Sg.", "senator "), ("Gen. Sg.", "senatoris "), ("Dat. Sg.", "senatori "), ("Akk. Sg.", "senatorem "),
         ("Abl. Sg.", "senatore "), ("Nom. Pl.", "senatores "), ("Gen. Pl.", "senatorum "),
         ("Dat. Pl.", "senatoribus "), ("Akk. Pl.", "senatores "), ("Abl. Pl.", "senatoribus "))


class Kometen:
    def __init__(self, colour, frage, antwort, textfarbe):
        self.colour = colour
        self.x = randrange(50, 570, 80)
        self.y = randrange(-900, 50, 80)
        speedlist = [0.3, 0.4, 0.5]
        self.speed = choice(speedlist)
        self.radius = 40
        self.frage = frage
        self.antwort = antwort
        self.textfarbe = textfarbe

        self.text = schrift.render(self.frage, True, self.textfarbe)

    def fallen(self):
        global hit
        self.y += self.speed
        if self.y >= 500:
            self.y = -100
            self.y += self.speed
            if self.speed >= 0.4:
                self.speed -= 0.2
            hit -= 1

    def beantworten(self, hoehe):
        global punkte
        global user_text
        if self.y >= 0:
            if user_text == self.antwort:
                kopieformenliste = formenliste.copy()
                p = kopieformenliste.index(self)
                del kopieformenliste[p]
                for kasus in kopieformenliste:
                    if kasus.antwort == self.antwort:
                        if kasus.y > self.y:
                            kasus.y = hoehe
                            if kasus.speed <= 1.5:
                                kasus.speed += 0.1
                            punkte += 1
                            user_text = ""
                        else:
                            self.y = hoehe
                            if self.speed <= 1.5:
                                self.speed += 0.1
                            punkte += 1
                            user_text = ""
                if user_text == self.antwort:
                    self.y = hoehe
                    if self.speed <= 2:
                        self.speed += 0.1
                    punkte += 1
                    user_text = ""

    def zeichnen(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)
        screen.blit(self.text, (self.x - 30, self.y - 10))


comet1 = Kometen((238, 105, 58), fragen[0][0], fragen[0][1], (71, 31, 106))
comet2 = Kometen((238, 105, 58), fragen[1][0], fragen[1][1], (71, 31, 106))
comet3 = Kometen((238, 105, 58), fragen[2][0], fragen[2][1], (71, 31, 106))
comet4 = Kometen((238, 105, 58), fragen[3][0], fragen[3][1], (71, 31, 106))
comet5 = Kometen((238, 105, 58), fragen[4][0], fragen[4][1], (71, 31, 106))
comet6 = Kometen((238, 105, 58), fragen[5][0], fragen[5][1], (71, 31, 106))
comet7 = Kometen((238, 105, 58), fragen[6][0], fragen[6][1], (71, 31, 106))
comet8 = Kometen((238, 105, 58), fragen[7][0], fragen[7][1], (71, 31, 106))
comet9 = Kometen((238, 105, 58), fragen[8][0], fragen[8][1], (71, 31, 106))
comet10 = Kometen((238, 105, 58), fragen[9][0], fragen[9][1], (71, 31, 106))
comet1a = Kometen((206, 215, 224), aDekl[0][0], aDekl[0][1], (5, 69, 105))
comet2a = Kometen((206, 215, 224), aDekl[1][0], aDekl[1][1], (5, 69, 105))
comet3a = Kometen((206, 215, 224), aDekl[2][0], aDekl[2][1], (5, 69, 105))
comet4a = Kometen((206, 215, 224), aDekl[3][0], aDekl[3][1], (5, 69, 105))
comet5a = Kometen((206, 215, 224), aDekl[4][0], aDekl[4][1], (5, 69, 105))
comet6a = Kometen((206, 215, 224), aDekl[5][0], aDekl[5][1], (5, 69, 105))
comet7a = Kometen((206, 215, 224), aDekl[6][0], aDekl[6][1], (5, 69, 105))
comet8a = Kometen((206, 215, 224), aDekl[7][0], aDekl[7][1], (5, 69, 105))
comet9a = Kometen((206, 215, 224), aDekl[8][0], aDekl[8][1], (5, 69, 105))
comet10a = Kometen((206, 215, 224), aDekl[9][0], aDekl[9][1], (5, 69, 105))
comet1d = Kometen((161, 206, 63), dDekl[0][0], dDekl[0][1], (16, 126, 87))
comet2d = Kometen((161, 206, 63), dDekl[1][0], dDekl[1][1], (16, 126, 87))
comet3d = Kometen((161, 206, 63), dDekl[2][0], dDekl[2][1], (16, 126, 87))
comet4d = Kometen((161, 206, 63), dDekl[3][0], dDekl[3][1], (16, 126, 87))
comet5d = Kometen((161, 206, 63), dDekl[4][0], dDekl[4][1], (16, 126, 87))
comet6d = Kometen((161, 206, 63), dDekl[5][0], dDekl[5][1], (16, 126, 87))
comet7d = Kometen((161, 206, 63), dDekl[6][0], dDekl[6][1], (16, 126, 87))
comet8d = Kometen((161, 206, 63), dDekl[7][0], dDekl[7][1], (16, 126, 87))
comet9d = Kometen((161, 206, 63), dDekl[8][0], dDekl[8][1], (16, 126, 87))
comet10d = Kometen((161, 206, 63), dDekl[9][0], dDekl[9][1], (16, 126, 87))

oDeklination = [comet1, comet2, comet3, comet4, comet5, comet6, comet7, comet8, comet9, comet10]
aDeklination = [comet1a, comet2a, comet3a, comet4a, comet5a, comet6a, comet7a, comet8a, comet9a, comet10a]
dDeklination = [comet1d, comet2d, comet3d, comet4d, comet5d, comet6d, comet7d, comet8d, comet9d, comet10d]
formenliste = oDeklination + aDeklination + dDeklination


def anleitung(rahmen, hl, scr, scrbg):
    screen.fill(rahmen)
    pygame.draw.rect(screen, scr, (20, 20, 560, 560))
    pygame.draw.rect(screen, scrbg, (100, 100, 400, 400))
    zeile = schrift.render("Meteoriten bedrohen deinen Planeten!", True, scr)
    zeile1 = schrift.render("Nur du kannst den Planeten retten.", True, scr)
    zeile2 = schrift.render("Tippe möglichst schnell die verlangten", True, scr)
    zeile3 = schrift4.render("KASUSFORMEN!", True, hl)
    zeile4 = schrift.render("Drücke am Ende deiner Eingabe die", True, scr)
    zeile5 = schrift4.render("LEERTASTE (space),", True, hl)
    zeile6 = schrift.render("um den Meteoriten zu zerstören.", True, scr)
    zeile7 = schrift.render("Mit der Escape-Taste (esc) kehrst du", True, scr)
    zeile8 = schrift.render("zum Menu zurück.", True, scr)
    zeile9 = schrift.render("Drücke jetzt die Leertaste (space),", True, scr)
    zeile10 = schrift.render("um zu beginnen. Viel Glück!", True, scr)

    screen.blit(zeile, (120, 120))
    screen.blit(zeile1, (120, 150))
    screen.blit(zeile2, (120, 180))
    screen.blit(zeile3, (120, 210))
    screen.blit(zeile4, (120, 240))
    screen.blit(zeile5, (120, 270))
    screen.blit(zeile6, (120, 300))
    screen.blit(zeile7, (120, 360))
    screen.blit(zeile8, (120, 390))
    screen.blit(zeile9, (120, 420))
    screen.blit(zeile10, (120, 450))


def bgzeichnen(bgfarbe, cometfarbe, wort):
    screen.fill(bgfarbe)
    wort = base_font.render(wort, True, cometfarbe)
    screen.blit(wort, (300, 300))


def loss(dekl, farbe):
    global hit
    global punkte
    global user_text
    global menu
    global oo
    global aa
    global dd
    global zz
    global highscore

    if hit <= -5:
        for case in dekl:
            case.speed = 0
        if punkte >= highscore:
            gewinn = schrift2.render("neue", True, farbe)
            screen.blit(gewinn, (80, 190))
            gewinn1 = schrift2.render("highscore!", True, farbe)
            screen.blit(gewinn1, (100, 280))
            user_text = ""
            highscore = punkte
            for eingabe in pygame.event.get():
                if eingabe.type == pygame.QUIT:
                    sys.exit()
                if eingabe.type == pygame.KEYDOWN:
                    if eingabe.key == pygame.K_ESCAPE:
                        oo = False
                        aa = False
                        dd = False
                        zz = False
                        menu = True
                        punkte = 0
                        hit = 0
                        for case in dekl:
                            case.speed = 0.5
                            case.y -= randrange(100, 500, 50)
        else:
            result = schrift2.render("game over", True, farbe)
            screen.blit(result, (80, 190))
            for eingabe in pygame.event.get():
                if eingabe.type == pygame.QUIT:
                    sys.exit()
                if eingabe.type == pygame.KEYDOWN:
                    if eingabe.key == pygame.K_ESCAPE:
                        oo = False
                        aa = False
                        dd = False
                        zz = False
                        menu = True
                        punkte = 0
                        hit = 0
                        for case in dekl:
                            case.speed = 0.5
                            case.y -= randrange(100, 500, 50)
    if punkte >= 100:
        erg = schrift2.render("victoria", True, farbe)
        screen.blit(erg, (80, 190))
        for case in dekl:
            case.speed = 0
        for eingabe in pygame.event.get():
            if eingabe.type == pygame.QUIT:
                sys.exit()
            if eingabe.type == pygame.KEYDOWN:
                if eingabe.key == pygame.K_ESCAPE:
                    oo = False
                    aa = False
                    dd = False
                    zz = False
                    menu = True
                    punkte = 0
                    hit = 0
                    for case in dekl:
                        case.speed = 0.5
                        case.y -= randrange(100, 500, 50)


def entry(dekl):
    global hit
    global punkte
    global menu
    global oo
    global aa
    global dd
    global zz
    global user_text
    for eingabe in pygame.event.get():
        if eingabe.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if eingabe.type == pygame.KEYDOWN:
            if eingabe.key == pygame.K_ESCAPE:
                if punkte >= highscore:
                    hit = -5
                else:
                    oo = False
                    aa = False
                    dd = False
                    zz = False
                    menu = True
                    punkte = 0
                    hit = 0
                    for case in dekl:
                        case.speed = 0.5
                        case.y -= randrange(100, 500, 50)

            if eingabe.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += eingabe.unicode


def fgzeichnen(erdfarbe, eingabefarbe):
    pygame.draw.circle(screen, erdfarbe, (300, 1100), 600)
    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, eingabefarbe)
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(100, text_surface.get_width() + 10)
    pygame.draw.rect(screen, color, punkte_rect)
    punktezaehler = base_font.render(str(punkte), True, eingabefarbe)
    screen.blit(punktezaehler, (punkte_rect.x + 5, punkte_rect.y + 5))


go = True
while go:

    o = False
    a = False
    d = False

    menu = True
    while menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                if event.key == pygame.K_o:
                    o = True
                    menu = False
                    user_text = ""
                if event.key == pygame.K_a:
                    a = True
                    menu = False
                    user_text = ""
                if event.key == pygame.K_3:
                    d = True
                    menu = False
                    user_text = ""
                if event.key == pygame.K_z:
                    z = True
                    menu = False
                    user_text = ""

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (164, 67, 34), (70, 70, 430, 430))
        pygame.draw.rect(screen, (248, 188, 4), (90, 90, 410, 410))
        pygame.draw.rect(screen, (5, 20, 39), (100, 100, 400, 400))
        pygame.draw.rect(screen, (83, 15, 30), (150, 150, 320, 320))
        text = schrift.render("Welche Deklination möchtest du lernen?", True, (248, 188, 4))
        text1 = schrift.render("Drücke o für o-Deklination", True, (248, 188, 4))
        text2 = schrift.render("Drücke a für a-Deklination", True, (248, 188, 4))
        text3 = schrift.render("Drücke 3 für 3. Deklination", True, (248, 188, 4))
        text4 = schrift.render("Drücke z für alle Deklinationen", True, (248, 188, 4))
        screen.blit(text, (120, 120))
        screen.blit(text1, (160, 200))
        screen.blit(text2, (160, 260))
        screen.blit(text3, (160, 320))
        screen.blit(text4, (160, 380))

        pygame.display.flip()

    while o:

        anleitung((238, 105, 58), (238, 105, 58), (42, 10, 79), (238, 171, 65))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    o = False
                    oo = True
                if event.key == pygame.K_ESCAPE:
                    o = False
                    menu = True

        pygame.display.flip()

    while oo:

        bgzeichnen((42, 10, 79), (238, 105, 58), "dominus")

        for form in oDeklination:
            form.fallen()
            form.beantworten(randrange(-1000, -800))
            form.zeichnen()

        fgzeichnen((238, 171, 65), (238, 105, 58))
        loss(oDeklination, (238, 171, 65))
        entry(oDeklination)

        pygame.display.flip()
        clock.tick(60)

    while a:

        anleitung((206, 215, 224), (5, 69, 105), (6, 44, 67), (156, 205, 220))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    a = False
                    aa = True
                if event.key == pygame.K_ESCAPE:
                    a = False
                    menu = True

        pygame.display.flip()

    while aa:

        bgzeichnen((6, 44, 67), (206, 215, 224), "serva")

        for form in aDeklination:
            form.fallen()
            form.beantworten(randrange(-1000, -800))
            form.zeichnen()

        fgzeichnen((156, 205, 220), (5, 69, 105))
        loss(aDeklination, (156, 205, 220))
        entry(aDeklination)

        pygame.display.flip()
        clock.tick(60)

    while d:

        anleitung((161, 206, 63), (1, 71, 96), (1, 48, 38), (203, 229, 142))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    d = False
                    dd = True
                if event.key == pygame.K_ESCAPE:
                    d = False
                    menu = True

        pygame.display.flip()

    while dd:

        bgzeichnen((1, 48, 38), (161, 206, 63), "senator")

        for form in dDeklination:
            form.fallen()
            form.beantworten(randrange(-1000, -800))
            form.zeichnen()

        fgzeichnen((203, 229, 142), (1, 71, 96))
        loss(dDeklination, (203, 229, 142))
        entry(dDeklination)

        pygame.display.flip()
        clock.tick(60)

    while z:

        anleitung((161, 206, 63), (238, 105, 58), (42, 10, 79), (206, 215, 224))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    z = False
                    zz = True
                if event.key == pygame.K_ESCAPE:
                    z = False
                    menu = True

        for form in formenliste:
            form.y = randrange(-3000, 50, 80)

        pygame.display.flip()

    while zz:

        bgzeichnen((42, 10, 79), (238, 105, 58), "dominus")
        serva = base_font.render("serva", True, (206, 215, 224))
        screen.blit(serva, (300, 325))
        senator = base_font.render("senator", True, (161, 206, 63))
        screen.blit(senator, (300, 350))

        for form in oDeklination:
            form.fallen()
            form.beantworten(randrange(-3500, -2500))
            form.zeichnen()
            grundwort = schrift5.render("dominus", True, form.textfarbe)
            screen.blit(grundwort, (form.x - 20, form.y + 15))

        for form in aDeklination:
            form.fallen()
            form.beantworten(randrange(-3500, -2500))
            form.zeichnen()
            grundwort = schrift5.render("serva", True, form.textfarbe)
            screen.blit(grundwort, (form.x - 15, form.y + 15))

        for form in dDeklination:
            form.fallen()
            form.beantworten(randrange(-3500, -2500))
            form.zeichnen()
            grundwort = schrift5.render("senator", True, form.textfarbe)
            screen.blit(grundwort, (form.x - 20, form.y + 15))

        fgzeichnen((206, 215, 224), (42, 10, 79))
        loss(formenliste, (206, 215, 224))
        entry(formenliste)

        pygame.display.flip()
        clock.tick(60)
