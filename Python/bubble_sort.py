# bubble sort implementation

'''
bubble sort ~ cookbook:
    Precondition: we start with an array A of n comparable elements.
    Loop invariant: after each pass, the largest remaining unsorted element 
                    is placed at the end of the unsorted portion.
    Termination: after n-1 passes, no unsorted portion remains.
    Postcondition: array A is sorted in non-decreasing order.
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
    for i in range(n - 1): # outer loop cached at n-1 
        swap = False # to esc for optimization
        for j in range(n - 1 - i): # inner loop shrinks
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swap = True
        if not swap:
            break
    return nums
