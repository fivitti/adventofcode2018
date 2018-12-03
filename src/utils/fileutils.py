import os.path
from typing import List

def read_lines(filename, directory='inputs', extension='.txt') -> List[str]:
    filename = os.path.basename(filename)
    filename, _ = os.path.splitext(filename)
    path = os.path.join(directory, filename + extension)
    path = os.path.normpath(path)
    path = os.path.abspath(path)

    with open(path, 'rt') as f:
        return (r.rstrip('\n') for r in f.readlines())