from dataclasses import dataclass

from helpers import read


@dataclass
class _CubeSetOrBag:
    r: int = 0  # red
    g: int = 0  # green
    b: int = 0  # blue


class CubeSet(_CubeSetOrBag):

    @classmethod
    def from_text(cls, text_description):
        """
        the plain old __init__ class takes values for r, g, b
        this is a syntactic sugar constructor when we just have a text string, which appears frequently

        text_description: something like "3 blue, 4 red, 6 green"
        return: instance of CubeSet
        """
        cubes_text = [c.strip() for c in text_description.split(',')]  # e.g. ["1 red", "2 blue"]
        # turn it into # {"r": 1, "b": 2}:
        cubes_dict = {colour[:1]: int(count) for count, colour in [c.split(' ') for c in cubes_text]}
        return cls(**cubes_dict)

    @property
    def power(self):
        return self.r * self.g * self.b


class CubeGame:
    def __init__(self, text_description: str):
        """
        text_description: the entire row from puzzle input e.g. "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        """
        # id
        game_id_start_char = text_description.find(" ") + 1
        game_id_end_char = text_description.find(":")
        self.id = int(text_description[game_id_start_char:game_id_end_char])

        # sets
        sets_text = [s.strip() for s in text_description[game_id_end_char + 2:].split(';')]
        self.sets = [CubeSet.from_text(s) for s in sets_text]

    @property
    def minimum_viable_set(self):
        r = max([s.r for s in self.sets])
        g = max([s.g for s in self.sets])
        b = max([s.b for s in self.sets])
        return CubeSet(r, g, b)


class CubeBag(_CubeSetOrBag):
    def is_game_possible(self, game: CubeGame) -> bool:
        for cube_set in game.sets:
            if cube_set.r > self.r or cube_set.g > self.g or cube_set.b > self.b:
                return False
        return True


def sum_possible_games(cube_bag: CubeBag, cube_games: list[CubeGame]) -> int:
    possible_ids_sum = 0
    for g in cube_games:
        if cube_bag.is_game_possible(g):
            possible_ids_sum += g.id
    return possible_ids_sum


def sum_minimum_viable_sets(cube_games: list[CubeGame]) -> int:
    min_viable_sets = [g.minimum_viable_set for g in cube_games]
    return sum([s.power for s in min_viable_sets])


if __name__ == "__main__":
    # pt1
    bag = CubeBag(r=12, g=13, b=14)
    games = [CubeGame(line) for line in read.read_file_as_list('y2023/day02/puzzle_input.txt')]
    print(f"sum of possible game ids: {sum_possible_games(bag, games)}")

    # pt2
    print(f"sum of powers for minimum viable sets: {sum_minimum_viable_sets(games)}")
