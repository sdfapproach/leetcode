# https://leetcode.com/problems/robot-return-to-origin/?envType=daily-question&envId=2026-04-05
# Robot Return to Origin

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        v = 0
        h = 0

        for move in moves:

            if move == "U":
                v += 1
            elif move == "D":
                v -= 1
            elif move =="R":
                h -= 1
            elif move =="L":
                h += 1

        if v == 0 and h == 0:
            return True
        else:
            return False