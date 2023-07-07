''' 
Iterates through list swapping current and next value if needed
Ends when no swaps performed after a full iteration
'''
def sort(inputList):
    swapCount = -1

    while (swapCount != 0):
        swapCount = 0

        for i in range(inputList.__len__() - 1):
            if inputList[i] <= inputList[i + 1]:
                continue
            
            # swap values
            temp = inputList[i]
            inputList[i] = inputList[i + 1]
            inputList[i + 1] = temp
            swapCount += 1

    return inputList