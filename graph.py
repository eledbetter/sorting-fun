import matplotlib.pyplot as plt
from sort import *

algorithmList = ["bubblesort", "mergesort", "selectionsort"]

# display data in a graph
def drawGraph(comparisonsList):
    global algorithmList

    plt.bar(algorithmList, comparisonsList)
    plt.ylabel('comparisons')
    plt.show()

# get comparisons each algorithm makes
def compareSort(inputList):
    # is there a way to iterate through these?
    bubblesort.sort(inputList)
    mergesort.sort(inputList)
    selectionsort.sort(inputList)

    comparisons = [bubblesort.comparisons, 
                   mergesort.comparisons, 
                   selectionsort.comparisons]
    
    drawGraph(comparisons)