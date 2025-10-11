import random
from termcolor import colored

# user = input('Play Russian Roulette (y/n): ')
# turn = input("Pick Gun (y/n): ") if else

live = random.randint(1,6)
chamber = 6
gun = chamber

# Turn based mechanic to take turn first or pass it
choice = input("Pick gun (y/n): ")
if choice == 'y':
    turn = 'Player'
else:
    turn = 'Machine'


while True:
    if gun > 0:
        trigger = input("Pull Trigger (y/n): ")

        if trigger == 'y':
            if gun == live:
                print(colored('\nBammm! You are dead...', 'red'))
                break

            else:
                print(colored('\nYou Survived...!', 'blue'))
                gun -= 1

                if gun == live:
                    print(colored('\nBammm! Machine\'s Dead...', 'green'))
                    print(colored('You Survived...', 'blue'))
                    break

                else:
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