# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/?envType=daily-question&envId=2024-01-03
# Number of Laser Beams in a Bank

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        laser = 0
        last_floor = 0

        for idx, floor in enumerate(bank):
            
            if "1" not in floor:
                continue
            else:
                num = floor.count("1")

                if last_floor == 0:
                    last_floor = num
                    continue

                laser += last_floor * num
                last_floor = num

        return laser