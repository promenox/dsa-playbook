import unittest

# [A] algorithms
# 1) fibonacci
from fibonacci_recursive import fibonacci as fib_recu
from fibonacci_iterative import fibonacci as fib_iter

# 2) max / min val arrays
import val_array

# 3) sorting
import bubble_sort
import selection_sort
import insertion_sort
import quick_sort

# [B] data structures
# 1) stack and queue
from stack import Stack, ManualStack


class BaseDSASetup(unittest.TestCase):
    # new arrays for each test
    def setUp(self):
        self.num_array = [7, 12, 9, 11, 3, -1]
        self.test_array = [5, 1, 4, 2, 3]
        self.test_array_2 = [3, 1, 1, 5, 1]
        self.ascd_array = [1, 2, 3, 4, 5]
        self.dscd_array = [5, 4, 3, 2, 1]
        self.ascd_dupl_array = [1, 1, 1, 3, 5]
        self.dscd_dupl_array = [5, 3, 1, 1, 1]


# == ALGORITHIMS ==
class TestFibonacci(unittest.TestCase):
    # -- testing fibonacci --

    # recurisive ver of fib seq
    def test_fib_recursive(self):
        self.assertEqual(fib_recu(9), 34)

    # iterative ver of fib seq
    def test_fib_iterative(self):
        self.assertEqual(fib_iter(9), 34)


class TestValFinder(BaseDSASetup):
    # -- testing num val arrays --

    # min val array with python min()
    def test_minVal_builtIn(self):
        self.assertEqual(val_array.min_val_built(self.num_array), -1)

    # min val array with python max()
    def test_maxVal_builtIn(self):
        self.assertEqual(val_array.max_val_built(self.num_array), 12)

    # min val array with conditions <
    def test_minVal_selfCond(self):
        self.assertEqual(val_array.min_val_cond(self.num_array), -1)

    # min val array with conditions >
    def test_maxVal_selfCond(self):
        self.assertEqual(val_array.max_val_cond(self.num_array), 12)


# -- SORTING --
class TestBubbleSort(BaseDSASetup):
    # a. bubble sort
    # ascending
    def test_bubble_sort_ascd(self):
        self.assertEqual(
            bubble_sort.bubble_sort_ascd(self.test_array),
            self.ascd_array
        )

    # ascending on rev array
    def test_bubble_sort_ascd_rev(self):
        self.assertEqual(
            bubble_sort.bubble_sort_ascd(self.dscd_array),
            self.ascd_array
        )

    # ascending on dupl array
    def test_bubble_sort_ascd_dup(self):
        self.assertEqual(
            bubble_sort.bubble_sort_ascd(self.test_array_2),
            self.ascd_dupl_array
        )

    # descending
    def test_bubble_sort_dscd(self):
        self.assertEqual(
            bubble_sort.bubble_sort_dscd(self.test_array),
            self.dscd_array
        )

    # ascending on rev array
    def test_bubble_sort_dscd_rev(self):
        self.assertEqual(
            bubble_sort.bubble_sort_dscd(self.ascd_array),
            self.dscd_array
        )

    # descending on dupl array
    def test_bubble_sort_dscd_dup(self):
        self.assertEqual(
            bubble_sort.bubble_sort_dscd(self.test_array_2),
            self.dscd_dupl_array
        )


class TestSelectionSort(BaseDSASetup):
    # b. selection sort
    # ascending
    def test_selection_sort_ascd(self):
        self.assertEqual(
            selection_sort.selection_sort_ascd(self.test_array),
            self.ascd_array
        )

    # ascending on rev array
    def test_selection_sort_ascd_rev(self):
        self.assertEqual(
            selection_sort.selection_sort_ascd(self.dscd_array),
            self.ascd_array
        )

    # ascending on dupl array
    def test_selection_sort_ascd_dup(self):
        self.assertEqual(
            selection_sort.selection_sort_ascd(self.test_array_2),
            self.ascd_dupl_array
        )

    # descending
    def test_selection_sort_dscd(self):
        self.assertEqual(
            selection_sort.selection_sort_dscd(self.test_array),
            self.dscd_array
        )

    # descending on rev array
    def test_selection_sort_dscd_rev(self):
        self.assertEqual(
            selection_sort.selection_sort_dscd(self.ascd_array),
            self.dscd_array
        )

    # descending on dupl array
    def test_selection_sort_dscd_dup(self):
        self.assertEqual(
            selection_sort.selection_sort_dscd(self.test_array_2),
            self.dscd_dupl_array
        )

