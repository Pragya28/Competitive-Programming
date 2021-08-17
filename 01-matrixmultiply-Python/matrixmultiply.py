# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.

def multiply(row, col):
    s = 0
    for i in range(len(row)):
        s += row[i]*col[i]
    return s

def fun_matrixmultiply(m1, m2):
    if len(m1[0]) != len(m2):
        return None
    mtx = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]
    for i in range(len(mtx)):
        row = m1[i]
        for j in range(len(mtx[0])):
            col = [m2[k][j] for k in range(len(m2))]
            mtx[i][j] = multiply(row, col)
    return mtx

print(fun_matrixmultiply([[1,3],[2,4]], [[1,3,2,2], [2,4,5,1]]))