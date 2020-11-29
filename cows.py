n, k = map(int, input().split()) # 6 3
a = list(map(int, input().split()))  # 2 5 7 11 15 20
a.sort()
left = 0
right = a[-1] - a[0] + 1
while left < right:
    mid = (left + right)//2
    cows = 1
    last = a[0]
    for cur in a[1:]:
        if cur - last > mid:
            cows += 1
            last = cur
    if cows >= k:
        left = mid+1
    else:
        right = mid
print(left)
