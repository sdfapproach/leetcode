# https://leetcode.com/problems/unique-3-digit-even-numbers/?envType=daily-question&envId=2026-09-11
# Unique 3-Digit Even Numbers

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        n = len(digits)
        nums = set()

        for i in range(n):
            if digits[i] == 0:
                continue

            for j in range(n):
                if j == i:
                    continue

                for k in range(n):
                    if k == i or k == j:
                        continue

                    if digits[k] % 2 != 0:
                        continue

                    num = (
                        digits[i] * 100
                        + digits[j] * 10
                        + digits[k]
                    )

                    nums.add(num)

        return len(nums)