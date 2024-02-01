import time, sys

duration = 10  # Durata del caricamento
bar_length = 30  # Lunghezza della barra di progresso

for i in range(duration + 1):
    percent = int((i / duration) * 100)
    filled_length = int(bar_length * i // duration)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f"\rDownload: [{bar}] {percent}%")

    time.sleep(0.5)

print("\nDownload Completato")