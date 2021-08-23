# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.

def check(a):
	for i in range(1, len(a)):
		if sum(a[i]) != sum(a[i-1]):
			return (i-1, i)
	return -1

def fixmostlymagicsquare(L):
	rows = check(L)
	c = []
	for i in range(len(L[0])):
		c.append([L[j][i] for j in range(len(L))])
	cols = check(c)
	S = 0
	for i in range(len(L)):
		if i not in rows:
			for j in rows:
				if sum(L[i]) != sum(L[j]):
					rows = j
					S = sum(L[i])
					break
			if isinstance(rows, int):
				break
	for i in range(len(c)):
		if i not in cols:
			for j in cols:
				if sum(c[i]) != sum(c[j]):
					cols = j
					break
			if isinstance(cols, int):
				break
	M = [[0] * len(L) for _ in range(len(L))]
	for i in range(len(M)):
		for j in range(len(M)):
			if i == rows and j == cols:
				M[i][j] = L[i][j] + (S - sum(L[i]))
			else:
				M[i][j] = L[i][j]
	return M
print(fixmostlymagicsquare([[2, 7, 9], [9, 5, 1], [4, 3, 8]]))
