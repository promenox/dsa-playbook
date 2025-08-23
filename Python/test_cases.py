import unittest

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


class TestDSA(unittest.TestCase):
    # -- testing fibonacci --

    # recurisive ver of fib seq
    def test_fib_recursive(self):
        self.assertEqual(fib_recu(9), 34)

    # iterative ver of fib seq
    def test_fib_iterative(self):
        self.assertEqual(fib_iter(9), 34)

    # -- testing num val arrays --
    num_array = [7, 12, 9, 11, 3, -1]

    # min val array with python min()
    def test_minVal_builtIn(self):
        self.assertEqual(val_array.min_val_built(self.num_array.copy()), -1)

    # min val array with python max()
    def test_maxVal_builtIn(self):
        self.assertEqual(val_array.max_val_built(self.num_array.copy()), 12)

    # min val array with conditions <
    def test_minVal_selfCond(self):
        self.assertEqual(val_array.min_val_cond(self.num_array.copy()), -1)

    # min val array with conditions >
    def test_maxVal_selfCond(self):
        self.assertEqual(val_array.max_val_cond(self.num_array.copy()), 12)

    # -- testing array sorting --

    # test arrays
    test_array = [5, 1, 4, 2, 3]
    test_array_2 = [3, 1, 1, 5, 1]

    # result arrays
    ascd_dupl_array = [1, 1, 1, 3, 5]
    dscd_dupl_array = [5, 3, 1, 1, 1]
    ascd_array = [1, 2, 3, 4, 5]
    dscd_array = [5, 4, 3, 2, 1]

    # a. bubble sort
    # ascending
    def test_bubble_sort_ascd(self):
        self.assertEqual(
            bubble_sort.bubble_sort_ascd(self.test_array.copy()),
            self.ascd_array
        )

    # ascending on rev array
    def test_bubble_sort_ascd_rev(self):
        self.assertEqual(
            bubble_sort.bubble_sort_ascd(self.dscd_array.copy()),
            self.ascd_array
        )

    # ascending on dupl array
    def test_bubble_sort_ascd_dup(self):
        self.assertEqual(
            bubble_sort.bubble_sort_ascd(self.test_array_2.copy()),
            self.ascd_dupl_array
        )

    # descending
    def test_bubble_sort_dscd(self):
        self.assertEqual(
            bubble_sort.bubble_sort_dscd(self.test_array.copy()),
            self.dscd_array
        )

    # ascending on rev array
    def test_bubble_sort_dscd_rev(self):
        self.assertEqual(
            bubble_sort.bubble_sort_dscd(self.ascd_array.copy()),
            self.dscd_array
        )

    # descending on dupl array
    def test_bubble_sort_dscd_dup(self):
        self.assertEqual(
            bubble_sort.bubble_sort_dscd(self.test_array_2.copy()),
            self.dscd_dupl_array
        )

    # b. selection sort
    # ascending
    def test_selection_sort_ascd(self):
        self.assertEqual(
            selection_sort.selection_sort_ascd(self.test_array.copy()),
            self.ascd_array
        )

    # ascending on rev array
    def test_selection_sort_ascd_rev(self):
        self.assertEqual(
            selection_sort.selection_sort_ascd(self.dscd_array.copy()),
            self.ascd_array
        )

    # ascending on dupl array
    def test_selection_sort_ascd_dup(self):
        self.assertEqual(
            selection_sort.selection_sort_ascd(self.test_array_2.copy()),
            self.ascd_dupl_array
        )

    # descending
    def test_selection_sort_dscd(self):
        self.assertEqual(
            selection_sort.selection_sort_dscd(self.test_array.copy()),
            self.dscd_array
        )

    # descending on rev array
    def test_selection_sort_dscd_rev(self):
        self.assertEqual(
            selection_sort.selection_sort_dscd(self.ascd_array.copy()),
            self.dscd_array
        )

    # descending on dupl array
    def test_selection_sort_dscd_dup(self):
        self.assertEqual(
            selection_sort.selection_sort_dscd(self.test_array_2.copy()),
            self.dscd_dupl_array
        )

    # the ascd / dscd workflow is redundant
    # at this point, i focus on ascd only

    # c. insertion sort
    def test_insertion_sort(self):
        self.assertEqual(
            insertion_sort.insertion_sort_shift(self.test_array.copy()),
            self.ascd_array
        )

    def test_insertion_sort_rev(self):
        self.assertEqual(
            insertion_sort.insertion_sort_shift(self.dscd_array.copy()),
            self.ascd_array
        )

    def test_insertion_sort_dup(self):
        self.assertEqual(
            insertion_sort.insertion_sort_shift(self.test_array_2.copy()),
            self.ascd_dupl_array
        )

    # d. quick sort
    # recursive type A
    def test_quick_sort_typeA(self):
        self.assertEqual(
            quick_sort.quick_sort_typeA(self.test_array.copy()),
            self.ascd_array
        )

    def test_quick_sort_typeA_rev(self):
        self.assertEqual(
            quick_sort.quick_sort_typeA(self.dscd_array.copy()),
            self.ascd_array
        )

    def test_quick_sort_typeA_dup(self):
        self.assertEqual(
            quick_sort.quick_sort_typeA(self.ascd_dupl_array.copy()),
            self.ascd_dupl_array
        )

    # recursive type B
    def test_quick_sort_typeB(self):
        self.assertEqual(
            quick_sort.quick_sort_typeB(self.test_array.copy()),
            self.ascd_array
        )

    def test_quick_sort_typeB_rev(self):
        self.assertEqual(
            quick_sort.quick_sort_typeB(self.dscd_array.copy()),
            self.ascd_array
        )

    def test_quick_sort_typeB_dup(self):
        self.assertEqual(
            quick_sort.quick_sort_typeB(self.ascd_dupl_array.copy()),
            self.ascd_dupl_array
        )


if __name__ == "__main__":
    unittest.main()
