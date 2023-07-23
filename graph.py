'''
will be used to display number of comparisons each algorithm makes
for now just testing stuff

TODO: implement way to track and display comparisons each algorithm makes
'''

import matplotlib.pyplot as plt
from sort import *

'''
get # of comparisons from each algorithm
    
display graph
'''
sortAlgorithms = ["bubblesort", "mergesort", "selectionsort"]

def drawGraph(comparisons):
    global sortAlgorithms

    plt.bar(sortAlgorithms, comparisons)
    plt.ylabel('comparisons')
    plt.show()

def compareSort(inputList):
    # is there a way to iterate through these?
    bubblesort.sort(inputList)
    mergesort.sort(inputList)
    selectionsort.sort(inputList)

    comparisons = [bubblesort.comparisons, 
              mergesort.comparisons, 
              selectionsort.comparisons]
    
    drawGraph(comparisons)

unsorted = [9, 2, 3, 1, 19, 0]
compareSort(unsorted)