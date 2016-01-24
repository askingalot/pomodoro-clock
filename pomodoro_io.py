import os
import datetime as dt
from pyfiglet import figlet_format


def clear_screen():
    print(chr(27) + "[2J")


def print_large(msg, font='big'):
    clear_screen()
    str_msg = str(msg)
    large_text = figlet_format(str_msg, font=font).center(80)
    print( large_text + "\n\n\n\n\n" )


def beep():
    print('\a\a\a')


def say(message):
    os.system('say "' + message + '"')


def say_take_a_break():
    beep()
    say("It's time to take a break")
    beep()


def say_back_to_work():
    beep()
    say("get back to work")
    beep()



