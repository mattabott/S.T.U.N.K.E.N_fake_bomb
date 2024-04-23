import time
import sys
from easter_egg import logo

# Codici colore ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

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
        time.sleep(0.05)

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

sys.stdout.write("\r" + BLUE + logo)
sys.stdout.flush()

