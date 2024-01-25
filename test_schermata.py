import tkinter as tk
from tkinter import simpledialog
import RPi.GPIO as gpio
import time
import pygame

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(10, gpio.IN, pull_up_down=gpio.PUD_DOWN)

pygame.mixer.init()
pygame.mixer.music.load("sirena.mp3")


PASSWORD_CORRETTA = "password"
timer_stopped = False

def display_time():
    minutes, seconds = divmod(counter, 60)
    label.config(text=f"{minutes:02d}:{seconds:02d}")

def start_countdown():
    global counter, running
    counter = 600  # Durata del countdown in secondi
    running = True
    pygame.mixer.music.play(-1)
    update_label()

def update_label():
    global counter, time_stopped
    if counter > 0 and running and not timer_stopped:
        minutes, seconds = divmod(counter, 60)
        label.config(text=f"{minutes:02d}:{seconds:02d}")
        counter -= 1
        window.after(1000, update_label)
    elif not running and not timer_stopped:
        display_time()
    elif timer_stopped:
        display_time()

def stop_countdown():
    global running
    verifica_password()

def verifica_password():
    password = simpledialog.askstring("Password", "Inserisci la password:", parent=window, show='*')
    if password == PASSWORD_CORRETTA:
        global running
        running = False
        timer_stopped = True
        pygame.mixer.music.stop()
        display_time()
    else:
        label.config(text="Password Errata")

# Configurazione della finestra
window = tk.Tk()
window.title("Autodistruzione")
window.configure(bg="black")
window.geometry("800x600+100+100")  # Larghezza x Altezza + PosX + PosY

label = tk.Label(window, text="Pronto", font=("Arial", 100), fg="red", bg="black")
label.pack(pady=40)

start_button = tk.Button(window, text="Inizia", font=("Arial", 20), command=start_countdown, bg="green", fg="white", height=2, width=10)
start_button.pack(side=tk.LEFT, padx=50)

stop_button = tk.Button(window, text="STOP", font=("Arial", 20), command=stop_countdown, bg="red", fg="white", height=2, width=10)
stop_button.pack(side=tk.RIGHT, padx=50)

counter = 0
running = False  # Variabile per tenere traccia dello stato del countdown


while True:
	if gpio.input(10) == gpio.HIGH:
		print("Button was pushed")
		break
start_countdown()

window.mainloop()
