m = 22
n = 2
k = [0] * (m+1)
k[m] = 1

for i in range(m, n-1, -1):
    k[i-2] += k[i]
    k[i-5] += k[i]
print(k[n])
