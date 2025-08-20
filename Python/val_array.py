# finding the largest and smallest items from an array and returning those vals

# -- min imp --

def min_val_built(nums):
    min_ = 0
    for num in nums:
        min_ = min(min_, num)
    return min_


def min_val_cond(nums):
    min_ = 0
    for num in nums:
        if (num < min_):
            min_ = num
    return min_

# =- max imp --


def max_val_built(nums):
    max_ = 0
    for num in nums:
        max_ = max(max_, num)
    return max_


def max_val_cond(nums):
    max_ = 0
    for num in nums:
        if (num > max_):
            max_ = num
    return max_
