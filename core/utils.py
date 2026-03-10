import time
from termcolor import colored

# animate() for "Pulling Trigger... effect"
def animate(message, dots=3, delay=0.5):
    print(message, end='', flush=True)
    for _ in range(dots):
        time.sleep(delay)
        print('.', end='', flush=True)
    print('\n')

# cprint() for "You Survived!" with color
def cprint(message, color):
    print(colored(message, color))
