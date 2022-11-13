def solution(n):
    result = []
    array = [i for i in range(1, n)]

    last_index = {0: [-1]}
    for i in range(len(array)):
        for s in list(last_index.keys()):
            new_s = s + array[i]
            if new_s in last_index:
                last_index[new_s].append(i)
            else:
                last_index[new_s] = [i]

    def recur(new_n, max_i):
        for i in last_index[new_n]:
            if i == -1:
                yield []  # Empty sum.
            elif max_i <= i:
                break  # Not our solution.
            else:
                for answer in recur(new_n - array[i], i):
                    answer.append(array[i])
                    yield answer

    for answer in recur(n, len(array)):
        result.append(answer)

    return len(result)


def solution2(n):
    # Make sure that we're building a staircase with more than 3 and less than 200 bricks.
    if 3 <= n <= 200:
        # We are going to be counting the amount of stairs that can be built in a (n + 1)**2 matrix.
        # We are going to store the number of different staircases that can be built in them.
        matrix = [[0 for i in range(n + 1)] for j in range(n + 1)]

        matrix[0][0] = 1  # Our starting state. We can 'build' 1 stair of 0 height from 0 bricks.

        # We start at height 1, as height 0 is our base state.
        for height in range(1, n + 1):
            for bricks in range(0, n + 1):

                # Here we define the states:
                # Initialize the number of different staircases that we built
                # of the last height with the amount of bricks currently available.
                matrix[height][bricks] = matrix[height - 1][bricks]

                if bricks >= height:
                    # If we have more or the same number of bricks than our current height,
                    # we add the amount of stairs that were built of the previous height from
                    # (bricks-height) amount of bricks left.
                    matrix[height][bricks] += matrix[height - 1][bricks - height]

        # We return matrix[n][n] -1 to account for the stair that uses all the bricks in one step.
        return matrix[n][n] - 1

    else:
        return -1


print(solution2(200))
