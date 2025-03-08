# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/?envType=daily-question&envId=2025-03-08
# Minimum Recolors to Get K Consecutive Black Blocks

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        min_white = k

        for i in range(len(blocks) - k + 1):
            min_white = min(min_white, Counter(blocks[i:i+k])['W'])

        return min_white