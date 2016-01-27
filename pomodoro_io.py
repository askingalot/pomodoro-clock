import os
import datetime as dt
from pyfiglet import figlet_format
from sys import stdin
from select import select


def did_press_enter_before_timeout(timeout):
    buffers = select([stdin,],[],[],timeout)[0]
    if buffers:
        buffers[0].readline()
        return True
    else:
        return False


def clear_screen():
    print("\x1b[2J\x1b[H")


def print_large(msg, font='starwars'):
    clear_screen()
    str_msg = str(msg)
    large_text = figlet_format(str_msg, font=font).center(80)
    print( large_text )


def beep():
    print('\a\a')


def say(message):
    os.system('say "' + message + '"')


def say_with_beeps(message):
    beep()
    say(message)
    beep()



