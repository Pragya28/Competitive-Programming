# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	s = 0
	c = 0
	while x > 0 or y > 0:
		a = x % 10
		b = y % 10 
		s = (a+b)%10 * (10 ** c) + s
		x //= 10
		y //= 10
		c += 1
	return s

print(fun_carrylessadd(785,376))
