import random
import time
from termcolor import colored

# user = input('Play Russian Roulette (y/n): ')
# turn = input("Pick Gun (y/n): ") if else

for i in range(1,7):
    trigger = input("Pull Trigger (y/n): ")

    if trigger == 'y':
        gun = random.randint(1,2)
        if gun == 1:
            print('Pulling Trigger', end='', flush=True)
            for i in range(3):
                time.sleep(0.5)
                print('.', end='', flush=True)
            time.sleep(0.3)
            print(colored('\nYou Survived...!', 'blue'))

            print('\nMachine turn')
            gun_machine = random.randint(1,2)
            if gun_machine == 1:
                print('Machine Pulling Trigger', end='', flush=True)
                for i in range(3):
                    time.sleep(0.3)
                    print('.', end='', flush=True)
                time.sleep(0.1)
                print(colored('\nMachine survived...!', 'red'))
                print('\nYours Turn')
                continue

            else:
                print('Machine Pulling Trigger', end='', flush=True)
                for i in range(3):
                    time.sleep(0.3)
                    print('.', end='', flush=True)
                time.sleep(0.1)
                print('\nBammm! Machine\'s Dead...')
                print(colored('\nYou Survived...', 'blue'))
                break

        elif gun == 2:
            print('Pulling Trigger', end='', flush=True)
            for i in range(3):
                time.sleep(0.5)
                print('.', end='', flush=True)
            time.sleep(0.3)
            print(colored('\nBammm! You are dead...', 'red'))
            break

    elif trigger == 'n':
        print('You are killed for leaving the game...!')
        break
    else:
        print('You are killed for being a coward...!')
        break
                 