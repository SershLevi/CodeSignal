# Given a string, find out if its characters can be rearranged to form a palindrome.
#
# Example
#
# For inputString = "aabb", the output should be
# palindromeRearranging(inputString) = true.
#
# We can rearrange "aabb" to make "abba", which is a palindrome.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] string inputString
#
# A string consisting of lowercase English letters.
#
# Guaranteed constraints:
# 1 ≤ inputString.length ≤ 50.
#
# [output] boolean
#
# true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.
from my_decorators import pd


@pd
def palindromeRearranging(inputString):
    d = {}
    [d.update({c: d.setdefault(c, 0) + 1}) for c in inputString]
    return sum([1 for v in d.values() if v % 2 != 0]) <= 1
    # better way
    return sum([inputString.count(i) % 2 for i in set(inputString)]) <= 1

palindromeRearranging('aaddds')
palindromeRearranging('abbcabb')
