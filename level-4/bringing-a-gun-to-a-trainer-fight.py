from math import atan2
from itertools import product


def solution(dimensions, your_position, trainer_position, distance):
    # We are going to solve this problem by creating reflections of the targets.

    ways = {}
    quads = [[1, 1], [-1, 1], [1, -1], [-1, -1]]

    # Nest a loop to reflect our and the target's position across every dimension, creating reflections of
    # the room based on the distance our shot can travel (-(distance // -d) + 1).
    for pos in your_position, trainer_position:
        for refl in product(*[range(-(distance // -d) + 1) for d in dimensions]):
            for quad in quads:
                # Here we define x, y for every possible reflection in the room we could hit.
                # This is achieved by zipping together our variables that define an x, y coordinate,
                # and calculating all possible outcomes.
                x, y = [
                    (d * r + (d - p if r % 2 else p)) * q
                    for d, p, r, q in zip(dimensions, pos, refl, quad)
                ]
                # Then we calculate the distance of the shot from our position, and the way the bullet travels.
                shot_distance = (abs(x - your_position[0]) ** 2 + abs(y - your_position[1]) ** 2) ** 0.5
                heading = atan2(your_position[0] - x, your_position[1] - y)

                # We filter that no shots that would hit a farther target, or is farther away than the range of
                # our weapon will make it to the final dictionary.
                if shot_distance > distance:
                    continue
                if heading in ways and shot_distance > abs(ways[heading]):
                    continue

                # We filter the shots that if it would hit us, we just set the shot_distance to negative
                # and count only the positive distances at the end.
                if pos == your_position:
                    ways[heading] = shot_distance * -1
                else:
                    ways[heading] = shot_distance
    ways_count = [1 for shot_distance in ways.values() if shot_distance > 0]
    return len(ways_count)


print(solution([300,275], [150,150], [185,100], 500))
