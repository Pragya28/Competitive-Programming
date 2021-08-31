# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    n = len(lst)
    syms = set(lst[0])
    if len(syms) != n:
        return False
    for row in lst:
        if set(row) != syms:
            return False
    newLst = [[lst[i][j] for i in range(n)] for j in range(n)]
    for row in newLst:
        if set(row) != syms:
            return False
    return True
    

a = [
    ["A", "B", "C"],
    ["C", "A", "B"],
    ["B", "C", "A"]
]

assert(isLatinSquare(a) == True)

b = [
    [1, 2],
    [1, 2]
]

assert(isLatinSquare(b) == False)

c = [
    [1, 2, 3, 4, 5],
    [2, 3, 5, 1, 4],
    [3, 5, 4, 2, 1],
    [4, 1, 2, 5, 3],
    [5, 4, 1, 3, 2]
]

assert(isLatinSquare(c) == True)

print("All test cases passed.")