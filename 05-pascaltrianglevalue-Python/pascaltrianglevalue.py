# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




def fun_pascaltrianglevalue(row, col):
	if row < 0 or col < 0 or row < col:
		return 0
	if row == 0:
		return 1
	if col == 0 or col == row:
		return 1
	r = [1, 1]
	for i in range(2, row+1):
		nR = [1]
		for j in range(1, i):
			k = r[j-1] + r[j]
			nR.append(k)
		nR.append(1)
		r = nR
	return r[col]