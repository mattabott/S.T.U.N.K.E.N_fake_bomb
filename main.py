import tkinter as tk
from datetime import datetime
from excel_manager import initialize_excel, update_excel
from timer_logic import find_next_target_time
import RPi.GPIO as gpio
import time
import pygame

# Impostazioni GPIO, suono e variabili globali
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(10, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(40, gpio.OUT)
gpio.output(40, gpio.LOW)

pygame.mixer.init()
pygame.mixer.music.load("sirena.mp3")

excel_file = 'team_times.xlsx'
df = initialize_excel(excel_file)

last_printed_team = None
timer_start_time = None
timer_running = False  # Variabile per controllare lo stato del timer

# Prepara l'interfaccia grafica ma non mostrarla ancora
root = tk.Tk()
root.title("Eliminazione Database")
root.geometry("1920x1080")
root.configure(bg='black')
root.withdraw()  # Nasconde la finestra

time_str = tk.StringVar()
timer_label = tk.Label(root, textvariable=time_str, font=("Helvetica", 300), fg='red', bg='black')
timer_label.pack(expand=True)

def update_timer():
    global last_printed_team, timer_start_time, df, timer_running
    if timer_running:
        now = datetime.now()
        target_time, team = find_next_target_time()
        remaining = target_time - now
        if remaining.total_seconds() > 0:
            mins, secs = divmod(remaining.total_seconds(), 60)
            time_str.set('{:02d}:{:02d}'.format(int(mins), int(secs)))
        else:
            time_str.set("00:00")
        
        if team != last_printed_team:
            print("Prossimo team:", team)
            last_printed_team = team
            if timer_start_time is None:
                timer_start_time = now.strftime("%H:%M:%S")

            update_excel(df, excel_file, team, now, mins, secs)

        root.after(1000, update_timer)

def toggle_timer():
    global timer_running
    if not timer_running:
        root.deiconify()  # Mostra la finestra
        timer_running = True
        pygame.mixer.music.play(-1)
        update_timer()
    else:
        pygame.mixer.music.stop()
        timer_running = False
        time_str.set("PAUSA")
        root.withdraw()  # Nasconde la finestra

# Funzione per controllare il pulsante in modo asincrono
def check_button():
    if gpio.input(10) == gpio.HIGH:
        toggle_timer()
        time.sleep(0.2)  # Debouncing
    root.after(200, check_button)

root.after(500, check_button)  # Inizia a controllare il pulsante dopo un breve ritardo

root.mainloop()

