import re
from typing import Dict, List, Iterable
from utils.fileutils import read_lines

pattern = re.compile(r'''\#(?P<id>\d+)        # id
                         \s@\s                # delimeter
                         (?P<left_offset>\d+) # left offset
                         ,                    # offset delimiter
                         (?P<top_offset>\d+)  # top offset
                         :\s                  # delimiter
                         (?P<width>\d+)       # width
                         x                    # size delimiter
                         (?P<height>\d+)''',  # height
                         re.VERBOSE)  

class Claim:
    def __init__(self, id, left_offset, top_offset, width, height):
        self.id = id
        self.left_offset = left_offset
        self.top_offset = top_offset
        self.width = width
        self.height = height

    @classmethod
    def parse(cls, input: str):
        match = pattern.match(input)
        raw = [match.group('id'), match.group('left_offset'),
                match.group('top_offset'), match.group('width'),
                match.group('height')]
        ints = [int(i) for i in raw]
        return Claim(*ints)

class Area:
    def __init__(self):
        self._taken_place: Dict[int, Dict[int, List[int]]]  = {}

    @classmethod
    def range(self, from_index: int, size: int) -> Iterable[int]:
        return range(from_index, from_index + size, 1)

    def take_place(self, claim: Claim):
        for row in Area.range(claim.top_offset, claim.height):
            if row not in self._taken_place:
                self._taken_place[row] = {}

            for column in Area.range(claim.left_offset, claim.width):
                if column not in self._taken_place[row]:
                    self._taken_place[row][column] = []

                self._taken_place[row][column].append(claim.id)

    def get_overlapped_cells_count(self):
        overlapped = 0
        for row in self._taken_place.values():
            for column in row.values():
                if len(column) > 1:
                    overlapped += 1
        return overlapped

    def is_overlapped(self, claim: Claim):
        for row in Area.range(claim.top_offset, claim.height):
            for column in Area.range(claim.left_offset, claim.width):
                if len(self._taken_place[row][column]) != 1:
                    return True
        return False

def create_data():
    input = read_lines(__file__)
    claims = [Claim.parse(r) for r in input]
    area = Area()

    for claim in claims:
        area.take_place(claim)
    
    return (claims, area)

def part1():
    _, area = create_data()

    print('Part 1:', area.get_overlapped_cells_count())

def part2():
    claims, area = create_data()

    non_overlapped = [c.id for c in claims if not area.is_overlapped(c)]

    print('Part 2:', non_overlapped)

if __name__ == '__main__':
    part1()
    part2()