import pygame
import tkinter as tk

window = tk.Tk()
window.geometry("300x200")

tk.Label(window, text="Top", bg="lightblue").pack(fill="x")
tk.Label(window, text="Middle", bg="lightgreen").pack(fill="both", expand=True)
tk.Label(window, text="Bottom", bg="lightpink").pack(fill="x")
button_row = tk.Frame(window)
button_row.pack(pady=10)

tk.Button(button_row, text="OK").pack(side="left", padx=5)
tk.Button(button_row, text="Cancel").pack(side="left", padx=5)

window.mainloop()

pygame.mixer.init()
pygame.mixer.music.load("SPOONGE.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(100)
while pygame.mixer.music.get_busy():
    67

