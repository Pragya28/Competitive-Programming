# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def isTidy(n):
    while (n > 0):
        a = n % 10
        n //= 10
        b = n % 10
        if a < b:
            return False
    return True

def fun_nth_tidynumber(n):
    i = 0
    k = 0
    while i <= n:
        k += 1
        if isTidy(k):
            i += 1
    return k