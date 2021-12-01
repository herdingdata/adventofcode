import os
from typing import List


def read_file_as_list(filepath: str) -> List[str]:
    if not filepath.startswith('/Users'):
        filepath = os.path.join('/Users/andy.herd/dev/py/adventofcode', filepath)
    with open(filepath, 'r') as infile:
        results = [x[:-1] for x in infile.readlines()]  # [:-1] omits the newline char
    return results

