# https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/?envType=daily-question&envId=2026-10-12
# Apply Operations on Array to Maximize Sum of Squares

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        
        MOD = 10**9 + 7

        bits = [0] * 31

        for num in nums:
            for i in range(31):
                if num & (1 << i):
                    bits[i] += 1

        answer = 0

        for _ in range(k):
            num = 0

            for i in range(31):
                if bits[i] > 0:
                    num |= (1 << i)
                    bits[i] -= 1

            answer = (answer + num * num) % MOD

        return answer