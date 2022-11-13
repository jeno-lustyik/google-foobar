from decimal import getcontext, Decimal


# This problem is the Beatty sequence: https://oeis.org/A001951
def solution(s):
    # We set our calculations precision to 101 decimals, which will help us get back the correct result
    # even at 10^100 characters, since 2**0.5 is an irrational number
    getcontext().prec = 101

    # We can set up a recursive solution to the problem, since at each step,
    # we multiply n with (2**0.5 - 1), and the value decreases exponentially.
    def sub(n):
        while n != 0:
            j = int((Decimal(2).sqrt() - 1) * n)
            return n * j + n * (n + 1) / 2 - j * (j + 1) / 2 - sub(j)
        return 0

    return str(sub(int(s)))


print(solution('5'))
