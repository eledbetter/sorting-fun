'''
will be used to display number of comparisons each algorithm makes
for now just testing stuff

TODO: implement way to track and display comparisons each algorithm makes
'''

import matplotlib.pyplot as plt
from sort import *



aList = [4, 2, 7, 10, 22, 1]
print("bubblesort: ", bubblesort.sort(aList), bubblesort.comparisons)
print("mergesort: ", mergesort.sort(aList), mergesort.comparisons)
print("selectionsort: ", selectionsort.sort(aList), selectionsort.comparisons)

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()