from itertools import cycle
from pprint import pprint as pp
import operator


class MemorySpiral:
    """ see description in day03.md

    We describe a position as an (x,y) coordinate on a chart with 4 axes.
    MemorySpiral.positions is a dictionary of integer: coordinate tuple."""
    def __init__(self, max_number):
        self.max_number = max_number
        self.positions = {}
        self._max_x = 0
        self._max_y = 0
        self._min_x = 0
        self._min_y = 0
        self._generate_spiral()
        pp(self.positions)

    def _generate_spiral(self):
        posn_factory = self._next_available_position()
        for posn in range(1, self.max_number + 1):
            self.positions[posn] = next(posn_factory)

    def _next_increment(self):
        posn_increments = cycle([(1, 0), (0, 1), (-1, 0), (0, -1)])
        for increment in posn_increments:
            yield increment

    def _next_available_position(self):
        last_posn = (0, 0)
        increment_factory = self._next_increment()
        increment = next(increment_factory)
        yield last_posn
        while True:
            posn = tuple(map(operator.add, last_posn, increment))
            # pp({'increment: ': increment, 'position: ': posn})
            yield posn
            last_posn = posn
            if self._does_position_break_boundary(posn) is True:
                # we've broken the boundary, change direction for the next one
                increment = next(increment_factory)
                # remember the new max/min values for x and y
                self._store_new_max_min_values(posn)

    def _store_new_max_min_values(self, position):
        self._max_x = max(self._max_x, position[0])
        self._max_y = max(self._max_y, position[1])
        self._min_x = min(self._min_x, position[0])
        self._min_y = min(self._min_y, position[1])

    def _does_position_break_boundary(self, position):
        breaks_boundary = position[0] > self._max_x \
            or position[1] > self._max_y \
            or position[0] < self._min_x \
            or position[1] < self._min_y
        return breaks_boundary  # bool


def get_distance(number):
    """
    :param number: a number which we're starting from in our MemorySpiral
    :return: the number of steps following Manhattan path
             to reach the centre of the spiral
    """
    spiral = MemorySpiral(number)
    position = spiral.positions[number]
    abs_position = (abs(x) for x in position)
    return sum(abs_position)


if __name__ == '__main__':
    number = 347991
    pp(['result: ', get_distance(number)])