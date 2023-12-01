# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/1

from ...base import StrSplitSolution, answer
import re

class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    @answer(54632)
    def part_1(self) -> int:
        inp = self.input
        total = 0
        for i in inp:
            matches = re.findall("1|2|3|4|5|6|7|8|9|0", i)
            res = int("".join((matches[0], matches[-1])))
            self.debug(res)
            total += res
        return total
    
    def convertToInt(self, str: str) -> str:
        str = str.replace("one", "1")
        str = str.replace("two", "2")
        str = str.replace("three", "3")
        str = str.replace("four", "4")
        str = str.replace("five", "5")
        str = str.replace("six", "6")
        str = str.replace("seven", "7")
        str = str.replace("eight", "8")
        str = str.replace("nine", "9")
        str = str.replace("zero", "0")

        return str

    @answer(54019)
    def part_2(self) -> int:
        inp = self.input
        total = 0
        for i in inp:
            #fix overlap in regex
            matches = re.findall(r"(?=(1|2|3|4|5|6|7|8|9|0|one|two|three|four|five|six|seven|eight|nine|zero))", i)
            res = int("".join((self.convertToInt(matches[0]), self.convertToInt(matches[-1]))))
            total += res

        return total