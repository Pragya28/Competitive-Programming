# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

import math as m

def distance(x1, y1, x2, y2):
	return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

def trianglearea(s1, s2, s3):
	s = (s1 + s2 + s3)/2
	a = m.sqrt(s * (s-s1) * (s-s2) * (s-s3))
	return a

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	s1 = distance(x1, y1, x2, y2)
	s2 = distance(x2, y2, x3, y3)
	s3 = distance(x3, y3, x1, y1)
	return trianglearea(s1, s2, s3)