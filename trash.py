from my_decorators import pd


@pd
def arrayMaximalAdjacentDifference(inputArray):
    return max([abs(inputArray[i + 1] - v) for i, v in enumerate(inputArray[:-1])])


inputArray = [2, 4, 1, 0]

arrayMaximalAdjacentDifference(inputArray)
