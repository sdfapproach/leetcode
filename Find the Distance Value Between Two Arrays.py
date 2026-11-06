# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/?envType=daily-question&envId=2026-11-05
# Find the Distance Value Between Two Arrays

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        
        answer = 0

        for a in arr1:
            if all(abs(a - b) > d for b in arr2):
                answer += 1

        return answer