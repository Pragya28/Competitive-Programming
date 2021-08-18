# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def isPrime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(n ** 0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

def sumOfSq(n):
	s = 0
	while n > 0:
		s += (n % 10) ** 2
		n //= 10
	return s

def fun_nth_happy_prime(n):
	k = 0
	i = 0
	while (k <= n):
		i += 1
		if isPrime(i):
			num = sumOfSq(i)
			while num > 9:
				num = sumOfSq(num)
			if num == 1:
				k += 1
	return i

print(fun_nth_happy_prime(1))