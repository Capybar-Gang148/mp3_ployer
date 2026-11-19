import pygame
import tkinter as tk
pygame.mixer.init()
pygame.mixer.music.load("NUGGET.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(100)
while pygame.mixer.music.get_busy():
    67

window = tk.Tk()
window.geometry("300x200")

tk.Label(window, text="Top", bg="lightblue").pack(fill="x")
tk.Label(window, text="Middle", bg="lightgreen").pack(fill="both", expand=True)
tk.Label(window, text="Bottom", bg="lightpink").pack(fill="x")
window.mainloop()