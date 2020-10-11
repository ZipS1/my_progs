def sortlen(i):
    return len(i)

n, m = map(int, input().split())

hor = []
vert = []

for i in range(2*n + 1):
    if i % 2 == 0:
        hor.append(input())
    else:
        vert.append(input())

path = [(0, 0)]
route = ''
outs = []
mult_ways = False
x = 0
y = 0

routes = []
banned_ways = []


while True:
    if x + 1 <= m :
        if hor[y][x] == 'e' and (x + 1, y) not in path and (x + 1, y, 'e') not in banned_ways:
            outs.append((x + 1, y, 'e'))
    if x - 1 >= 0:
        if hor[y][x - 1] == 'w' and (x - 1, y) not in path and (x - 1, y, 'w') not in banned_ways:
            outs.append((x - 1, y, 'w'))
    if y + 1 <= n:
        if vert[y][x] == 's' and (x, y + 1) not in path and (x, y + 1, 's') not in banned_ways:
            outs.append((x, y + 1, 's'))
    if y - 1 >= 0:
        if vert[y - 1][x] == 'n' and (x, y - 1) not in path and (x, y - 1, 'n') not in banned_ways:
            outs.append((x, y - 1, 'n'))

    if len(outs) == 0:
        if mult_ways:
            path = [(0, 0)]
            route = ''
            outs = []
            mult_ways = False
            x = 0
            y = 0
        else:
            print(len(routes[0]))
            print(routes[0])
            quit()


    if len(outs) > 1:
        mult_ways = True
        outs = [outs[0]]
        banned_ways.append(outs[0])

    if len(outs) == 1:
        x, y = outs[0][0], outs[0][1]
        route += outs[0][2]
        if len(routes) == 1:
            if len(routes[0]) < len(route):
                if mult_ways:
                    path = [(0, 0)]
                    route = ''
                    outs = []
                    mult_ways = False
                    x = 0
                    y = 0
                else:
                    print(len(routes[0]))
                    print(routes[0])
                    quit()

        path.append((x, y))
        if x == m and y == n:
            routes.append(route)
            if mult_ways:
                path = [(0, 0)]
                route = ''
                outs = []
                mult_ways = False
                x = 0
                y = 0
                continue
            break,md м
        outs = []

routes.sort()
routes.sort(key=sortlen)
print(len(routes[0]))
print(routes[0])
