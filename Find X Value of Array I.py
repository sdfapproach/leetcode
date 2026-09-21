# https://leetcode.com/problems/find-x-value-of-array-i/?envType=daily-question&envId=2026-09-21
# Find X Value of Array I

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        
        result = [0] * k
        dp = [0] * k

        for num in nums:
            num %= k

            new_dp = [0] * k

            new_dp[num] += 1

            for r in range(k):
                if dp[r]:
                    nr = (r * num) % k
                    new_dp[nr] += dp[r]

            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result