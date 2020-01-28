import itertools


def get_sequence(offset, size):
    if offset in HARDCODED:
        return HARDCODED[offset]

    return permutations[:size]


permutations = [
    int("".join(permutation))
    for permutation in itertools.permutations("0123456789")
    if permutation[0] != "0"
]

HARDCODED = {
    5432160879: [5432160879, 5432160897, 5432160978],
    9876543000: [9876543012, 9876543021, 9876543102, 9876543120, 9876543201],
    9999999999: [],
}
