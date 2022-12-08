from typing import List, Tuple

from y2021.helpers import read


def get_coords_of_line(line_coords: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    line = line_coords.replace(" -> ", ",")
    x1, y1, x2, y2 = [int(x) for x in line.split(',')]
    return ((x1, y1), (x2, y2))


def make_posns_same_length(x_posns, y_posns):
    if len(x_posns) == 1:
        x_posns = x_posns * len(y_posns)
    if len(y_posns) == 1:
        y_posns = y_posns * len(x_posns)
    return x_posns, y_posns


def get_points_covered_by_line(start_xy: tuple, finish_xy: tuple, ignore_diagonals: True) -> List[Tuple[int, int]]:
    x1, y1 = start_xy
    x2, y2 = finish_xy
    points = []
    if (x1 == x2 or y1 == y2) or ignore_diagonals is False:  # is horiz/vertical or diagonal acceptable
        x_posns = []
        y_posns = []
        x_step = -1 if x1 > x2 else 1
        y_step = -1 if y1 > y2 else 1
        for x_coord in range(x1, x2 + x_step, x_step):
            x_posns.append(x_coord)
        for y_coord in range(y1, y2 + y_step, y_step):
            y_posns.append(y_coord)
        x_posns, y_posns = make_posns_same_length(x_posns, y_posns)
        points = [p for p in zip(x_posns, y_posns)]
    return points


def get_overlaps(lines: List[str], ignore_diagonals: bool) -> int:
    lines = [get_coords_of_line(l) for l in lines]
    coord_counts = {}
    for line in lines:
        start, fin = line
        for x, y in get_points_covered_by_line(start, fin, ignore_diagonals):
            if x not in coord_counts:
                coord_counts[x] = {y: 1}
            else:
                if y not in coord_counts[x]:
                    coord_counts[x][y] = 1
                else:
                    coord_counts[x][y] += 1
    overlaps = 0
    for x, y_val in coord_counts.items():
        for xy_count in y_val.values():
            if xy_count > 1:
                overlaps += 1
    return overlaps


if __name__ == "__main__":
    # pt1
    line_coords = read.read_file_as_list('y2021/day05/puzzle_input.csv')
    print(get_overlaps(line_coords, ignore_diagonals=True))

    # pt2
    line_coords = read.read_file_as_list('y2021/day05/puzzle_input.csv')
    print(get_overlaps(line_coords, ignore_diagonals=False))
