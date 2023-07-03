import unittest

from sort import mergesort

class TestSort(unittest.TestCase):

    def test_sort(self):
        mergeSortArray = mergesort.sort([3, 19, 44, 2, 50])
        sortedArray = [2, 3, 19, 44, 50]
        self.assertEqual(mergeSortArray, sortedArray, "array of ints should be sorted")

    def test_negatives(self):
        mergeSortArray = mergesort.sort([3, -19, 44, -2, 50])
        sortedArray = [-19, -2, 3, 44, 50]
        self.assertEqual(mergeSortArray, sortedArray, "array with negative ints should be sorted")

    def test_string(self):
        mergeSortString = mergesort.sort(['B', 'A', 'D', 'C'])
        sortedString = ['A', 'B', 'C', 'D']
        self.assertEqual(mergeSortString, sortedString, "array of strings should be sorted")
        

if __name__ == '__main__':
    unittest.main()