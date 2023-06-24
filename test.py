import unittest

import sort

class TestSort(unittest.TestCase):

    def test_mergeSort(self):

        mergeSortArray = sort.mergeSort([3, 19, 44, 2, 50])
        sortedArray = [2, 3, 19, 44, 50]
        self.assertEqual(mergeSortArray, sortedArray, "array of ints should be sorted")

    def test_mergeSort_negatives(self):
        mergeSortArray = sort.mergeSort([3, -19, 44, -2, 50])
        sortedArray = [-19, -2, 3, 44, 50]
        self.assertEqual(mergeSortArray, sortedArray, "array with negative ints should be sorted")

    def test_mergeSort_string(self):
        mergeSortString = sort.mergeSort(['B', 'A', 'D', 'C'])
        sortedString = ['A', 'B', 'C', 'D']
        self.assertEqual(mergeSortString, sortedString, "array of strings should be sorted")
        

if __name__ == '__main__':
    unittest.main()