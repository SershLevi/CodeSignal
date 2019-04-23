# An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.
#
# Given a string, find out if it satisfies the IPv4 address naming rules.
#
# Example
#
# For inputString = "172.16.254.1", the output should be
# isIPv4Address(inputString) = true;
#
# For inputString = "172.316.254.1", the output should be
# isIPv4Address(inputString) = false.
#
# 316 is not in range [0, 255].
#
# For inputString = ".254.255.0", the output should be
# isIPv4Address(inputString) = false.
#
# There is no first number.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] string inputString
#
# A string consisting of digits, full stops and lowercase English letters.
#
# Guaranteed constraints:
# 1 ≤ inputString.length ≤ 30.
#
# [output] boolean
#
# true if inputString satisfies the IPv4 address naming rules, false otherwise.
from my_decorators import pd


@pd
def isIPv4Address(inputString):
    return all(v.isdigit() and 0 <= int(v) <= 255 for v in inputString.split(".")) and len(inputString.split(".")) == 4


inputString = "172.16.254.1"
isIPv4Address(inputString)

inputString = ".254.255.0"
isIPv4Address(inputString)