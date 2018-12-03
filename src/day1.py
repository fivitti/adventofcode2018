from utils.fileutils import read_lines

def part_1():
    frequency = 0


    for line in read_lines(__file__):
        frequency_change = int(line)
        frequency += frequency_change
    return frequency

def part_2():
    frequency = 0
    frequency_occurrences = set()
    
    while True:
        data = read_lines(__file__)
        for line in data:
            frequency_change = int(line)
            frequency += frequency_change
            if (frequency in frequency_occurrences):
                return frequency
            else:
                frequency_occurrences.add(frequency)    

if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())