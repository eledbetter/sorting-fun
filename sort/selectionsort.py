comparisons = 0

# Swaps current position with lowest value in unsorted portion of the list if needed
def sort(inputList):
    global comparisons
    sortedList = inputList[:]

    for pos in range(0, sortedList.__len__()):
        selectedPosition = pos

        # find lowest value and select it
        for i in range(pos + 1, sortedList.__len__()):
            comparisons += 1
            if (sortedList[selectedPosition] > sortedList[i]):
                selectedPosition = i

        # swap selected value with current position
        temp = sortedList[pos]
        sortedList[pos] = sortedList[selectedPosition]
        sortedList[selectedPosition] = temp

    return sortedList