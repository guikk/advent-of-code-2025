import sys
from typing import List, NamedTuple
sys.path.append('util')
from runner import Runner

RawWorksheet = List[str]

class Problem(NamedTuple):
    numbers: List[int]
    operation: str

class Worksheet:
    problems: List[Problem]
    def __init__(self, rws: RawWorksheet):
        self.problems = []

        split_ws = [line.strip().split() for line in rws]

        num_problems = len(split_ws[0])
        num_lines = len(split_ws) - 1

        number_lines, op_line = split_ws[:num_lines], split_ws[num_lines]

        for i in range(num_problems):
            operation = op_line[i]
            numbers = [int(number_lines[j][i]) for j in range(num_lines)]
            self.problems.append(Problem(numbers, operation))

class CephalopodWorksheet(Worksheet):
    def __init__(self, rws: RawWorksheet):
        self.problems = []

        problem_start = True
        curr_problem = None
        for j in range(len(rws[0])):
            col = ''.join([rws[i][j] for i in range(len(rws))])
            if col.strip() == "":
                self.problems.append(curr_problem)
                problem_start = True
                continue

            if (problem_start):
                operation = col[-1]
                curr_problem = Problem([], operation)
                problem_start = False

            number = int(col[:-1].strip())
            curr_problem.numbers.append(number)

        self.problems.append(curr_problem)



operations = {
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y,
}

def sum_of_problems(ws: Worksheet) -> int:
    total = 0
    for numbers, operation in ws.problems:
        op = operations[operation]
        problem_result = numbers[0]

        for nl in numbers[1:]:
            problem_result = op(problem_result, nl)

        total += problem_result

    return total

def read_input(filename: str) -> RawWorksheet:
    with open(filename) as f:
        lines = f.readlines()
    return [line.removesuffix('\n') for line in lines]

if __name__ == "__main__": 

    def human_math(ws: RawWorksheet) -> int:
        worksheet = Worksheet(ws)
        return sum_of_problems(worksheet)
    
    def cephalopod_math(ws: RawWorksheet) -> int:
        worksheet = CephalopodWorksheet(ws)
        return sum_of_problems(worksheet)

    Runner(
        read_input,
        "day6/input.txt",
        human_math,
        cephalopod_math
    ).run()