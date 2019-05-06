# In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.
#
# Example
#
# For
#
# matrix = [[true, false, false],
#           [false, true, false],
#           [false, false, false]]
# the output should be
#
# minesweeper(matrix) = [[1, 2, 1],
#                        [2, 1, 1],
#                        [1, 1, 1]]
# Check out the image below for better understanding:
#
#
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.array.boolean matrix
#
# A non-empty rectangular matrix consisting of boolean values - true if the corresponding cell contains a mine, false otherwise.
#
# Guaranteed constraints:
# 2 ≤ matrix.length ≤ 100,
# 2 ≤ matrix[0].length ≤ 100.
#
# [output] array.array.integer
#
# Rectangular matrix of the same size as matrix each cell of which contains an integer equal to the number of mines in the neighboring cells. Two cells are called neighboring if they share at least one corner.
from my_decorators import pd


@pd
def minesweeper(matrix):
    for j, _ in enumerate(matrix):
        matrix[j].insert(0, False)
        matrix[j].append(False)
        for i, _ in enumerate(matrix[j]):
            matrix[j][i] = 1 if matrix[j][i] else 0
    matrix.insert(0, [0 for _ in matrix[0]])
    matrix.append([0 for _ in matrix[0]])

    return [
        [(sum(matrix[i][j:j + 3]) + sum(matrix[i + 2][j:j + 3]) + matrix[i + 1][j] + matrix[i + 1][j + 2]) for j, _ in
         enumerate(matrix[i][1:-1])] for i, _ in enumerate(matrix[1:-1])]


matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]

ExpectedOutput = [[1, 2, 1],
                  [2, 1, 1],
                  [1, 1, 1]]

print(minesweeper(matrix) == ExpectedOutput)

matrix = [[True, True, True],
          [True, True, True],
          [True, True, True]]

ExpectedOutput = [[3, 5, 3],
                  [5, 8, 5],
                  [3, 5, 3]]

print(minesweeper(matrix) == ExpectedOutput)
