import random

def load_gun(chambers=6):
    bullet_position = random.randint(1,chambers)
    return chambers, bullet_position

def pull_trigger(remaining, bullet_position):
    if remaining <= 0:
        outcome = 'Empty'
        return outcome, remaining
    elif remaining == bullet_position:
        outcome = 'Bang'
        remaining -= 1
    else:
        outcome = 'Click'
        remaining -= 1

    return outcome, remaining
