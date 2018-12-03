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
        self._overlapped_ids = set()

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

                cell_count = len(self._taken_place[row][column])
                if cell_count == 1:
                    self._overlapped_ids.add(self._taken_place[row][column][0])
                if cell_count > 0:
                    self._overlapped_ids.add(claim.id)

                self._taken_place[row][column].append(claim.id)

    def get_overlapped_cells_count(self):
        overlapped = 0
        for row in self._taken_place.values():
            for column in row.values():
                if len(column) > 1:
                    overlapped += 1
        return overlapped

    def get_overlapped_ids(self):
        return self._overlapped_ids

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

    all_ids = set([c.id for c in claims])
    overlapped = area.get_overlapped_ids()

    non_overlapped = all_ids.difference(overlapped)

    print('Part 2:', non_overlapped)

if __name__ == '__main__':
    part1()
    part2()