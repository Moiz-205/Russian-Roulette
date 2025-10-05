import random
import time
from termcolor import colored

# user = input('Play Russian Roulette (y/n): ')
# turn = input("Pick Gun (y/n): ") if else

live = random.randint(1,6)
# print(live)
chamber = 6
gun = chamber

while True:
    # gun = chamber
    if gun > 0:
        trigger = input("Pull Trigger (y/n): ")

        if trigger == 'y':
            if gun == live:
                print('\nPulling Trigger', end='', flush=True)
                for i in range(3):
                    time.sleep(0.5)
                    print('.', end='', flush=True)
                time.sleep(0.3)
                print(colored('\nBammm! You are dead...', 'red'))
                break

            else:
                print('\nPulling Trigger', end='', flush=True)
                for i in range(3):
                    time.sleep(0.5)
                    print('.', end='', flush=True)
                time.sleep(0.3)
                print(colored('\nYou Survived...!', 'blue'))

                # to remove the used blanks
                gun -= 1

                if gun == live:
                    print('\nMachine Pulling Trigger', end='', flush=True)
                    for i in range(3):
                        time.sleep(0.3)
                        print('.', end='', flush=True)
                    time.sleep(0.1)
                    print(colored('\nBammm! Machine\'s Dead...', 'green'))
                    print(colored('You Survived...', 'blue'))
                    break

                else:
                    print('\nMachine Pulling Trigger', end='', flush=True)
                    for i in range(3):
                        time.sleep(0.3)
                        print('.', end='', flush=True)
                    time.sleep(0.1)
                    print(colored('\nMachine survived...!', 'red'))
                    print('\nYours Turn')
                    gun -= 1
                    continue
        
        elif trigger == 'n':
            print(colored('You are killed for being a CHICKEN...!', 'red'))
            break
        else:
            print(colored('You are killed for being a FOOLISH CHICKEN...!', 'red'))
            break
    
    else:
        break
