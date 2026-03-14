import random

def load_gun(chambers=6):
    bullet_position = random.randint(1,chambers)
    return chambers, bullet_position

def pull_trigger(remaining, bullet_position):
    if remaining <= 0:
        outcome = 'empty'
        return outcome, remaining
    elif remaining == bullet_position:
        outcome = 'bang'
        remaining -= 1
    else:
        outcome = 'click'
        remaining -= 1

    return outcome, remaining

# Mid-game revolver spin for the strategy
def spin_chamber(chambers=6):
    bullet_position = random.randint(1, chambers)
    return chambers, bullet_position
