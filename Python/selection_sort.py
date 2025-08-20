# selection sort implementation

'''
selection sort ~ cookbook:
    Precondition: we start with an array A of n comparable elements.

    Loop invariant (ascending): after k passes, the first k elements of A 
        are the smallest k elements in sorted (non-decreasing) order.

    Loop invariant (descending): after k passes, the first k elements of A 
        are the largest k elements in sorted (non-increasing) order.

    Termination: after n-1 passes, all elements are in their correct position.

    Postcondition (ascending): array A is sorted in non-decreasing order.
    Postcondition (descending): array A is sorted in non-increasing order.
'''


def selection_sort_ascd(nums):
    n = len(nums)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
        # swap more efficient (O(1)) than splice/insert (O(n))
        # alternative approaches:
        #   nums.insert(i, nums.pop(min_idx))
        #   nums[i], nums[i+1:n] = (
        #       nums[min_idx],
        #       ums[i:min_idx] + nums[min_idx+1:n],
        #   )
    return nums


def slection_sort_dscd(nums):
    n = len(nums)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] > nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums
