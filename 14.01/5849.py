m, n = map(int, input("Введите числа через пробел: ").split())
INDEXERROR_FUSE = 20

k = [0] * (n+INDEXERROR_FUSE)
k[m] = 1

for i in range(m, n+1):
    k[i+1] += k[i]

    if i // 10 == 0:
        if i == 9:
            continue
        k[i] += k[i]
    else:
        k[i+10] += k[i]

print("Ответ:", k[n])
