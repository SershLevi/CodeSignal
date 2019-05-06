# You are given an array of integers representing coordinates of obstacles situated on a straight line.
#
# Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.
#
# Find the minimal length of the jump enough to avoid all the obstacles.
#
# Example
#
# For inputArray = [5, 3, 6, 7, 9], the output should be
# avoidObstacles(inputArray) = 4.
#
# Check out the image below for better understanding:
#
#
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.integer inputArray
#
# Non-empty array of positive integers.
#
# Guaranteed constraints:
# 2 ≤ inputArray.length ≤ 1000,
# 1 ≤ inputArray[i] ≤ 1000.
#
# [output] integer
#
# The desired length.
from my_decorators import pd


@pd
def avoidObstacles(inputArray):
    return min([v for v in range(1, max(inputArray) + 2) if all(x % v != 0 for x in inputArray)])


inputArray = [19, 32, 11, 23]
ExpectedOutput = 3

avoidObstacles(inputArray)

inputArray = [1, 4, 10, 6, 2]
ExpectedOutput = 7
avoidObstacles(inputArray)

inputArray = [1000, 999]
ExpectedOutput = 6
avoidObstacles(inputArray)

inputArray = [2, 3]
ExpectedOutput = 4
avoidObstacles(inputArray)
