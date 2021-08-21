# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def countDigits(n):
	if n == 0:
		return 1
	c = 0
	while n > 0:
		c += 1
		n //= 10
	return c

def endsWith(n, k):
	c = countDigits(k)
	num = 0
	for p in range(c):
		num = n % 10 * 10 ** p + num
		n //= 10
	if num == k:
		return True
	return False

def nthautomorphicnumbers(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	if n == 3:
		return 5
	if n == 4:
		return 6
	i = 4
	cnt = 1
	nums = [5, 6]
	while i < n:
		arr = []
		p = 0
		c = 10 ** cnt
		while p < len(nums):			
			x = nums[p]
			for j in range(1, 10):
				r = j * c + x
				sq = r ** 2
				if endsWith(sq, r):
					nums.remove(x)
					arr.append(r)
					p -= 1
					break
			p += 1
		if len(arr) != 0:
			arr.sort()
			while len(arr) > 0 and i < n:
				nums.append(arr[0])
				arr.pop(0)
				i += 1
		cnt += 1
	return nums[-1]

# import time
# t = time.time()
# print(nthautomorphicnumbers(10))
# print(time.time() - t)