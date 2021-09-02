# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def reverse(n):
	rev = 0
	while n > 0:
		rev = rev * 10 + n % 10
		n //= 10
	return rev

def palindrome(n):
	return n == reverse(n)

def nthlychrelnumbers(n):
	maxIter = 25
	i = 0
	k = 0
	while i < n:
		k += 1
		flag = True
		x = k
		for _ in range(maxIter):
			x = x + reverse(x)
			if palindrome(x):
				flag = False
				break
		if flag:
			i += 1
	return k
			
	