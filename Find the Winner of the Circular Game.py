# https://leetcode.com/problems/find-the-winner-of-the-circular-game/?envType=daily-question&envId=2024-07-08
# Find the Winner of the Circular Game

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        circular = [i + 1 for i in range(n)]
        idx = 0

        while len(circular) > 1:

            idx = (idx + k - 1) % len(circular)
            
            circular.pop(idx)

        return circular[0]