# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def countDigits(n):
	c = 0
	while n > 0:
		c += 1
		n //= 10
	return c

def hasZero(n):
	while n > 0:
		if n % 10 == 0:
			return True
		n //= 10
	return False

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

def nthcircularprime(n):
	i = 0
	k = 1
	while i < n:
		k += 1
		flag = True
		if not hasZero(k):
			c = countDigits(k)
			x = k
			if isPrime(x):
				for j in range(c-1):
					x = x % (10 **(c-1)) * 10 + x // (10 **(c-1))
					if not isPrime(x) or x == k:
						flag = False
						break
				if flag:
					i += 1
	return k

print(nthcircularprime(5))