from math import sqrt, atan2
from itertools import product


def solution(dimensions, your_position, trainer_position, distance):

    ways = {}
    quads = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
    for pos in your_position, trainer_position:
        for refl in product(*[range(-(distance // -d) + 1) for d in dimensions]):
            for quad in quads:
                x, y = [
                    (d * r + (d - p if r % 2 else p)) * q
                    for d, p, r, q in zip(dimensions, pos, refl, quad)
                ]
                print d, p, r, q
                shot_distance = (abs(x - your_position[0]) ** 2 + abs(y - your_position[1]) ** 2) ** 0.5
                shot = atan2(your_position[0] - x, your_position[1] - y)
                if shot_distance > distance:
                    continue
                if shot in ways and shot_distance > abs(ways[shot]):
                    continue

                if pos == your_position:
                    ways[shot] = shot_distance * -1
                else:
                    ways[shot] = shot_distance
    ways_count = [1 for shot_distance in ways.values() if shot_distance > 0]
    return len(ways_count)


print(solution([3, 2], [1, 1], [2, 1], 4))
