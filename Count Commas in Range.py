# https://leetcode.com/problems/count-commas-in-range/?envType=daily-question&envId=2026-09-08
# Count Commas in Range

class Solution:
    def countCommas(self, n: int) -> int:
        
        answer = 0
        threshold = 1000

        while threshold <= n:
            answer += n - threshold + 1
            threshold *= 1000

        return answer