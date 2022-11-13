def solution(x, y):
    x = int(x)
    y = int(y)

    m = [x, y]
    i = 0
    while m != [1, 1]:
        if m[0] == m[1]:
            return "impossible"

        elif 1 in {m[0], m[1]}:
            i += max(m) - min(m)
            return i
        else:
            m = [max(m) - (min(m)), min(m)]
            i += 1
        print m
    return str(i)

print(solution(69, 12))