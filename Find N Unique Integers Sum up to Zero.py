# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/?envType=daily-question&envId=2025-09-07
# Find N Unique Integers Sum up to Zero

class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        arr = []

        for i in range(1, n//2+1):
            arr.append(i)
            arr.append(-i)

        if n % 2 == 1:
            arr.append(0)

        return arr