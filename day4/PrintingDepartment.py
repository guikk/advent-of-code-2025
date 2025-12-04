from copy import deepcopy
import sys
from typing import List
sys.path.append('util')
from runner import Runner

Diagram = List[List[str]]

def adjacents(diagram: Diagram, row: int, col: int) -> List[tuple[int, int]]:
    for i in range(row-1, row+2):
        if i < 0 or i >= len(diagram):
            continue
        for j in range(col-1, col+2):
            if j < 0 or j >= len(diagram[i]):
                continue
            if i == row and j == col:
                continue
            yield (i, j, diagram[i][j])

def is_available(diagram: Diagram, row: int, col: int) -> bool:
    adjacent_rolls = 0
    adjacent_iter = list(adjacents(diagram, row, col))
    for i, j, cell in adjacent_iter:
        if cell == '@':
          adjacent_rolls += 1
        if adjacent_rolls >= 4:
          return False
    return True

def available_rolls(diagram: Diagram) -> int:

  resulting_diagram = deepcopy(diagram)  
  count = 0

  for row in range(len(diagram)):
      # rowstr = ''
      for col in range(len(diagram[row])):
          # rowstr += diagram[row][col]
          if not diagram[row][col] == '@':
              continue
          
          if is_available(diagram, row, col):
              count += 1
              resulting_diagram[row][col] = '.'
              # rowstr = rowstr[:-1] + 'x'

      # print(rowstr)

  return count, resulting_diagram

def available_rolls_w_removals(diagram: Diagram) -> int:
    total_count = 0
    current_diagram = diagram

    while True:
        count, new_diagram = available_rolls(current_diagram)
        if count == 0:
            break
        total_count += count
        current_diagram = new_diagram

    return total_count

def read_input(filename: str) -> Diagram:
    with open(filename) as f:
        lines = f.readlines()

    return list(map(lambda l: list(l.strip()), lines))

if __name__ == "__main__": 
    def part1(diagram: Diagram) -> int:
        count, _ = available_rolls(diagram)
        return count
    Runner(
        read_input,
        "day4/input.txt",
        part1,
        available_rolls_w_removals
    ).run()