# Swaps current position with lowest value in unsorted portion of the list if needed
def sort(inputList):

    for pos in range(0, inputList.__len__()):
        selectedPosition = pos

        # find lowest value and select it
        for i in range(pos, inputList.__len__()):
            if (inputList[selectedPosition] > inputList[i]):
                selectedPosition = i

        # swap selected value with current position
        temp = inputList[pos]
        inputList[pos] = inputList[selectedPosition]
        inputList[selectedPosition] = temp

    return inputList