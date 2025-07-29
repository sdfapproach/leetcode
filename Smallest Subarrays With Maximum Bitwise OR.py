# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/?envType=daily-question&envId=2025-07-29
# Smallest Subarrays With Maximum Bitwise OR

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        suffix_or = [0]*n
        cur = 0
        for i in range(n-1, -1, -1):
            cur |= nums[i]
            suffix_or[i] = cur

        next_idx = [n]*31
        answer = [0]*n

        for i in range(n-1, -1, -1):
            v = nums[i]
            for b in range(31):
                if (v >> b) & 1:
                    next_idx[b] = i

            farthest = i
            goal = suffix_or[i]
            for b in range(31):
                if (goal >> b) & 1:
                    if next_idx[b] > farthest:
                        farthest = next_idx[b]

            answer[i] = farthest - i + 1

        return answer