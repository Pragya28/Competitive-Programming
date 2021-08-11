# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	flag = (n == abs(n))
	n = abs(n)
	i = 0
	x = 0
	for i in range(k):
		dig = n % 10
		n //= 10
		x = dig * 10 ** i + x
	n //= 10
	n = n * 10 ** (k+1) + d * 10 ** k + x
	if flag:
		return n
	else:
		return -n
