from enum import Enum
import sys


class Direction(Enum):
    UP = '('
    DOWN = ')'


if __name__ == "__main__":
    if sys.argv[1] == 'part1':
        floor_pos = 0
        with open('./Day1/directions.txt', 'r', encoding="utf-8") as f:
            read_data = f.read()
            for ch in read_data:
                if ch == Direction.UP.value:
                    floor_pos += 1
                if ch == Direction.DOWN.value:
                    floor_pos -= 1
        print(floor_pos)

    if sys.argv[1] == 'part2':
        floor_pos = 0
        char_pos = 0
        with open('./Day1/directions.txt', 'r', encoding="utf-8") as f:
            read_data = f.read()
            for ch in read_data:
                if floor_pos < 0:
                    break
                if ch == Direction.UP.value:
                    floor_pos += 1
                if ch == Direction.DOWN.value:
                    floor_pos -= 1
                char_pos += 1
        print(char_pos)

