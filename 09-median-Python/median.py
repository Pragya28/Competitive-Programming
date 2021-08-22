# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	if len(a) == 0:
		return None
	L = sorted(a)
	n = len(L)
	if n % 2 == 0:
		return (L[n//2-1] + L[n//2])/2
	else:
		return L[(n-1)//2]