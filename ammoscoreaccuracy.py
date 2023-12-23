import threading

import pygame as pg

pg.init()

class ammo_score_acc():
    def __init__(self, screen):
        self.screen = screen
        self.bullet = 30


    def ammo(self, shoot, hit):
        pg.init()
        text = ("AMMO // " + str(self.bullet - shoot))
        pg.draw.rect(self.screen, (0, 0, 0), [0, 900, 300, 100])
        font = pg.font.Font(None, 60)
        metin1 = font.render(text, True, (0, 255, 0))
        metin2 = ("OUT OF BULLETS", None, (255, 0, 0))

        return metin1


    def score(self, hit):
        pg.init()
        score = "SCORE // " + str(hit)
        pg.draw.rect(self.screen, (0, 0, 0), [0, 0, 1080, 100])
        font = pg.font.Font(None, 60)
        metin1 = font.render(score, True, (0, 255, 0))
        return metin1




    def accuracy(self, shoot_c, hit):
        pg.init()
        if shoot_c == 0 or hit == 0:
            acc_text = "ACCURACY // 0"
        else:
            accuracy = hit / shoot_c
            fixed_accuracy = round(accuracy, 2)
            acc_text = "ACCURACY // " + str(fixed_accuracy)
        pg.draw.rect(self.screen, (0, 0, 0), [0, 0, 1080, 100])
        font = pg.font.Font(None, 60)
        metin1 = font.render(acc_text, True, (0, 255, 0))
        return metin1




if __name__ == "__main__":
    thread1 = threading.Thread(target=x.ammo)
    thread2 = threading.Thread(target=x.score)
    thread3 = threading.Thread(target=x.accuracy)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()


