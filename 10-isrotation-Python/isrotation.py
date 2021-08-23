# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotated(str1, str2):
	if len(str1) != len(str2):
		return False
	for i in range(len(str1)):
		if str1 == str2:
			return True
		str2 = str2[1:] + str2[0]
	return False

def isrotation(x, y):
	if x == y:
		return True
	s1 = str(x)
	s2 = str(y)
	return isrotated(s1, s2)