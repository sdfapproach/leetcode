# https://leetcode.com/problems/count-symmetric-integers/?envType=daily-question&envId=2025-04-11
# Count Symmetric Integers

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        count = 0

        for i in range(low, high + 1):
            s = str(i)
            length = len(s)

            if length % 2 == 0:
                half = length // 2
                first_half = sum(int(c) for c in s[:half])
                second_half = sum(int(c) for c in s[half:])
                if first_half == second_half:
                    count += 1

        return count