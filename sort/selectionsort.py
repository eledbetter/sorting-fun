def sort(inputArray):

    for pos in range(0, inputArray.__len__()):
        selectedPosition = pos

        # find lowest value and select it
        for i in range(pos, inputArray.__len__()):
            if (inputArray[selectedPosition] > inputArray[i]):
                selectedPosition = i

        # swap selected value with current position
        temp = inputArray[pos]
        inputArray[pos] = inputArray[selectedPosition]
        inputArray[selectedPosition] = temp

    return inputArray