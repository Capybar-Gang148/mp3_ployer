import pygame
import tkinter as tk
window = tk.Tk()
window.geometry("300x200")

tk.Label(window, text="Top", bg="lightblue").pack(fill="x")
tk.Label(window, text="Middle", bg="lightgreen").pack(fill="both", expand=True)
tk.Label(window, text="Bottom", bg="lightpink").pack(fill="x")
button_row = tk.Frame(window)
button_row.pack(pady=10)

tk.Button(button_row, text="Chupa").pack(side="left", padx=5)
tk.Button(button_row, text="Cancel").pack(side="left", padx=5)

window = tk.Tk()
window.title("Sign Up")

tk.Label(window, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(window)
email_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Button(window, text="Submit").grid(row=2, column=0, columnspan=2, pady=10)

label = tk.Label(
    window,
    text="Welcome!",
    font=("Arial", 18, "bold"),
    fg="white",          # text color
    bg="#2b6cb0",        # background color
    padx=20, pady=10,    # space inside the label
)
label.pack(pady=10)

pygame.mixer.init()
pygame.mixer.music.load("I'm flying highhhhh.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(100)


window.mainloop()