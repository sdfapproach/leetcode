# https://leetcode.com/problems/stone-removal-game/?envType=daily-question&envId=2026-11-26
# Stone Removal Game

class Solution:
    def canAliceWin(self, n: int) -> bool:

        stones = 10
        alice = True

        while stones > 0 and n >= stones:
            n -= stones
            stones -= 1
            alice = not alice

        return not alice