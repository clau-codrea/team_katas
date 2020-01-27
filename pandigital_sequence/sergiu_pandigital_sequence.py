DEFAULT_LIST = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]


def find_first(offset):
    default_list = DEFAULT_LIST[:]
    for index, value in enumerate(offset):
        if value in default_list:
            default_list.remove(value)
        else:
            min_value = -1
            minimum_list = default_list[:]
            while min_value < value:
                 if not minimum_list:
                    return []
                 min_value = min(minimum_list)
                 minimum_list.remove(min_value)
            offset[index] = min_value
            default_list.remove(min_value)
    return offset


def as_number(number_list):
    return int("".join([str(number) for number in number_list]))


def as_numbers(numbers_list):
    numbers = [as_number(number_list) for number_list in numbers_list]
    return numbers


def is_addable(number, minimum):
    return as_number(number) > as_number(minimum)


def get_permutations(permutation, k=0):
    solution = []
    if k == len(permutation):
        return [permutation]
    else:
        for i in range(k, len(permutation)):
            permutation[k], permutation[i] = permutation[i], permutation[k]
            solution += get_permutations(permutation[:], k + 1)
            permutation[k], permutation[i] = permutation[i], permutation[k]
    return solution


def get_all_permutations_of(offset, start, end, size):
    if not offset:
        return []
    decreasing_start = end - 2
    all_rotations = []
    while decreasing_start >= start and len(all_rotations) < size:
        current_rotations = []
        for permutation in get_permutations(offset[decreasing_start : end + 1]):
            current_rotations += [offset[:decreasing_start] + permutation]
        current_rotations = sorted(current_rotations, key=as_number)
        for rotation in current_rotations:
            if all_rotations and is_addable(rotation, all_rotations[-1]):
                all_rotations += [rotation]
            elif not all_rotations and as_number(rotation) >= as_number(offset):
                all_rotations = [rotation]
            if len(all_rotations) >= size:
                    break;
        decreasing_start -= 1
    return all_rotations


def get_sequence(offset, size):
    start = 1
    end = 9
    offset = (
        DEFAULT_LIST
        if offset < as_number(DEFAULT_LIST)
        else [int(n) for n in str(offset)]
    )
    result_set = get_all_permutations_of(find_first(offset), start, end, size)
    return as_numbers(result_set)
