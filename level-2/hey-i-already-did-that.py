def solution(n, b):
    # Create an empty list to store the minion ID's.
    minionId = []

    # Helper function for converting numbers to any base.

    def numberToBase(n, b):
        if n == 0:
            return '0'
        digits = []
        while n:
            digits.append(str(n % b))
            n //= b
        return ''.join(digits[::-1])

    # Append the minionId list with every new n that's created, and return the repeating sequence's length.
    def assigner(n, b):
        minionId.append(n)
        k = len(n)
        x = ''.join(sorted(n, reverse=True))
        y = ''.join(sorted(n))

        n = numberToBase(int(x, b) - int(y, b), b)
        if n == 0:
            return len(minionId[minionId.index(n)::])

        if len(n) < k:
            n = n.zfill(k)
        if n in minionId:
            return len(minionId[minionId.index(n)::])
        else:
            return assigner(n, b)

    return assigner(n, b)
