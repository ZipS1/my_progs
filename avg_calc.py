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
