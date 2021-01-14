m, n = map(int, input().split())
k = [0] * (n+100)
k[m] = 1

for i in range(m, n+1):
    k[i+1] += k[i]
    k[i+2] += k[i]
    k[2*i-1] += k[i]
print(k[n])
