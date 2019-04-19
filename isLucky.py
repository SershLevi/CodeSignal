def isLucky(n):
    n_str = str(n)
    return sum([int(x) for x in n_str[:len(n_str) // 2]]) == sum([int(x) for x in n_str[len(n_str) // 2:]])


print(isLucky(123006))
print(isLucky(123007))
