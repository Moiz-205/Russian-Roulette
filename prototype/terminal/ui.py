from terminal.utils import animate, cprint, countdown_timer

def get_player_input(timer):
    return countdown_timer(timer)

def show_outcome(actor, outcome):
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

def show_timeout():
    cprint('You took too long... BANG! You are dead!', 'red')

def show_who_goes_first(turn):
    cprint(f'{turn.upper()} goes first!', 'yellow')

def show_spin(actor):
    cprint(f'{actor.capitalize()} spun the revolver...', 'yellow')
