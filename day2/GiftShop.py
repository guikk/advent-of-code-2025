from typing import List, Tuple

import sys
sys.path.append('util')
from runner import Runner

IDRange = Tuple[str, str]

def repeats_twice(id: str) -> bool:
    size = len(id)

    if not size % 2 == 0:
        return False
    
    half = size // 2

    return id[:half] == id[half:]

def repeats_n_times(id: str) -> bool:
    size = len(id)

    for n in range(2, size+1):
        if size % n != 0:
            continue
        
        part_size = size // n
        part = id[:part_size]

        if (id == part * n):
            return True
    
    return False

def invalids_in_range(id_range: IDRange, invalid_check):
    start, end = id_range
    for id in range(int(start), int(end)+1):
        if invalid_check(str(id)):
            yield id
    
def sum_of_invalids(ranges, invalid_check) -> int:
    total = 0
    for id_range in ranges:
        invalids = list(invalids_in_range(id_range, invalid_check))
        # print(f'{invalids} from {" to ".join(id_range)}')
        total += sum(invalids)
    return total

def read_input(filename: str) -> List[IDRange]:
    with open(filename) as f:
        line = f.readline()

    ranges = line.rstrip().split(',')
    def parse_range(r: str) -> IDRange:
        start, end = r.split('-')
        return (start, end)
    
    return list(map(parse_range, ranges))
    

if __name__ == "__main__":
    def part1(ranges):
        return sum_of_invalids(ranges, repeats_twice)
    def part2(ranges):
        return sum_of_invalids(ranges, repeats_n_times)
    Runner(
        read_input,
        "day2/input.txt",
        part1,
        part2
    ).run()     