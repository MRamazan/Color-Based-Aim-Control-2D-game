import pygame as pg
class sound():
    def shoot_sound(self):
        pg.mixer.init()
        reload_sound = r"sounds\Gun shoot - Sound effect.mp3"
        pg.mixer.music.load(reload_sound)
        return pg.mixer.music.play()

    def reload_sound(self):
        pg.mixer.init()
        reload_sound = r"sounds\Gun Reload sound effect (1).mp3"
        pg.mixer.music.load(reload_sound)
        return pg.mixer.music.play()

if __name__ == "__main__":
   print("l")
