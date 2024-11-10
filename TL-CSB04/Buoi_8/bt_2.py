def sort_balls(nums):
    n = len(nums)

    for _ in range(n):
        for i in range(n - 1):
            if (nums[i] == 'b' and nums[i + 1] != 'b') or \
               (nums[i] == 'w' and nums[i + 1] == 'r'):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

nums = ["b", "r", "b", "w", "w", "r"]

print(sort_balls(nums))
