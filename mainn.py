import threading
import cv2
import numpy as np
import pygame as pg
import random
from multiprocessing import Manager
from multiprocessing import Process, Value

import ammoscoreaccuracy
import encounters
import sounds
import menus


class red_detect():
    def __init__(self, manager_list):
        self.manager_list = manager_list


    def masking(self):
        cap = cv2.VideoCapture(0)
        while True:
            _, frame = cap.read()

            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Red color
            low_red = np.array([161, 155, 84])
            high_red = np.array([179, 255, 255])
            red_mask = cv2.inRange(hsv_frame, low_red, high_red)
            red = cv2.bitwise_and(frame, frame, mask=red_mask)

            # Every color except white


            cv2.imshow("Red", red)
            contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if cv2.contourArea(contour) > 100:
                    mo_x, mo_y, w, h = cv2.boundingRect(contour)

                    cv2.rectangle(red, (mo_x, mo_y), (mo_x + w, mo_y + h), (0, 255, 0), 2)
                    # Listeye ekleyin
                    self.manager_list[0] = mo_x
                    self.manager_list[1] = mo_y

            key = cv2.waitKey(1)
            if key == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

    def new_enc(self):
        img = pg.transform.scale(pg.image.load(r"C:\Users\PC\Downloads\853b792d9db7c1afed8be8f25694c61d.png"),
                                 (100, 200))
        screen = pg.display.set_mode((1080, 1000))
        enemy_x = random.randint(100, 900)
        enemy_y = random.randint(100, 900)
        screen.blit(img, (enemy_x, enemy_y))
        pg.display.flip()

    def aim(self):
        pg.init()
        img = pg.transform.scale(pg.image.load(r"C:\Users\PC\Downloads\853b792d9db7c1afed8be8f25694c61d.png"),
                                 (100, 200))
        sayac = 0
        while True:
            sayac += 1
            # Listeden okuyun
            mo_x = self.manager_list[0]
            mo_y = self.manager_list[1]


            instance = encounters.enc(img, pg.display.set_mode((1080, 1000)), mo_x, mo_y, sayac)
            instance.main()
            if sayac == 1:
                instance.new_enc()


    def main(self):
        pg.mouse.set_visible(False)
        img = pg.transform.scale(pg.image.load(r"C:\Users\PC\Downloads\853b792d9db7c1afed8be8f25694c61d.png"),
                                 (100, 200))
        screen = pg.display.set_mode((1000, 1000))
        pg.init()
        enemy_x = 500
        enemy_y = 500
        screen.blit(img, (enemy_x, enemy_y))

        shoot = False
        hit_count = 0
        shoot_count = 0
        sound = sounds.sound()


        game = ammoscoreaccuracy.ammo_score_acc(screen)
        font = pg.font.Font(None, 60)
        metin4 = font.render("OUT OF BULLETS", None, (255, 0, 0))

        startmenu = True
        while startmenu:
            pg.mouse.set_visible(True)
            screen.fill((0, 0, 0))
            new_mx, new_my = pg.mouse.get_pos()

            for event4 in pg.event.get():
                if event4.type == pg.MOUSEBUTTONDOWN:
                    if 360 <= new_mx <= 760 and 300 <= new_my <= 450:
                        startmenu = False
                        pg.mouse.set_visible(False)
                    elif 65 <= new_mx <= 565 and 600 <= new_my <= 750:
                        pg.quit()
            strt_menu = menus.start_menu(screen, 1080, 1000)
            strt_menu.draw()

        while True:

            metin = game.ammo(shoot_count, hit_count)
            metin2 = game.score(hit_count)
            metin3 = game.accuracy(shoot_count, hit_count)

            m_x =self.manager_list[0]
            m_y = self.manager_list[1]




            if shoot_count == 30:
                pg.draw.rect(screen, (0, 0, 0), [0, 500, 1000, 100])
                screen.blit(metin4, (300, 520))
                screen.blit(metin, (20, 900))
                screen.blit(metin2, (500, 30))
                screen.blit(metin3, (20, 30))
                pg.display.flip()
                shoot_count = 0
                i = True
                while i:
                    for event2 in pg.event.get():
                        if event2.type == pg.KEYUP:
                            if event2.key == pg.K_r:
                                sound.reload_sound()
                                pg.time.delay(1000)
                                print("lol")
                                screen.fill((0, 0, 0))
                                pg.display.flip()
                                i = False



            if shoot:
                hit_count += 1
                game.score(hit_count)
                enemy_x, enemy_y = random.randint(200, 800), random.randint(200, 800)
                shoot = False
                game.ammo(shoot_count, hit_count)


            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    shoot_count += 1
                    sound.shoot_sound()
                    if enemy_x <= m_x <= enemy_x + 100 and enemy_y <= m_y <= enemy_y + 200:
                        screen.fill((0, 0, 0))
                        shoot = True
                        pg.display.flip()
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_ESCAPE:
                        pg.mouse.set_visible(True)
                        screen.fill((0, 0, 0))
                        menu = True
                        while menu:
                            new_mx, new_my = pg.mouse.get_pos()
                            for event3 in pg.event.get():
                                if event3.type == pg.MOUSEBUTTONDOWN:
                                    if  65 <= new_mx <= 565 and 200 <= new_my <= 350 :
                                        menu = False
                                        pg.mouse.set_visible(False)
                                    elif 65 <= new_mx <= 565 and 400 <= new_my <= 550:
                                        pg.quit()

                            start_menu = menus.pausemenu(screen, 1080, 1000)
                            start_menu.draw()


                    else:
                        print("emaneman")
                        screen.fill((0, 0, 0))
                        self.shoot = False
            screen.fill((0, 0, 0))
            screen.blit(img, (enemy_x, enemy_y))
            screen.blit(metin, (20, 900))
            screen.blit(metin2, (500, 30))
            screen.blit(metin3, (20, 30))



            pg.mouse.set_pos([m_x, m_y])
            pg.draw.rect(screen, (255, 255, 0), [m_x - 2, m_y, 1, 30], 9, 1)
            pg.draw.rect(screen, (255, 255, 0), [m_x - 16, m_y + 15, 30, 1], 9, 1)
            pg.display.update()
            


if __name__ == "__main__":
    with Manager() as manager:
        manager_list = manager.list([0, 0])
        z = red_detect(manager_list)

       
        producer_thread = threading.Thread(target=z.masking)
        producer_thread.start()


        
        consumer_process = Process(target=z.main)
        consumer_process.start()

    
        producer_thread.join()


      
        manager_list[0] = None
        manager_list[1] = None

        consumer_process.join()



