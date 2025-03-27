# https://leetcode.com/problems/minimum-index-of-a-valid-split/?envType=daily-question&envId=2025-03-27
# Minimum Index of a Valid Split

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        x, cnt = Counter(nums).most_common(1)[0]
        cur = 0

        for i, v in enumerate(nums, 1):
            if v == x:
                cur += 1
                if cur * 2 > i and (cnt - cur) * 2 > len(nums) - i:
                    return i - 1
        return -1