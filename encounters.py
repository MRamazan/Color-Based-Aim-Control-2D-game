import pygame as pg
import random
pg.init()

class enc():
   def __init__(self, img, screen,m_x, m_y, sayı):
    self.img = img
    self.screen = screen
    self.enemy_x = 0
    self.enemy_y = 0
    self.m_y = m_y
    self.m_x = m_x
    self.sayı = sayı
    self.shoot = False
   def new_enc(self):
         self.enemy_x = random.randint(100, 900)
         self.enemy_y = random.randint(100, 900)
         self.screen.blit(self.img, (self.enemy_x, self.enemy_y))
         pg.display.flip()
   def condition(self, x):
       pg.init()
       if self.shoot == False and self.sayı >= 1 and x == True:
           self.screen.fill((0, 0, 0))
           self.enemy_x = 500
           self.enemy_y = 500
           self.screen.blit(self.img, (self.enemy_x, self.enemy_y))
           pg.display.flip()


   def main(self):
     pg.init()
     self.new_enc()

     while True:
       for event in pg.event.get():
         if event.type == pg.QUIT:
            pg.quit()
         elif event.type == pg.MOUSEBUTTONDOWN:
            if self.enemy_x <= self.m_x <= self.enemy_x + 100 and self.enemy_y <= self.m_y <= self.enemy_y + 200:
              self.enemy_x = random.randint(100, 800)
              self.enemy_y = random.randint(100, 800)
              self.screen.fill((0, 0, 0))
              self.new_enc()
              self.shoot = False
              print(self.shoot)
              pg.display.flip()

            else:
                print("emaneman")
                self.shoot = False


       pg.init()
       pg.mouse.set_pos([self.m_x, self.m_y])
       pg.draw.rect(self.screen, (255, 255, 0), [self.m_x - 2, self.m_y, 1, 30], 9, 1)
       pg.draw.rect(self.screen, (255, 255, 0), [self.m_x - 16, self.m_y + 15, 30, 1], 9, 1)
       pg.display.update()
       pg.time.Clock().tick(60)
       break




if __name__ == "__main__":
    img = pg.transform.scale(pg.image.load(r"C:\Users\PC\Downloads\853b792d9db7c1afed8be8f25694c61d.png"), (100, 200))
    instance = enc(img, pg.display.set_mode((1200, 1000)),random.randint(100, 800),random.randint(100, 800),1)
    instance.main()















