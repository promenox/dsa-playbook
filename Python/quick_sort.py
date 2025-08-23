# using pivot element and recursive soirting

'''
quick sort recursive ~ cookbook:
    Precondition: we start with an array A of n comparable elements.

    Recursive step: we select the pivot element (can be start, middle, end,
        or random). Left sub arrays <= pivot and right sub-array containin
        elems >= pivot. We recursivley sort the left and right sub arrays.

        Partitioning internally swaps elements as needed and finally swaps
        the pivot into its correct position before recursion continues.

    Termination: base case reached when sub-array size <= 1
'''
import random


def quick_sort_typeA(nums):
    n = len(nums)
    if n <= 1:
        return nums

    pivot = random.randrange(len(nums))
    pivot_val = nums[pivot]

    left = [x for x in nums if x < pivot_val]  # O(n)
    mid = [x for x in nums if x == pivot_val]   # O(n)
    right = [x for x in nums if x > pivot_val]  # O(n)
    # O(3n)

    return quick_sort_typeA(left) + mid + quick_sort_typeA(right)


'''
quick sort loop ~ cookbook:
    Precondition: we have an array A[l..r] of n values and a pivot value x
        chosen from A[l..r]. The loop moves l forward while A[l] < x and moves
        r backward while A[r] > x, swapping when needed.

    Loop invariant:
        left side -> A[start..l-1] <= pivot
        right side -> A[r+1..end] >= pivot
        middle -> A[l..r] not yet processed

        When l and r cross, the sub array is partitioned and the pivot is in
        it's final position.

        During the loop, swap elements at l and r when they are on the wrong
        side; after the loop ends, swap the pivot with the element at the
        partition point to place it in its final position.

    Terimnation: when l > r, the sub array is partitioned.
'''
# https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/visualize/


def quick_sort_typeB(nums):
    n = len(nums)

    # base case one elem or less
    if n <= 1:
        return nums

    # set middle as pivot index
    p_idx = n//2
    pivot = nums[p_idx]

    # swap pivot with last elem
    nums[p_idx], nums[-1] = nums[-1], nums[p_idx]

    # define sub array region
    l_idx = 0
    r_idx = n - 2

    while True:
        # move items around the pivot value and define a swap point
        while nums[l_idx] < pivot:
            l_idx += 1
        while nums[r_idx] > pivot:
            r_idx -= 1

        # pointers matched (swap point)
        if l_idx >= r_idx:
            break

        # swap items 
        # < piv -> left
        # > piv -> right
        nums[l_idx], nums[r_idx] = nums[r_idx], nums[l_idx]

        # and increment forwards
        l_idx += 1
        r_idx -= 1

    # swap the pivot back into place
    nums[l_idx],  nums[-1] = nums[-1], nums[l_idx]

    # recurse on left and right
    return (quick_sort_typeB(nums[:l_idx])  # left sub-array
            + [nums[l_idx]]  # pivot
            + quick_sort_typeB(nums[l_idx+1:])  # right sub-array
            )


'''
personal takeaweays:
    1. loop forms managing pivot indicies are tricky and hard to read.
    2. managing dupicate forms of a pivot are essential.
    3. placing the midpoint back is important.
    2. recursvie thinking is essential for the sub arrays.
    3. base cases are needed to terminate the recursion. 
'''
