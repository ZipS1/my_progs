while True:
    print("Введите пограничное число: ", end='')
    n = int(input())
    if n > 1:
        break
    else:
        "Введено неверное число"
simple = [2]
nums = []
skip = False

#1st way
print("1ST WAY :")
for i in range(2, n):
    for element in simple:
        if i % element == 0:
            skip = True
            break
    if skip:
        skip = False
        continue
    simple.append(i)

for i in simple:
    print(i, end=' ')
print()

print("2ND WAY: ")
#2nd way
nums = [i for i in range(2, n)]
p = 2

while p < 10:
    print(p, end=' ')
    for n in nums:
        if n == 0:
            continue
        if n % p == 0:
            nums[nums.index(n)] = 0
    while p not in nums:
        p += 1

for i in nums:
    if i != 0:
        print(i, end=' ')



    
