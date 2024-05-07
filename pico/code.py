import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_win_it import KeyboardLayout
import board
import digitalio
import time

# Definizione della classe di eccezione
class ButtonReleasedException(Exception):
    pass

kbd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayout(kbd)

red = digitalio.DigitalInOut(board.GP5)
red.direction = digitalio.Direction.OUTPUT

green = digitalio.DigitalInOut(board.GP13)
green.direction = digitalio.Direction.OUTPUT

btn = digitalio.DigitalInOut(board.GP16)
btn.switch_to_input(pull=digitalio.Pull.UP)

sleep_time = 60

def btn_on():
    if btn.value == False:
        green.value = True
        red.value = False
        return True
    else:
        green.value = False
        red.value = True
        return False

def check_on():
    if not btn_on():
        kbd.press(Keycode.LEFT_CONTROL, Keycode.C)
        time.sleep(0.1)
        kbd.release_all()
        raise ButtonReleasedException

def execute_commands(sleep_time):
    try:
        kbd.press(Keycode.R, Keycode.GUI)
        time.sleep(0.3)
        kbd.release_all()
        keyboard_layout.write("cmd")
        time.sleep(0.1)
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        time.sleep(1)
        check_on()
        
        keyboard_layout.write("cd Documenti\GDI\Torneo_STUNKEN\S.T.U.N.K.E.N_fake_bomb-main\S.T.U.N.K.E.N_fake_bomb-main")
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        time.sleep(0.5)
        check_on()
        keyboard_layout.write("python secret.py")
        kbd.press(Keycode.ENTER)
        kbd.release_all()
        
        for i in range(sleep_time):
            check_on()
            green.value = True
            time.sleep(0.5)
            green.value = False
            time.sleep(0.5)

        print('finish')
        
    except ButtonReleasedException:
        print("Pulsante rilasciato durante l'esecuzione dei comandi")
        return  # Uscita dalla funzione

    green.value = True
    red.value = False

try:
    while True:
        if btn_on():
            execute_commands(sleep_time)
            
            
            while True:
                if btn.value == False:
                    continue
                else:
                    break
            

        time.sleep(0.1)
except Exception as e:
    print(f"Errore: {e}")

