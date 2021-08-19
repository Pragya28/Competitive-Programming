# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.

from collections import defaultdict

def fun_kth_occurrences(s, n):
	freq = defaultdict(int)
	for ch in s:
		freq[ch] += 1
	d = sorted(freq.items(), key = lambda x: (x[1], x[0]), reverse = True)
	return d[n-1][0]


