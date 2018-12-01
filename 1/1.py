INPUT_FILENAME = 'input.txt'

def part_1():
    frequency = 0

    with open(INPUT_FILENAME, 'rt') as f:
        for line in f.readlines():
            frequency_change = int(line)
            frequency += frequency_change
    return frequency

def part_2():
    frequency = 0
    frequency_occurrences = set()

    with open(INPUT_FILENAME, 'rt') as f:
        while True:
            f.seek(0, 0)
            for line in f.readlines():
                frequency_change = int(line)
                frequency += frequency_change
                if (frequency in frequency_occurrences):
                    return frequency
                else:
                    frequency_occurrences.add(frequency)    

print('Part 1:', part_1())
print('Part 2:', part_2())