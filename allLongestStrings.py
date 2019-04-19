def allLongestStrings(inputArray):
    # max_v = 0
    # new_ar = []
    # for val in inputArray:
    #     max_v = max_v if max_v >= len(val) else len(val)
    #
    # for val in inputArray:
    #     if len(val) == max_v:
    #         new_ar.append(val)
    #
    # return new_ar

    m = max([len(a) for a in inputArray])
    return [x for x in inputArray if len(x) == max([len(a) for a in inputArray])]


inputArray = ["aba",
              "aa",
              "ad",
              "vcd",
              "aba"]

print(allLongestStrings(inputArray))
