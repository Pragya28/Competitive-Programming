# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

from collections import defaultdict

def mostfrequentdigit(n):
	d = defaultdict(int)
	while (n > 0):
		d[n%10] += 1
		n //= 10
	d = sorted(d.items(), key = lambda x:(-x[1], x[0]))
	# print(d)
	if len(d) == 0:
		return 0
	return d[0][0]

