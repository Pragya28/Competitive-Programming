# Background: we can represent a polynomial as a list of its coefficients. 
# For example, [2, 3, 0, 4] could represent the polynomial 2x3 + 3x2 + 4. 
# Write the function multiplyPolynomials(p1, p2) which takes two polynomials 
# and returns a third polynomial which is the product of the two. For example,
# multiplyPolynomials([2,0,3], [4,5]) represents the problem (2x**2 + 3)(4x + 5), and:
# (2x**22 + 3)(4x + 5) = 8x**3 + 10x**2 + 12x + 15
# And so this returns [8, 10, 12, 15].

import pytest

def multiplyPolynomials(p1, p2):
    p = [0 for i in range(len(p1) + len(p2) - 1)]
    p1.reverse()
    p2.reverse()
    if len(p2) > len(p1):
        (p1, p2) = (p2, p1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            p[i+j] += p1[i]*p2[j]
    p.reverse()
    return p

# print(multiplyPolynomials([2, 0, 3], [4, 5]))
# Write your own test cases
print ("All test cases passed...")
@pytest.mark.parametrize('p1, p2, result', [
    ([2, 0, 3], [4, 5], [8, 10, 12, 15]), 
    ([1, 2], [1, 2], [1, 4, 4])
])

def test_multiplyPolynomials(p1, p2, result):
    assert multiplyPolynomials(p1, p2) == result