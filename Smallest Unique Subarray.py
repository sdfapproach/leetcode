# https://leetcode.com/problems/smallest-unique-subarray/?envType=daily-question&envId=2026-11-25
# Smallest Unique Subarray

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        BASE = 131
        MASK = (1 << 64) - 1

        prefix = [0] * (n + 1)
        power = [1] * (n + 1)

        for i in range(n):
            prefix[i + 1] = (prefix[i] * BASE + nums[i]) & MASK
            power[i + 1] = (power[i] * BASE) & MASK

        def check(length):
            seen = set()
            duplicate = set()

            for i in range(n - length + 1):
                h = (
                    prefix[i + length]
                    - prefix[i] * power[length]
                ) & MASK

                if h in seen:
                    duplicate.add(h)
                else:
                    seen.add(h)

            return len(seen) > len(duplicate)

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left