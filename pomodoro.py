#!/usr/bin/env python3

import pomodoro_io as io
import datetime as dt
import time

WORK_BEGINNING = 1
WORKING = 2
BREAK_BEGINNING = 3
BREAKING = 4
PAUSED = 10

ZERO_TIMEDELTA  = dt.timedelta()
SLEEP_TIMEDELTA = dt.timedelta(seconds = 1)

WORK_TIMEDELTA  = dt.timedelta(seconds = 25)
BREAK_TIMEDELTA = dt.timedelta(seconds = 5)

WORK_MESSAGE = 'BACK TO WORK!'
BREAK_MESSAGE = 'TAKE A BREAK!'


def transition(state):
    if state['current_state'] == WORK_BEGINNING:
        io.print_large(WORK_MESSAGE)
        io.say_with_beeps(WORK_MESSAGE)
        new_state = { 'time_remaining': WORK_TIMEDELTA,
                      'current_state' : WORKING }
    else:
        io.print_large(BREAK_MESSAGE)
        io.say_with_beeps(BREAK_MESSAGE)
        new_state = { 'time_remaining': BREAK_TIMEDELTA,
                      'current_state' : BREAKING }
    return new_state


def countdown(state):
    time_remaining = state['time_remaining']
    io.print_large(time_remaining)

    new_state = state.copy();
    new_state['time_remaining'] = state['time_remaining'] - SLEEP_TIMEDELTA
    if time_remaining <= ZERO_TIMEDELTA:
        if state['current_state'] == WORKING:
            new_state['current_state'] = BREAK_BEGINNING
        else:
            new_state['current_state'] = WORK_BEGINNING

    return new_state


def toggle_paused(state):
    pass


def main():

    state_machine = { WORK_BEGINNING:  transition,
                      WORKING:         countdown,
                      BREAK_BEGINNING: transition,
                      BREAKING:        countdown,
                      PAUSED:          toggle_paused }

    state = { 'time_remaining': None,
              'current_state': WORK_BEGINNING }

    try:
        while True:
            current_state = state['current_state']
            state_action = state_machine[current_state]
            state = state_action(state)

            if io.did_press_enter_before_timeout(timeout = SLEEP_TIMEDELTA.seconds):
                while not io.did_press_enter_before_timeout(timeout = SLEEP_TIMEDELTA.seconds):
                    pass
            #time.sleep(SLEEP_TIMEDELTA.seconds)

    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    main()


