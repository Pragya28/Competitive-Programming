# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]


# Took help from GeeksForGeeks (https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/)

def permute(lst):
	if len(lst) == 0:
		return []
	if len(lst) == 1:
		return [lst]
	
	res = []

	for i in range(len(lst)):
		lst = list(lst)
		curr = lst[i]
		left = lst[:i]
		right = lst[i+1:]
		newLst = tuple(left + right)
		for p in permute(newLst):
			res.append(tuple([curr] + list(p)))
	return res


def getallpermutations(x):
	lst = tuple(x)
	return permute(lst)

from itertools import permutations
print(getallpermutations("xyza"))
print(list(permutations("xyza", r=4)))