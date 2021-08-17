# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def isPrime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(n**0.5)+1, 2):
		if n % i == 0:
			return False
	return True

def nthpowerfulnumber(n):
	if n == 0:
		return 1
	i = 0
	k = 1
	while i < n:
		flag = False
		k += 1
		for j in range(2, k):
			if k % j == 0 and isPrime(j):
				if k % j**2 == 0:
					flag = True
				else:
					flag = False
					break
		if (flag):
			i += 1
	return k

print(nthpowerfulnumber(4))