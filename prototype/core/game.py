import random
from core.gun import load_gun, pull_trigger, spin_chamber
from terminal.ui import (get_player_input, show_outcome, show_chicken, show_invalid,
show_timeout, show_who_goes_first, show_spin)

def get_timer(player_turn_count):
    if player_turn_count <= 3:
        return 10
    elif player_turn_count <= 5:
        return 7
    else:
        return 4

def should_machine_spin():
    return random.randint(1, 5) == 1

def player_turn(remaining, bullet_position, player_turn_count):
    timer = get_timer(player_turn_count)
    trigger = get_player_input(timer)

    if trigger is None:
        show_timeout()
        return 'bang', remaining
    elif trigger == 'n':
        show_chicken()
        return 'quit', remaining
    elif trigger != 'y':
        show_invalid()
        return 'quit', remaining

    outcome, remaining = pull_trigger(remaining, bullet_position)
    show_outcome('player', outcome)
    return outcome, remaining

def machine_turn(remaining, bullet_position):
    if should_machine_spin():
        remaining, bullet_position = spin_chamber()
        show_spin('machine')

    outcome, remaining = pull_trigger(remaining, bullet_position)
    show_outcome('machine', outcome)
    return outcome, remaining, bullet_position

def game_loop():
    remaining, bullet_position = load_gun()
    turn = random.choice(['player', 'machine'])
    show_who_goes_first(turn)
    player_turn_count = 0

    while True:
        if remaining <= 0:
            break

        if turn == 'player':
            player_turn_count += 1
            outcome, remaining = player_turn(remaining, bullet_position, player_turn_count)

            if outcome in ('bang', 'quit'):
                break
            turn = 'machine'

        elif turn == 'machine':
            outcome, remaining, bullet_position = machine_turn(remaining, bullet_position)
            if outcome == 'bang':
                break
            turn = 'player'
