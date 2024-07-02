# https://leetcode.com/problems/three-consecutive-odds/?envType=daily-question&envId=2024-07-01
# Three Consecutive Odds

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        odd = 0
        
        for num in arr:

            if num%2 == 1:
                odd += 1
            else:
                odd = 0

            if odd == 3:
                return True

        return False