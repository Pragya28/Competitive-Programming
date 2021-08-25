# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def isPrime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(n ** 0.5)+1, 2):
		if n % i == 0:
			return False
	return True

def fun_hasnoprimes(l):
	for i in l:
		for n in i:
			if isPrime(n):
				return False
	return True
