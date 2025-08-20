# bubble sort implementation

'''
bubble sort ~ cookbook:
    Precondition: we start with an array A of n comparable elements.

    Loop invariant (ascending): after k passes, the last k elements of A 
        are the largest k elements in sorted (non-decreasing) order.

    Loop invariant (descending): after k passes, the last k elements of A 
        are the smallest k elements in sorted (non-increasing) order.

    Termination: after n-1 passes, all elements are in their correct position.

    Postcondition (ascending): array A is sorted in non-decreasing order.
    Postcondition (descending): array A is sorted in non-increasing order.
'''


# ascending sort
def bubble_sort_ascd(nums):
    n = len(nums)
    for i in range(n - 1):
        swap = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swap = True
        if not swap:
            break
    return nums


# descending sort
def bubble_sort_dscd(nums):
    n = len(nums)
    for i in range(n - 1):  # outer loop cached at n-1
        swap = False  # to esc for optimization
        for j in range(n - 1 - i):  # inner loop shrinks
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swap = True
        if not swap:
            break
    return nums
