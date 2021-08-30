# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def powOf3toN(n, L, k):
	if k > n:
		if len(L) == 0:
			return None
		return L
	L.append(k)
	return powOf3toN(n, L, k*3)

def recursion_powersof3ton(n):
	return powOf3toN(n, [], 1)


print(recursion_powersof3ton(1))