def solution(n):
    # Number of steps required to get to 1, at n = 1 i = 0
    i = 0
    n = int(n)

    if n <= 1:
        return i

    # Repeat processing the number while it's higher than 1.
    while n > 1:

        # If the number is dividable by 2, take that step.
        if n % 2 == 0:
            n /= 2
            i += 1

        # If the number - 1 is dividable by 4, subtract 1, and then divide by 2.
        # If n == 3, we also want to take this step.
        # Even though 3 is not dividable by 4 this is the fastest way to 1.
        # This counts as 2 steps total.
        elif (n - 1) % 4 == 0 or n == 3:
            n -= 1
            n /= 2
            i += 2

        # In every other case, we are going to add 1, then divide by 2.
        # This counts as 2 steps total.
        else:
            n += 1
            n /= 2
            i += 2

    return i


print(solution(11))
