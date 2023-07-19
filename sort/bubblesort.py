''' 
Iterates through list swapping current and next value if needed
Ends when no swaps performed after a full iteration
'''

comparisons = 0

def sort(inputList):
    global comparisons
    swapCount = -1
    sortedList = inputList[:]

    while (swapCount != 0):
        swapCount = 0

        for i in range(sortedList.__len__() - 1):
            comparisons += 1

            if sortedList[i] <= sortedList[i + 1]:
                continue
            
            # swap values
            temp = sortedList[i]
            sortedList[i] = sortedList[i + 1]
            sortedList[i + 1] = temp
            swapCount += 1

    return sortedList