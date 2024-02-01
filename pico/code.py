import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import board
import digitalio
import time

red = digitalio.DigitalInOut(board.GP5)
red.direction = digitalio.Direction.OUTPUT
red.value = True

green = digitalio.DigitalInOut(board.GP13)
green.direction = digitalio.Direction.OUTPUT
green.value = False

kbd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kbd)
# Press ctrl-x.
kbd.press(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.T)
time.sleep(0.1)
kbd.release_all()

time.sleep(1)

keyboard_layout.write("cd /home/mattabott/Documents/GDI/STUNKEN")
kbd.press(Keycode.ENTER)
kbd.release_all()
time.sleep(0.5)

keyboard_layout.write("python3 secret.py")
kbd.press(Keycode.ENTER)
kbd.release_all()
time.sleep(0.5)

time.sleep(5)

green.value = True
red.value = False

while True:
    pass