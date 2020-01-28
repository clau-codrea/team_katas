import random

def generate_sequence(offset, size):
    sequence2 = []

    while len(sequence2) < size:
        digits = set(range(10))
        first_elem = random.randint(1, 9)
        last_elements = random.sample(digits - {first_elem}, 9)
        sequence = [first_elem] + last_elements
        sequence1 = int("".join([str(x) for x in sequence]))

        if sequence1 >= offset:
            sequence2.append(sequence1)


    return sequence2


# -----------------------------------------------------------------


def get_sequence(offset, size):
    start = 1023456789
    end = 9876543211
    sequence = []

    if offset < start:
        offset = start

    for number in range(offset, end):
        if check_number(number):
            sequence.append(number)

        if len(sequence) == size:
            break 

    return sequence

def check_number(number):
    seq = set(str(number))

    return len(seq) == 10


