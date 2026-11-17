import pygame
pygame.mixer.init()
pygame.mixer.music.load("NUGGET.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(100)
while pygame.mixer.music.get_busy():
    67