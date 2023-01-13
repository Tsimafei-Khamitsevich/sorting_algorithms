"""
Contains tests for sorting functions
"""

import unittest
import main

class TestSort():
    """
    Base class with test cases for
    sorting algorithms
    """
    def test_empty_list(self):
        self.assertEqual(self.func([]), [])

    def test_one_element(self):
        self.assertEqual(self.func([1]), [1])

    def test_two_elements(self):
        self.assertEqual(self.func([9, 2]), [2, 9])

    def test_neg_elements(self):
        self.assertEqual(self.func(
            [-8, -10, -83, -1, -99, -100]),
            [-100, -99, -83, -10, -8, -1]
            )
    
    def test_duplicates(self):
        self.assertEqual(self.func(
            [-8, -8, -9, -9, 10, 10, 10, 3, 1]),
            [-9, -9, -8, -8, 1, 3, 10, 10, 10]
            )

    def test_long_list(self):
        array = main.generate_rand_array(n=1000, min=-1000, max=1000)        
        sorted_array = sorted(array)
        self.assertEqual(self.func(array), sorted_array)


class TestSimpleSort(TestSort, unittest.TestCase):
    """
    simple_sort function test
    """

    def func(self, array):
        return main.simple_sort(array)


class TestSelectionSort(TestSort, unittest.TestCase):
    """
    selection_sort function test
    """

    def func(self, array):
        return main.selection_sort(array)


class TestBubbleSort(TestSort, unittest.TestCase):
    """
    bubble_sort function test
    """

    def func(self, array):
        return main.bubble_sort(array)


class TestInsertionSort(TestSort, unittest.TestCase):
    """
    insertion_sort function test
    """

    def func(self, array):
        return main.insertion_sort(array)


class TestMergeSort(TestSort, unittest.TestCase):
    """
    merge_sort function test
    """

    def func(self, array):
        return main.merge_sort(array)

    
class TestQuickSort(TestSort, unittest.TestCase):
    """
    quick_sort function test
    """

    def func(self, array):
        return main.quick_sort(array)


class TestShellSort(TestSort, unittest.TestCase):
    """
    shell_sort function test
    """
    def func(self, array):
        return main.shell_sort(array)


if __name__ == '__main__':
    unittest.main()