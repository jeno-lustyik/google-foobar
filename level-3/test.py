def solution(x, y):
    if x < 1 or y < 1:
        return -1

    x = int(x)
    y = int(y)

    m = [x, y]
    i = 0

    while m != [1, 1]:
        if 1 in {m[0], m[1]}:
            i += max(m) - min(m)
            return str(i)

        elif max(m) % min(m) == 0:
            return "impossible"

        else:
            i += (max(m) // min(m))
            m = [max(m) % min(m), min(m)]
        print 
    return str(i)


print(solution(4, 7))
