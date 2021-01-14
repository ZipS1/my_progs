m = int(input('из какого числа преобразовать?: '))
n = int(input('в какое число преобразовать?: '))
k = [0]*(n+1)
k[m] = 1
for i in range(m,n+1):
    
    k[i] += k[i-1]
    k[i] += k[i-2]
    if i <= 5:
        k[2 * i - 1] += k[i]
print(k[n])
