# https://leetcode.com/problems/pass-the-pillow/?envType=daily-question&envId=2024-07-06
# Pass the Pillow

class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        cycle = time % (2 * n - 2)

        if cycle < n:
            return  cycle + 1
        else:
            return n - (cycle - (n - 1))