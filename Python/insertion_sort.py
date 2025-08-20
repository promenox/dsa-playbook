# insertion sort algo

'''
insertion sort ~ cookbook:
    Precondition: we start with an array A of n comparable elements.

    Outer loop invariant: at the start of pass k (1 ≤ k ≤ n-1), the first
        A[0..k-1] elements of the array are sorted. The element A[k] is the
        head of the unsorted region A[k..n-1].

    Inner loop invariant: at the start of iteration j, the subarray A[0..k]
        consists of the A[k] key (not yet placed), a hole 'mark' at index j,
        and the remaining elements A[0..j-1] and A[j+1..k] which are sorted.

    Termination: after n-1 passes, all elements are in their correct position.
'''


# The swap is a clunkier version, there is a greater number of
# assignment of array values, it is also hard to infer the correctness
# of the implementation. In reverse order arrays, it just sucks.
'''
def insertion_sort_swap(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        for j in range(i):
            if nums[(i - 1) - j] > key:
                nums[(i - 1) - j], nums[i - j] = key, nums[(i - 1) - j]
    return nums
'''


# Much stronger implement
def insertion_sort_shift(nums):
    # in python range(a,b) stops at b
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums
