# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.

def alternatingSum(L, s = 0, sign = 1):
	if len(L) == 0:
		return s
	s = s + sign*L[0]
	sign = -sign
	return alternatingSum(L[1:], s, sign)

def fun_recursions_alternatingsum(l): 
	return alternatingSum(l)