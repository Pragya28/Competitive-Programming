# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

def sumOfSq(n):
	s = 0
	while n > 0:
		s += (n % 10) ** 2
		n //= 10
	return s

def ishappynumber(n):
	if n < 0:
		return False
	n = sumOfSq(n)
	while (n > 9):
		n = sumOfSq(n)
	if n == 1:
		return True
	return False

def nth_happy_number(n):
	i = 0
	k = 0
	while i < n:
		k += 1
		if ishappynumber(k):
			i += 1
	return k
