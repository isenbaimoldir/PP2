def unique(nums):
    u = []
    for i in nums:
        if i not in u:
            u.append(i)
    return u

nums = list(map(int, input().split()))
print(unique(nums))