from utils import animate, cprint

def get_player_input():
    trigger = input('Pull Trigger (y/n): ')
    return trigger

def show_output(actor, outcome):
    if actor == 'player':
        animate('Pulling Trigger')

        if outcome == 'bang':
            cprint('Bamm! You are dead...', 'red')
        elif outcome == 'click':
            cprint('You Survived...!', 'blue')

    elif actor == "machine":
        animate("Machine Pulling Trigger", delay=0.3)

        if outcome == "bang":
            cprint("Bamm! Machine's Dead...", "green")
            cprint("You Survived...", "blue")
        elif outcome == "click":
            cprint("Machine Survived...!", "red")

def show_chicken():
    cprint("You are killed for being a CHICKEN...!", "red")

def show_invalid():
    cprint("You are killed for being a FOOLISH CHICKEN...!", "red")
