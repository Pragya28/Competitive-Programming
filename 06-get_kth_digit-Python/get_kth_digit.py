# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 

def fun_get_kth_digit(n, k):
	n = abs(n)
	c =   0
	while n > 0:
		if c == k:
			return n % 10
		n //= 10 
		c += 1
	return 0
