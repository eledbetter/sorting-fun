# Recursively splits inputted list in half then sorts each half 
def sort(inputArray):

    arraySize = inputArray.__len__()

    # quit if only 1 element
    if(arraySize <= 1):
        return inputArray
    
    # split inputted array into halves
    unsortedLeft = inputArray[0 : (int)(arraySize / 2)]
    unsortedRight = inputArray[(int)(arraySize / 2) : arraySize]

    # sort left half of array
    sortedLeft = sort(unsortedLeft)

    # sort right half of array
    sortedRight = sort(unsortedRight)


    # compare first value of both halves 
    # append lowest to sortedWhole
    # repeat til no more elements 
    sortedWhole = []
    while((sortedLeft.__len__() > 0) or (sortedRight.__len__() > 0)):

        # append next value from right side, if left array is empty
        if (sortedLeft.__len__() < 1):
            sortedWhole.append(sortedRight.pop(0))
            continue

        # append next value from left side, if right array is empty
        if (sortedRight.__len__() < 1):
            sortedWhole.append(sortedLeft.pop(0))
            continue

        # append lowest value
        if (sortedLeft[0] < sortedRight[0]):
            sortedWhole.append(sortedLeft.pop(0))
            continue

        sortedWhole.append(sortedRight.pop(0))

    return sortedWhole