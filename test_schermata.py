import tkinter as tk
from tkinter import simpledialog
import RPi.GPIO as gpio
import time
import pygame

# Impostazioni GPIO, suono e variabili globali
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(10, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(11, gpio.OUT)
gpio.setup(40, gpio.OUT)

gpio.output(40, gpio.LOW)

p = gpio.PWM(11, 50)
p.start(0)

current_duty_cycle = 0

pygame.mixer.init()
pygame.mixer.music.load("sirena.mp3")

PASSWORD_CORRETTA = "password"
timer_stopped = False  # Inizializza la variabile timer_stopped a False

# Funzioni per l'interfaccia utente e il controllo del servo

def resize_elements(event=None):
    button_height = int(window.winfo_height() / 5)
    button_width = int(window.winfo_width() / 5)
    font_size = int(button_height / 5)

    label.config(font=("Helvetica", font_size))
    stop_button.config(font=("Helvetica", font_size), height=button_height, width=button_width)
    save_button.config(font=("Helvetica", font_size), height=button_height, width=button_width)

def display_time():
    minutes, seconds = divmod(counter, 60)
    label.config(text=f"{minutes:02d}:{seconds:02d}", fg="#FF0000", bg="#000000")  # Aggiorna solo il testo

def start_countdown():
    global counter, running, timer_stopped
    counter = 600
    running = True
    timer_stopped = False  # Imposta timer_stopped a False quando inizia il countdown
    pygame.mixer.music.play(-1)
    update_label()

def update_label():
    global counter, timer_stopped
    if counter > 0 and not timer_stopped:
        minutes, seconds = divmod(counter, 60)
        label.config(text=f"{minutes:02d}:{seconds:02d}")
        counter -= 1
        window.after(1000, update_label)
        display_time()
    elif timer_stopped:
        display_time()

def stop_countdown():
    global running
    verifica_password()

def verifica_password():
    password = simpledialog.askstring("Password", "Inserisci la password:", parent=window, show='*')
    if password == PASSWORD_CORRETTA:
        global running, counter, timer_stopped
        running = False
        timer_stopped = True
        pygame.mixer.music.stop()
        display_time()
        stop_button.pack_forget()
        save_button.pack_forget()
    else:
        label.config(text="Password Errata")

def move_servo(target_duty_cycle, duration, steps=100):
    global current_duty_cycle
    global counter
    if target_duty_cycle > current_duty_cycle:
        direction = 1
    elif target_duty_cycle < current_duty_cycle:
        direction = -1
    else:
        direction = 0

    duty_cycle_step = direction * abs(target_duty_cycle - current_duty_cycle) / steps

    for _ in range(steps):
        current_duty_cycle += duty_cycle_step
        p.ChangeDutyCycle(current_duty_cycle)
        time.sleep(duration / steps)

    p.ChangeDutyCycle(0)
    time.sleep(0.2)
    counter -= 4
    p.stop()
    #gpio.cleanup()
    #led verde acceso
    gpio.output(40, gpio.HIGH)

def save_documents():
    move_servo(12, 3)
    save_button.pack_forget()

window = tk.Tk()
window.title("Autodistruzione")
window.geometry("1080x920")  # Imposta le dimensioni della finestra
window.configure(bg="#000000")  # Sfondo nero

# Dimensioni fisse per il contatore e i pulsanti
font_size_label = 40
font_size_button = 20
button_width = 15
button_height = 4

label = tk.Label(window, text="Pronto", fg="#FF0000", bg="#000000", font=("Helvetica", 300))
label.pack(pady=20)

button_frame = tk.Frame(window, bg="#000000")  # Sfondo nero
button_frame.pack()

stop_button = tk.Button(button_frame, text="STOP", command=stop_countdown, font=("Helvetica", font_size_button), width=button_width, height=button_height, fg='black', bg='red')
stop_button.pack(side=tk.RIGHT, padx=150, pady=150)

save_button = tk.Button(button_frame, text="Salva Documenti", command=save_documents, font=("Helvetica", font_size_button), width=button_width, height=button_height, fg='black', bg='red')
save_button.pack(side=tk.LEFT, padx=150, pady=150)

counter = 0
running = False
timer_stopped = False  # Inizializza timer_stopped a False

while True:
    if gpio.input(10) == gpio.HIGH:
        break

start_countdown()
window.mainloop()
