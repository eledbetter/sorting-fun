import unittest

from sort import bubblesort

class TestSort(unittest.TestCase):

    def test_sort(self):
        bubblesortList = bubblesort.sort([3, 19, 44, 50, 2])
        sortedArray = [2, 3, 19, 44, 50]
        self.assertEqual(bubblesortList, sortedArray, "array of ints should be sorted")

    def test_negatives(self):
        bubblesortList = bubblesort.sort([3, -19, 44, 50, -2])
        sortedArray = [-19, -2, 3, 44, 50]
        self.assertEqual(bubblesortList, sortedArray, "array with negative ints should be sorted")

    def test_string(self):
        bubbleSortString = bubblesort.sort(['B', 'A', 'D', 'C'])
        sortedString = ['A', 'B', 'C', 'D']
        self.assertEqual(bubbleSortString, sortedString, "array of strings should be sorted")
        

if __name__ == '__main__':
    unittest.main()