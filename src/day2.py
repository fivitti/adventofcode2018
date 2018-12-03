from collections import Counter
from functools import reduce
from itertools import combinations
from utils.fileutils import read_lines

ACCEPT_DIFFERENCES = 1

def has_repeated_element(counter: Counter, repeats: int):
    return next((True for item in counter.items() if item[1] == repeats), False)

def part1():
    appears = {
        2: 0,
        3: 0
    }

    for line in read_lines(__file__):
        c = Counter(line)
        for appearTimes in appears.keys():
            if has_repeated_element(c, appearTimes):
                appears[appearTimes] += 1
    
    return reduce(lambda x, y: x * y, appears.values())

def are_the_same_with_tolerance(s1: str, s2: str, tolerance: int):
    if len(s1) != len(s2):
        raise Exception('Not supported')

    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if tolerance > 0:
                tolerance -= 1
            else:
                return False
    return True

def find_the_same_with_tolerance(data, tolerance: int):
    for s1, s2 in data:
        if are_the_same_with_tolerance(s1, s2, tolerance):
            return (s1, s2)
    return None

def get_common_part(s1: str, s2: str):
    result = []
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            result.append(c1)

    return str.join('', result)


def part2():
    data = read_lines(__file__)

    to_check = combinations(data, 2)
    the_same_rows = find_the_same_with_tolerance(to_check, ACCEPT_DIFFERENCES)
    if the_same_rows is None:
        return None

    return get_common_part(*the_same_rows)

if __name__ == '__main__':
    print('Part 1: ', part1())
    print('Part 2:', part2())


    
