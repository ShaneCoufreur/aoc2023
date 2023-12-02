# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/2

from collections import defaultdict

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    @answer(2727)
    def part_1(self) -> int:
        max_red = 12
        max_green = 13
        max_blue = 14
        
        games = self.input
        valid_games = []
        for game in games:
            round, values = game.split(":")
            _, round_id = round.split(" ")
            self.debug(round_id)
            draws = [v.strip() for v in values.split(";")]
            
            d = defaultdict(int)
            for draw in draws:
                cubedraws = [d.strip() for d in draw.split(",")]
                for cb in cubedraws:
                    n, c = cb.split(" ")
                    if( int(n) > d[c] ):
                        d[c] = int(n)
                    self.debug(n, c)
            self.debug(d)
            
            if( d['red'] <= max_red  and d['green'] <= max_green and d['blue'] <= max_blue):
                valid_games.append(int(round_id))

        return sum(valid_games)

    @answer(56580)
    def part_2(self) -> int:
        games = self.input
        game_products = []
        for game in games:
            round, values = game.split(":")
            _, round_id = round.split(" ")
            self.debug(round_id)
            draws = [v.strip() for v in values.split(";")]
            
            d = defaultdict(int)
            for draw in draws:
                cubedraws = [d.strip() for d in draw.split(",")]
                for cb in cubedraws:
                    n, c = cb.split(" ")
                    if( int(n) > d[c] ):
                        d[c] = int(n)
                    self.debug(n, c)
            self.debug(d)
            
            game_products.append(int(d['red']) * int(d['green']) * int(d['blue']))

        return sum(game_products)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
