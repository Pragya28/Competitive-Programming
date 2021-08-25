# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	newL = []
	for i in L:
		for n in i:
			if n not in newL:
				newL.append(n)
			else:
				return True
	return False
