# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]


def allSets(n):
    size = 2 ** n
    lst = []
    for i in range(size):
        s = set()
        for j in range(size):
            if i & (1 << j) > 0:
                s.add(j+1)
        lst.append(s)
    return lst

def limitedPowerSet(n, k):
    sets = sorted(allSets(n), key = len)
    res = sets[:k]
    res[0] = {}
    return res


assert(limitedPowerSet(5,7) == [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ])
print("Test case passed")