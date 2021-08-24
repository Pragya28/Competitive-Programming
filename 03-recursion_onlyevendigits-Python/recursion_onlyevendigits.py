# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def getEvenDigits(x, n = 0, c = 0):
	if x == 0:
		return n
	if x % 10 % 2 == 0:
		n = (x%10)*10**c+n
		c += 1
	return getEvenDigits(x//10, n, c)

def onlyEvenDigits(inL, outL = []):
	if len(inL) == 0:
		return outL
	outL.append(getEvenDigits(inL[0]))
	return onlyEvenDigits(inL[1:], outL)

def fun_recursion_onlyevendigits(l): 
		return onlyEvenDigits(l, [])

print(fun_recursion_onlyevendigits([43, 23265, 17, 58344]))