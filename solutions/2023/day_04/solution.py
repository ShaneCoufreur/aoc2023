# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/4

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 4

    @answer(25183)
    def part_1(self) -> int:
        cards  = [card for card in self.input]
        total = 0
        for card in cards:
            _, values = card.split(":")
            winning, own = values.split("|")
            winning = set([int(i) for i in winning.strip().split(" ") if i])
            own = set([int(i) for i in own.strip().split(" ") if i])

            intersect = winning & own
            s = 0
            for _ in intersect:
                if s == 0:
                    s = 1
                else:
                    s = s+s
            total += s
        return total

    @answer(5667240)
    def part_2(self) -> int:
        cards  = [card for card in self.input]
        newcards = []
        for card in cards:
            title, values = card.split(":")
            _, roundnumber = [i for i in title.strip().split(" ") if i]
            winning, own = values.split("|")
            winning = set([int(i) for i in winning.strip().split(" ") if i])
            own = set([int(i) for i in own.strip().split(" ") if i])

            intersect = winning & own
            newcards.append([roundnumber, len(intersect), 1])
        
        for rn, win, copies in newcards:
            for i in range(win):
                newcards[int(rn)+i][2] += copies
        sums = 0

        for _, _, copies in newcards:
            sums += copies
        return sums

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
