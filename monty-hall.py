#!/usr/bin/env python3

import random, argparse

parser = argparse.ArgumentParser(description='Suppose you\'re on a game show, and you\'re \
given the choice of three doors: Behind one door is a car; behind the others, goats. You \
pick a door, say No. 1, and the host, who knows what\'s behind the doors, opens another \
door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" \
Is it to your advantage to switch your choice?')
parser.add_argument('repeat', help='Amount of times the test runs.', type=int)
args = parser.parse_args()

holding = 0
changing = 0

for i in range(args.repeat):
    doors = [0, 0, 1]
    random.shuffle(doors)
    pick = random.choice(doors)
    if pick:
        holding += 1
    else:
        changing += 1

print('holding', holding)
print('changing', changing)

