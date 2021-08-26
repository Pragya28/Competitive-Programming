# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def sumDigits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def fun_nth_smithnumber(n):
    i = 0
    x = 3
    while i <= n:
        x += 1
        if not isPrime(x):
            k = x
            pf = []
            f = 2
            while f <= k:
                if k % f == 0:
                    if isPrime(f):
                        pf.append(f)
                    k //= f
                else:
                    f += 1
            s = 0
            for f in pf:
                s += sumDigits(f)
            if s == sumDigits(x):
                i += 1
    return x

print(fun_nth_smithnumber(1))