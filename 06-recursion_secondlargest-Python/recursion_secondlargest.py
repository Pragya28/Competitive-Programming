# Recursion-Only recursion_secondlargest(L) [15 pts]
# Note: recall that you may not use sort, sorted, min, or max this week! With that in mind, write the function 
# recursion_secondlargest(L) that takes a list of integers in any order and returns the second-largest value in the list. To 
# be more precise, it returns the second value from the end if the list was sorted (though you do not need to sort 
# it to solve this problem), so if the largest value occurs twice, you would return that value. Also, if there are 
# fewer than 2 values in the list, return None. Here are some test cases:
# assert(recursion_secondlargest([1,2,3,4,5]) == 4)
# assert(recursion_secondlargest([4,3]) == 3)
# assert(recursion_secondlargest([4,4,3]) == 4)
# assert(recursion_secondlargest([-3,-4]) == -4)
# assert(recursion_secondlargest([4]) == None)
# assert(recursion_secondlargest([ ]) == None)
# Again, you do not need to sort the list. We didn't sort it in our sample solution. We just tracked the two largest 
# values as we recursively traversed the list. Also, you may not use loops/iteration in this problem

def secondLargest(L, out = []):
	if len(out) == 2 and len(L) == 0:
		if out[0] > out[1]:
			return out[1]
		else:
			return out[0]
	if len(out) == 2:
		if L[0] > out[0] and L[0] >	out[1]:
			if out[0] < out[1]:
				out.pop(0)
			else:
				out.pop(1)
		elif L[0] > out[0]:
			out.pop(0)
		elif L[0] > out[1]:
			out.pop(1)
	if len(out) < 2:
		out.append(L[0])
	L.pop(0)
	return secondLargest(L, out)

def recursion_secondlargest(L):
	if len(L) < 2:
		return None
	return secondLargest(L, [])