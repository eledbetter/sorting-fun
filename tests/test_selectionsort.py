import unittest

from sort import selectionsort

class TestSort(unittest.TestCase):

    def test_sort(self):
        selectionSortArray = selectionsort.sort([3, 19, 44, 2, 50])
        sortedArray = [2, 3, 19, 44, 50]
        self.assertEqual(selectionSortArray, sortedArray, "array of ints should be sorted")

    def test_negatives(self):
        selectionSortArray = selectionsort.sort([3, -19, 44, -2, 50])
        sortedArray = [-19, -2, 3, 44, 50]
        self.assertEqual(selectionSortArray, sortedArray, "array with negative ints should be sorted")

    def test_string(self):
        selectionSortString = selectionsort.sort(['B', 'A', 'D', 'C'])
        sortedString = ['A', 'B', 'C', 'D']
        self.assertEqual(selectionSortString, sortedString, "array of strings should be sorted")
        

if __name__ == '__main__':
    unittest.main()