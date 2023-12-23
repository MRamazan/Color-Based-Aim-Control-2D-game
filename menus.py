import pygame as pg
import random
import sys

class start_menu():

    def __init__(self,screen, screen_w, screen_h):
        self.screen_width = screen_w
        self.screen_height = screen_h
        self.screen = screen
    def draw(self):
        pg.init()
        pg.display.set_caption("START MENU")
        pg.draw.rect(self.screen, (0, 255, 0), [(self.screen_width / 2) - 180, (self.screen_height / 2) - 200, 400, 150])
        pg.draw.rect(self.screen, (0, 255, 0), [(self.screen_width / 2) - 180, (self.screen_height / 2) + 100, 400, 150])
        font = pg.font.Font(None, 50)
        metin1 = font.render("START GAME", True, (0, 0, 0))
        metin2 = font.render("EXIT GAME", True, (0, 0, 0))
        self.screen.blit(metin1, (375, 360))
        self.screen.blit(metin2, (375, 660))
        pg.display.update()

class pausemenu():


    def __init__(self,screen, screen_w, screen_h):
        self.screen_width = screen_w
        self.screen_height = screen_h
        self.screen = screen
    def draw(self):
        pg.init()
        pg.display.set_caption("PAUSE MENU")
        pg.draw.rect(self.screen, (0, 255, 0), [(self.screen_width / 2)- 475, (self.screen_height / 2) - 300, 500, 150])
        pg.draw.rect(self.screen, (0, 255, 0), [(self.screen_width / 2) - 475, (self.screen_height / 2)- 100, 500, 150])
        font = pg.font.Font(None, 50)
        metin1 = font.render("CONTINUE GAME", True, (0, 0, 0))
        metin2 = font.render("EXIT GAME", True, (0, 0, 0))
        self.screen.blit(metin1, (80, 260))
        self.screen.blit(metin2, (80, 460))
        pg.display.update()




if __name__ == "__main__":
    x = start_menu(1080, 1000)
    x.draw()

    y = pausemenu(1080, 1000)
    y.draw()


















