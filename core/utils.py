import time
import signal
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

# countdown_timer() for handling timer
def countdown_timer(seconds):
    def timeout_handler(signum, frame):
        raise TimeoutError

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(seconds)

    try:
        player_input = input(f'Pull Trigger (y/n) [{seconds}s]:')
        signal.alarm(0)
        return player_input
    except TimeoutError:
        print("\rTime's up!")
        return None
