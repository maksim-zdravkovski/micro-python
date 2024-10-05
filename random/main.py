from microbit import *
import random

while True:
    if button_a.is_pressed():
        display.show(str(random.randint(1, 6)))