from itertools import combinations

def solution(num_buns, num_required):
    # Create an empty keyring for each bunny:
    rings = [[] for i in xrange(num_buns)]

    # We will use the combinations function to generate how many ways we can distribute the keys needed.
    # Using enumeration, we are going to have indexes that match our key numbers, and combinations
    # sorted in lexicographic order. Adding each key to the rings matching the index in the combination
    # will yield us the lexicographically least way of distributing the keys.
    for key, bunnies in enumerate(combinations(xrange(num_buns), num_buns - num_required + 1)):
        for bunny in bunnies:
            rings[bunny].append(key)

    return rings


print(solution(5, 3))
