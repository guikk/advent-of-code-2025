import sys
sys.path.append('util')
from runner import Runner

def joltage2(bank: str) -> int:
    
    start_max = '0'
    start_index = 0

    for i, battery in enumerate(bank[:-1]):
        if battery > start_max:
            start_max = battery
            start_index = i

    end_max = '0'
    for battery in bank[start_index+1:]:
        if battery > end_max:
            end_max = battery

    # print(f'Bank: {bank}, start max: {start_max}, end max: {end_max}')
        
    return int(f'{start_max}{end_max}')

def joltage_n(bank: str, n: int) -> int:
    
    if len(bank) < n:
        raise ValueError(f'Bank size {len(bank)} is smaller than n={n}')

    joltage = ''

    battery_index = 0
    for position in range(n):
      battery_max = '0'
      left_to_choose = bank[battery_index:len(bank)-n+position+1]
      for i, battery in enumerate(left_to_choose, battery_index):
          if battery > battery_max:
              battery_max = battery
              battery_index = i+1

      # print(f'Position {position}, left to choose: {left_to_choose}, picked battery: {battery_max}')
      joltage += battery_max

    # print(f'Bank: {bank}, joltage: {joltage}')        
    return int(joltage)

def total_joltage(banks, joltage_fn):
    return sum(map(joltage_fn, banks))

def read_input(filename: str):
    with open(filename) as f:
        lines = f.readlines()

    return list(map(str.strip, lines))

if __name__ == "__main__":
    def part1_size2_joltage(banks):
        return total_joltage(banks, joltage2)
    
    def part2_size12_joltage(banks):
        return total_joltage(banks, lambda b: joltage_n(b, 12))
    
    Runner(
        read_input,
        "day3/input.txt",
        part1_size2_joltage,
        part2_size12_joltage
    ).run()