# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/3

from functools import partial
from ...base import StrSplitSolution, TextSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 3

    def setup(self) -> None:
        global symbollocations
        symbols = set()
        symbollocations = set()
        global gearlocs
        gearlocs = set()
        for row, line in enumerate(self.input):
            for col, val in enumerate(line):
                if val != "." and not (val.isnumeric()):
                    symbols.add(val)
                    symbollocations.add( (col, row) )
                    if val == "*":
                        gearlocs.add( (col, row) )

        global numbers
        numbers = []
        numactive = False
        width = len(self.input[0])
        current = ""
        x1 = 0
        x2 = 0
        for row, line in enumerate(self.input):
            for col, val in enumerate(line):
                if not numactive and (val == "." or val in symbols ):
                    continue
                elif not (numactive) and val.isnumeric():
                    current = val
                    numactive = True
                    x1 = col
                elif numactive and (val == "." or val in symbols):
                    new = int(current)
                    x2 = col-1
                    numbers.append((new, x1, x2, row))
                    numactive = False
                    current = ""
                elif numactive and val.isnumeric():
                    current += val
                    if col == width - 1:
                        new = int(current)
                        x2 = col
                        numbers.append((new, x1, x2, row))
                        numactive = False
                        current = ""

    def part_1(self) -> int:
        answer = 0
        for num, x1, x2, row in numbers:
            borders = set()
            for y in range(row-1,row+2):
                for x in range(x1-1,x2+2):
                    borders.add((x, y))
            intersect = symbollocations & borders
            if len(intersect) > 0:
                answer += num
        return answer

    def part_2(self) -> int:
        answer = 0
        for gearX, gearY in gearlocs:
            borders = set()
            neighbours = []
            for x in range(gearX-1, gearX+2):
                for y in range(gearY-1, gearY+2):
                    borders.add( (x, y) )
            for num, x1, x2, y in numbers:
                if( x1, y) in borders or ( x2, y) in borders:
                    neighbours.append(num)
            if len(neighbours) == 2:
                n1, n2 = neighbours
                answer += n1*n2
        return answer

    @answer((535078, 75312571))
    def solve(self) -> tuple[int, int]:
        self.setup()
        return self.part_1(), self.part_2()
