def spy_game(nums):
    num = 0
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            num += 1
            i += 1
        elif nums[i] == 7 and num >= 2:
            return True
        else:
            i += 1
    return False

print(spy_game([1,2,4,0,0,7]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0])) 