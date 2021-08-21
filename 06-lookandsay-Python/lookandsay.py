# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def count(L, start):
	c = 1
	while start < len(L)-1:
		if L[start] == L[start+1]:
			c += 1
			start += 1
		else:
			break
	return c


def lookandsay(a):
	i = 0
	res = []
	while i < len(a):
		n = count(a, i)
		res.append((n, a[i]))
		i += n
	return res