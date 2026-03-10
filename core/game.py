from gun import load_gun, pull_trigger
from ui import get_player_input, show_outcome, show_chicken, show_invalid

def game_loop():
    remaining, bullet_position = load_gun()

    while True:
        if remaining <= 0:
            break

        trigger = get_player_input()

        if trigger == 'n':
            show_chicken()
            break
        elif trigger != 'y':
            show_invalid()
            break

        # player turn
        outcome, remaining = pull_trigger(remaining, bullet_position)
        show_outcome('player', outcome)
        if outcome == 'bang':
            break

        # machine turn
        outcome, remaining = pull_trigger(remaining, bullet_position)
        show_outcome('machine', outcome)
        if outcome == 'bang':
            break
