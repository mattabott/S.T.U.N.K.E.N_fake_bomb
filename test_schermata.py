import tkinter as tk

def start_countdown():
    global counter
    counter = 10  # Durata del countdown in secondi
    update_label()

def update_label():
    global counter
    if counter > 0:
        label.config(text=str(counter))
        counter -= 1
        window.after(1000, update_label)
    else:
        label.config(text="Finito!")

def stop_countdown():
    global counter
    counter = 0
    label.config(text="Ferma")

# Configurazione della finestra Tkinter
window = tk.Tk()
window.title("Countdown Timer")

# Imposta dimensioni e posizione della finestra
window.geometry("800x600+100+100")  # Larghezza x Altezza + PosX + PosY

# Creazione dell'etichetta per il countdown
label = tk.Label(window, text="Pronto", font=("Arial", 100), fg="blue")
label.pack(pady=40)

# Creazione dei pulsanti
start_button = tk.Button(window, text="Inizia", font=("Arial", 20), command=start_countdown, bg="green", fg="white", height=2, width=10)
start_button.pack(side=tk.LEFT, padx=50)

stop_button = tk.Button(window, text="Ferma", font=("Arial", 20), command=stop_countdown, bg="red", fg="white", height=2, width=10)
stop_button.pack(side=tk.RIGHT, padx=50)

# Variabile globale per il counter
counter = 0

# Avvia l'interfaccia
window.mainloop()
