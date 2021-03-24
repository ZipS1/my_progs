print("Welcome to average number calculator!")

nums = []
finished = False
while not finished:
    try:
        num = int(input("Enter number: "))
    except Exception:
        finished = True

    if not finished:
        nums.append(num)
        avg = sum(nums)/len(nums)
        print(f"Average: {avg:.3f}")

if avg is not None:
    count = 0
    while avg < 4.5:
        nums.append(5)
        avg = sum(nums)/len(nums)
        count += 1
    print(f"You need {count} more fives!")
