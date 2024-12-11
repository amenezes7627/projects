def check_safe(nums):
    diff = False
    inc = all(i < j for i, j in zip(nums, nums[1:]))
    dec = all(i > j for i, j in zip(nums, nums[1:]))
    if inc or dec:
        diff = all(((abs(i - j) >= 1) and (abs(i - j) <= 3)) for i, j in zip(nums, nums[1:]))
    if (inc or dec) and diff:
        return 1
    else:
        return 0

# part 1
fp = open("day2.txt")
sum = 0
unsafe = []
for line in fp.readlines():
    nums = line.split()
    nums = list(map(int, nums))
    result = check_safe(nums)
    if result == 1:
        sum += 1
    else:
        unsafe.append(line)

print(sum)

# part 2
for line in unsafe:
    nums = line.split()
    nums = list(map(int, nums))
    i = 0
    for i in range(len(nums)):
        element = nums.pop(i)
        result = check_safe(nums)
        if result == 1:
            sum += 1
            break
        nums.insert(i, element)

print(sum)