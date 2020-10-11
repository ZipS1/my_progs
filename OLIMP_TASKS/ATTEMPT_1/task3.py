def walle(x):
    while wall[x] > wall[x - 1]:
        wall[x] -= 1
        wall[x-1] += 1
        for i in range(x - 1, 0, -1):
            if wall[i] > wall[i - 1]:
                wall[i] -= 1
                wall[i - 1] += 1


stackAmount = input()

wall = input().split()
wall = [int(i) for i in wall]
past_wall = 0

while True:
    ind = 0
    for i in wall:
        if ind == 0:
            past = i
            ind += 1
            continue

        if i > past:
            work = True
            walle(ind)
            ind = 0
            continue

        past = i
        ind += 1
        if ind == stackAmount:
            ind == 0

    if past_wall == wall:
        for i in wall:
            print(i, end=' ')
        quit()
    else:
        past_wall = list(wall)

