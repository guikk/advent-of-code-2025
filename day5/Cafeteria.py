import sys
from typing import List, Tuple
sys.path.append('util')
from runner import Runner

Range = Tuple[int, int]

class Database:
    def __init__(self, ranges: List[Range], ids: List[int]):
        self.fresh_ranges: List[Range] = ranges
        self.ingredient_ids: List[int] = ids

def fresh_ingredients_from_ids(db: Database) -> int:
    fresh_count = 0

    for ingredient_id in db.ingredient_ids:
        for start, end in db.fresh_ranges:
            if start <= ingredient_id <= end:
                fresh_count += 1
                break

    return fresh_count

def fresh_ingredients_from_ranges(db: Database) -> int:
    return sum(map(lambda r: r[1]-r[0]+1, db.fresh_ranges))

def sort_and_merge_ranges(ranges: List[Range]) -> List[Range]:
    if not ranges:
        return []

    sorted_ranges = sorted(ranges, key=lambda r: r[0])
    merged_ranges = [sorted_ranges[0]]

    for current in sorted_ranges[1:]:
        last_merged = merged_ranges[-1]
        if current[0] <= last_merged[1] + 1:
            merged_ranges[-1] = (last_merged[0], max(last_merged[1], current[1]))
        else:
            merged_ranges.append(current)

    return merged_ranges

def read_input(filename: str) -> Database:
    with open(filename) as f:
        lines = f.readlines()

    ranges = []
    ids = []
    parsing_ranges = True
    
    for line in lines:
        line = line.strip()
        if line == "":
            parsing_ranges = False
            continue
        
        if parsing_ranges:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        else:
            ids.append(int(line))


    db = Database(sort_and_merge_ranges(ranges),ids)
    print(db.fresh_ranges)
    return db

if __name__ == "__main__": 
    Runner(
        read_input,
        "day5/input.txt",
        fresh_ingredients_from_ids,
        fresh_ingredients_from_ranges
    ).run()