# the ascd / dscd workflow is redundant
# at this point, i focus on ascd only


class TestInsertionSort(BaseDSASetup):
    # c. insertion sort
    def test_insertion_sort(self):
        self.assertEqual(
            insertion_sort.insertion_sort_shift(self.test_array),
            self.ascd_array
        )

    def test_insertion_sort_rev(self):
        self.assertEqual(
            insertion_sort.insertion_sort_shift(self.dscd_array),
            self.ascd_array
        )

    def test_insertion_sort_dup(self):
        self.assertEqual(
            insertion_sort.insertion_sort_shift(self.test_array_2),
            self.ascd_dupl_array
        )


class TestQuickSort(BaseDSASetup):
    # d. quick sort
    # recursive type A
    def test_quick_sort_typeA(self):
        self.assertEqual(
            quick_sort.quick_sort_typeA(self.test_array),
            self.ascd_array
        )

    def test_quick_sort_typeA_rev(self):
        self.assertEqual(
            quick_sort.quick_sort_typeA(self.dscd_array),
            self.ascd_array
        )

    def test_quick_sort_typeA_dup(self):
        self.assertEqual(
            quick_sort.quick_sort_typeA(self.test_array_2),
            self.ascd_dupl_array
        )

    # recursive type B
    def test_quick_sort_typeB(self):
        self.assertEqual(
            quick_sort.quick_sort_typeB(self.test_array),
            self.ascd_array
        )

    def test_quick_sort_typeB_rev(self):
        self.assertEqual(
            quick_sort.quick_sort_typeB(self.dscd_array),
            self.ascd_array
        )

    def test_quick_sort_typeB_dup(self):
        self.assertEqual(
            quick_sort.quick_sort_typeB(self.test_array_2),
            self.ascd_dupl_array
        )


class TestStack(unittest.TestCase):
    def setUp(self):
        # new stack for each test
        self.test_stack = Stack([])
        self.test_manual_stack = ManualStack(10)

    # built-in methods
    def test_1stack_isEmpty_true(self):
        self.assertTrue(self.test_stack.isEmpty())

    def test_2stack_isEmpty_false(self):
        self.test_stack.push('A')
        self.assertFalse(self.test_stack.isEmpty())

    def test_3stack_peek(self):
        self.test_stack.push('A')
        self.test_stack.push('B')
        self.assertEqual(self.test_stack.peek(), 'B')

    def test_4stack_pop(self):
        self.test_stack.push('A')
        self.test_stack.push('B')
        self.assertEqual(self.test_stack.pop(), 'B')

    def test_5stack_size(self):
        self.test_stack.push('A')
        self.test_stack.push('B')
        self.assertEqual(self.test_stack.size(), 2)

    # not using built-in methods
    def test_1manualStack_isEmpty_true(self):
        self.assertTrue(self.test_manual_stack.isEmpty())

    def test_2manualStack_isEmpty_false(self):
        self.test_manual_stack.push('A')
        self.assertFalse(self.test_manual_stack.isEmpty())

    def test_3manualStack_peek(self):
        self.test_manual_stack.push('A')
        self.test_manual_stack.push('B')
        self.assertEqual(self.test_manual_stack.peek(), 'B')

    def test_4manualStack_pop(self):
        self.test_manual_stack.push('A')
        self.test_manual_stack.push('B')
        self.assertEqual(self.test_manual_stack.pop(), 'B')

    def test_5manualStack_size(self):
        self.test_manual_stack.push('A')
        self.test_manual_stack.push('B')
        self.assertEqual(self.test_manual_stack.size(), 2)


if __name__ == "__main__":
    unittest.main()
