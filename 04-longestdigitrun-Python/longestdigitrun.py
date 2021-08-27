# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).

def run(n):
	c = 1
	while n > 0:
		a = n % 10
		n //= 10
		b = n % 10
		if a == b:
			c += 1
		else:
			break
	return c, a

def longestdigitrun(n):
	n = abs(n)
	cnt = 0
	k = n % 10
	while n > 0:
		(c, x) = run(n)
		if cnt == c:
			k = min(x, k)
		if cnt < c:
			cnt = c
			k = x
		n = n // 10 ** c
	return k