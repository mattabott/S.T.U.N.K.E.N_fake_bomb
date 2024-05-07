import time
import sys
from easter_egg import logo
from colorama import init, Fore, Style

# Inizializza colorama (necessario per Windows)
init(autoreset=True)

# Definizioni dei colori usando `Fore` da colorama
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
WHITE = Fore.WHITE

# Resetta lo stile utilizzando `Style.RESET_ALL`
RESET = Style.RESET_ALL

def print_colored(text, color):
    sys.stdout.write(color + text + RESET)

def fake_download():
    print_colored("\nInizio del download...\n\n", YELLOW)
    
    time.sleep(2)

    duration = 100  # Durata del caricamento
    bar_length = 50  # Lunghezza della barra di progresso

    for i in range(duration + 1):
        percent = int((i / duration) * 100)
        filled_length = int(bar_length * i // duration)
        bar = '*' * filled_length + '-' * (bar_length - filled_length)
        sys.stdout.write("\r" + MAGENTA + f"Download: [{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(0.6)  # Tempo di ritardo per simulare il download

    time.sleep(1)
    
    print_colored("\n\nDownload completato!", GREEN)
    
    time.sleep(1)
    
    print_colored("\nOra puoi scollegare l'Hard Disk in sicurezza\n\n", GREEN)
    
    time.sleep(1)

if __name__ == "__main__":
    try:
        fake_download()
    except:
        print_colored("\n\nDownload non completato\n\n", RED)

# Scrivi il logo utilizzando il colore appropriato
sys.stdout.write("\r" + BLUE + logo + RESET)
sys.stdout.flush()
