# https://leetcode.com/problems/jump-game-ix/?envType=daily-question&envId=2026-05-07
# Jump Game IX

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        suffix_min = [float('inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        ans = [0] * n
        start = 0
        prefix_max = float('-inf')
        comp_max = float('-inf')

        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            comp_max = max(comp_max, nums[i])

            if i == n - 1 or prefix_max <= suffix_min[i + 1]:
                for j in range(start, i + 1):
                    ans[j] = comp_max

                start = i + 1
                comp_max = float('-inf')

        return ans