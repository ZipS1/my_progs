m, n = map(int, input().split())

k = [0] * (n+1)
k[m] = 1

for i in range(m, n+1):
    k[i] += k[i-1]
    if i % 4 == 0 and i//4 >= m:
        k[i] += k[i//4]

print(k[n])
