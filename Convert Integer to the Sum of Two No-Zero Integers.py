# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/?envType=daily-question&envId=2025-09-08
# Convert Integer to the Sum of Two No-Zero Integers

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        for i in range(1, n):

            a = n - i

            print(a, i)

            if "0" not in str(a) and "0" not in str(i):
                return [a, i]