# Write a function that reverses characters in (possibly nested) parentheses in the input string.
#
# Input strings will always be well-formed with matching ()s.
#
# Example
#
# For inputString = "(bar)", the output should be
# reverseInParentheses(inputString) = "rab";
# For inputString = "foo(bar)baz", the output should be
# reverseInParentheses(inputString) = "foorabbaz";
# For inputString = "foo(bar)baz(blim)", the output should be
# reverseInParentheses(inputString) = "foorabbazmilb";
# For inputString = "foo(bar(baz))blim", the output should be
# reverseInParentheses(inputString) = "foobazrabblim".
# Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] string inputString
#
# A string consisting of lowercase English letters and the characters ( and ). It is guaranteed that all parentheses in inputString form a regular bracket sequence.
#
# Guaranteed constraints:
# 0 ≤ inputString.length ≤ 50.
#
# [output] string
#
# Return inputString, with all the characters that were in parentheses reversed.
from my_decorators import pd


@pd
def reverseInParentheses(istr):
    a, b = "(", ")"
    while a in istr and b in istr:
        start_p = istr.rfind(a)
        end_p = istr[start_p:].find(b) + start_p
        istr = istr[:start_p] + istr[start_p + 1:end_p][::-1] + istr[end_p + 1:]
        a, b = b, a
    return istr

# FIND MORE EFFECTIVE SOLUTION,
    # props to vanpet90 for his genious idea to use eval in the previous version of this task
def reverseInParentheses(s):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')
