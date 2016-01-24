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

WORK_TIMEDELTA  = dt.timedelta(minutes = 1)
BREAK_TIMEDELTA = dt.timedelta(minutes = 1)


def work_beginning(state):
    io.print_large('BACK TO WORK!')
    io.say_back_to_work()

    new_state = { 'time_remaining': WORK_TIMEDELTA,
                  'current_state' : WORKING }
    return new_state


def working(state):
    time_remaining = state['time_remaining']
    io.print_large(time_remaining)

    if time_remaining <= ZERO_TIMEDELTA:
        new_state = state.copy()
        new_state['current_state'] = BREAK_BEGINNING
        return new_state
    else:
        return state


def break_beginning(state):
    io.print_large('TAKE A BREAK!')
    io.say_take_a_break()

    new_state = { 'time_remaining': BREAK_TIMEDELTA,
                  'current_state' : BREAKING }
    return new_state


def breaking(state):
    time_remaining = state['time_remaining']
    io.print_large(time_remaining)

    if time_remaining <= ZERO_TIMEDELTA:
        new_state = state.copy()
        new_state['current_state'] = WORK_BEGINNING
        return new_state
    else:
        return state


def paused(state):
    pass


def main():

    state_machine = { WORK_BEGINNING:  work_beginning,
                      WORKING:         working,
                      BREAK_BEGINNING: break_beginning,
                      BREAKING:        breaking,
                      PAUSED:          paused }

    state = { 'time_remaining': None,
              'current_state': WORK_BEGINNING }

    try:
        while True:
            current_state = state['current_state']
            state_action = state_machine[current_state]
            state = state_action(state)

            state['time_remaining'] = state['time_remaining'] - SLEEP_TIMEDELTA
            time.sleep(SLEEP_TIMEDELTA.seconds)

    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    main()


