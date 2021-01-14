m, n = map(int, input().split())
k = [0] * (n+100)
k[m] = 1

for i in range(m, n+1):
    if i == 25:
        continue
    k[i+1] += k[i]
    k[i*2] += k[i]
print(k[n])
