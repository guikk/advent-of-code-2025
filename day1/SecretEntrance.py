from typing import Tuple, List
import sys
sys.path.append('util')
from runner import Runner


START_POSITION = 50
DIAL_SIZE = 100

Rotation = Tuple[str, int]

def count_exact_zeros(rotations):
    position = START_POSITION
    zero_count = 0
    for sign, steps in rotations:
        position = (position + sign * steps) % DIAL_SIZE

        if position == 0:
            zero_count += 1
    return zero_count

def count_zeros_clicked(rotations):
    position = START_POSITION
    zero_count = 0
    for sign, steps in rotations:
        for _ in range(steps):
            position = (position + sign) % DIAL_SIZE
            if position == 0:
                zero_count += 1
    return zero_count

def zero_clicks_in_rotation(position: int, rotation: Rotation) -> int:
    sign, steps = rotation

    distance_to_zero = 100 - position if sign == 1 or position == 0 else position

    clicks = 0
    if (steps >= distance_to_zero):
        clicks = 1 + (steps - distance_to_zero) // DIAL_SIZE
    # print(f'From pos {position} with rotation {rotation}, distance to zero is {distance_to_zero}, clicks: {clicks}')
    return clicks


def count_zeros_clicked_optimized(rotations):
    position = START_POSITION
    zero_count = 0
    for sign, steps in rotations:
        zero_count += zero_clicks_in_rotation(position, (sign, steps))
        position = (position + sign * steps) % DIAL_SIZE
    return zero_count


def read_input(filename: str) -> List[Rotation]:
    with open(filename) as f:
        lines = f.readlines()

    def read_line(line: str) -> Rotation:
        direction = line[0]
        sign = -1 if direction == 'L' else 1
        
        steps = int(line[1:].rstrip())
        return (sign, steps)
    
    return list(map(read_line, lines))

if __name__ == "__main__":

    Runner(
        read_input,
        "day1/input.txt",
        count_exact_zeros,
        count_zeros_clicked,
        count_zeros_clicked_optimized
    ).run()