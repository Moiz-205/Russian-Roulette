import random

live = random.randint(1,6)
chamber = 6
gun = chamber

while True:
    # r = input('R (y/n): ')
    # if r == 'y':
    #     gun = chamber
    # else:
    print(live)
    print(gun)
    t = input('T (t or r): ')
    if t == 'r':
            gun = chamber
            continue
    elif t == 't':
        if gun == live:
            print('Fire')
            break
        else:
            print('Blank')
            gun -= 1
    else:
         break
    