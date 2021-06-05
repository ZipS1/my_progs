import random as r
ITERATIONS = 1000
count_1 = 0
count_2 = 0
for _ in range(ITERATIONS):
    doors = [0 for i in range(3)]
    prize = r.randint(0, 2)
    doors[prize] = 1
    choice = r.randint(0,2)
    if doors[choice] == 1:
        count_1 += 1

for _ in range(ITERATIONS):
    doors = [0 for i in range(3)]
    prize = r.randint(0, 2)
    doors[prize] = 1
    choice = r.randint(0,2)
    opened = prize
    while opened == prize or opened == choice:
        opened = r.randint(0,2)
    old_choice = choice
    while choice == old_choice or choice == opened:
        choice = r.randint(0,2)
    if doors[choice] == 1:
        count_2 += 1
print(f"NO CHANGING: {count_1} out of {ITERATIONS} ({count_1/ITERATIONS:.2%})")
print(f"WITH CHANGING: {count_2} out of {ITERATIONS} ({count_2/ITERATIONS:.2%})")
