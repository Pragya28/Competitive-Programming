# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def check0to9(n):
	s = str(n)
	if len(s) < 10:
		return False
	for i in range(10):
		k = str(i)
		if k not in s:
			return False
	return True

def nthwithproperty309(n):
	i = 0
	k = 1
	while i <= n:
		k += 1
		if check0to9(k ** 5):
			i += 1
	return k
